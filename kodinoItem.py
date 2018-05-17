import json, os, glob, sys
import redis
import random
import subprocess
import hashlib
import threading
import shutil
import glob

from kodinoPlugins import KodinoPlugins
import settings
    
kodinoPlugin = None

redis_connection = redis.StrictRedis(host=settings.REDIS_HOST, port= settings.REDIS_PORT,db= settings.REDIS_DB)

def getKodinoPlugin():
    global kodinoPlugin
    if kodinoPlugin == None:
        kodinoPlugin = KodinoPlugins()
    return kodinoPlugin
    
def addStat(key, path , value = 1):
    pathkey  = "/".join(x[0] for x in path)
    rediskey = "stats:%s:%s" % (key, pathkey)
    redis_connection.incrby(rediskey, value )
    redis_connection.expire(rediskey, settings.CACHETIME_STATS)    

class KodinoItem():
    def __init__(self, addon, url, title, isFolder, thumbnailImage, requireKeyboard, parent ):
        self.parent = parent
        self.addon = addon 
        self.isAdult = self.addon.isAdult # this is not automagically here, to mark addons as adult, add them to settings.py! 
        self.url = url #internal kodi url, or sometimes http url for playable items
        self.title = title
        self.isFolder = isFolder
        self.thumbnailImage = thumbnailImage
        self.requireKeyboard = requireKeyboard
        
        self.hash = hashlib.sha256(("%s\t%s" % (self.addon.id, self.url)).encode("UTF-8")).hexdigest()[0:16]
        self.cache_key = "cache:%s:%s" % (self.addon.id, self.url)
        
        self.handle = "%s" % random.randint(0,2000000000)
        self.keyboardInput = None
    
    def getPath(self):
        pathitems = []
        pathitem = self
        while pathitem != None:
            pathitems.append(pathitem)
            pathitem = pathitem.parent
        pathitems = pathitems
        path = []
        for pathitem in pathitems[::-1]:
            path.append([pathitem.hash, pathitem.title])
            if pathitem.requireKeyboard == True:
                if pathitem.keyboardInput != None:
                    path.append([pathitem.keyboardInput, pathitem.keyboardInput])
        return path
    
    def getSubItems(self, keyboardInput = None):
        self.keyboardInput = keyboardInput    
        if self.requireKeyboard == True and keyboardInput == None:
            raise Exception("This item requires Keyboard input")
        
        if keyboardInput != None:
            key = "%s:%s:keyboard" % (self.addon.id, self.handle)
            redis_connection.set(key, keyboardInput)
            redis_connection.expire(key, settings.TIMEOUT_XBMCWRAPPER + 5)
            self.cache_key = "cache:%s:%s:keyboard:%s" % (self.addon.id, self.url, keyboardInput)
        else:
            self.cache_key = "cache:%s:%s" % (self.addon.id, self.url)
        
        itemstrings = redis_connection.lrange( self.cache_key, 0, -1 )
        if itemstrings == [] or settings.CACHE_DISABLED == True:  # actually call addon
            itemstrings = self._execute()
            
        subitems = []        
        for itemstring in itemstrings:
            item = json.loads(itemstring.decode("UTF-8"))
            isFolder = True
            thumbnailImage = ""
            if item["key"] == "xbmcplugin:addDirectoryItem":
                if item["isfolder"] == False or item["listitem"]["isfolder"] == False:
                    isFolder = False
                if "isplayable" in item["listitem"] and item["listitem"]["isplayable"] == True:
                    isFolder = False
                if "thumbnailimage" in item["listitem"] and item["listitem"]["thumbnailimage"] != None and len( item["listitem"]["thumbnailimage"]) > 8:
                    thumbnailImage = item["listitem"]["thumbnailimage"]
                if thumbnailImage == "" and "fanart_image" in  item["listitem"] and item["listitem"]["fanart_image"] != None and len( item["listitem"]["fanart_image"]) > 8:
                    thumbnailImage = item["listitem"]["fanart_image"]
                if thumbnailImage.startswith("/http"):
                    thumbnailImage = thumbnailImage[1:]
                subaddon = self.addon
                if item["url"].startswith("plugin://"):
                    subaddonid =  item["url"].split("plugin://")[1].split("/")[0]
                    if subaddonid !=  self.addon.id:
                        s = getKodinoPlugin().getInstalledById(subaddonid)   
                        if s != None:
                            subaddon = s
                        else:   
                            print("SUBADDON NAMED %s not FOUND" % subaddonid)
                subitem = KodinoItem(subaddon, item["url"], item["listitem"]["title"], isFolder, thumbnailImage, False, self)
                subitems.append(subitem)   
            if item["key"] == "xbmc_PlayList:add":
                subaddon = self.addon
                if item["url"].startswith("plugin://"):
                    subaddonid =  item["url"].split("plugin://")[1].split("/")[0]
                    if subaddonid !=  self.addon.id:
                        s = getKodinoPlugin().getInstalledById(subaddonid)                
                        if s != None:
                            subaddon = s
                        else:   
                            print("SUBADDON NAMED %s not FOUND" % subaddonid)
                if item["listitem"] == None:
                    subitem = KodinoItem(subaddon, item["url"], "video has no title", False, "", False, self)
                    subitems.append(subitem) 
                else:
                    print("LISTITEM IS NOT NONE")
                    
                
            if item["key"] == "Keyboard:getText": # requireKeyboard
                print("requireKeyboard, returning only one item")
                subitems = []
                subitems.append(KodinoItem(self.addon, self.url, self.title, self.isFolder, self.thumbnailImage, True, self))
                return subitems
            if item["key"] == "xbmc:executebuiltin": # executebuiltin
                function = item["function"]
                command  = function.split("(")[0]    
                if command == "Container.Update":
                    url = function.split("Container.Update(")[1].split(")")[0]
                    if url.startswith("plugin://"):
                        subaddonid =  url.split("plugin://")[1].split("/")[0]
                        subaddon = getKodinoPlugin().getInstalledById(subaddonid)      
                        subitem = KodinoItem(subaddon, url, "Dummy", True, "", False, self)
                        tmp_subitems = subitem.getSubItems()
                        for tmp_subitem in tmp_subitems:
                            tmp_subitem.parent = self
                        subitems.extend(tmp_subitems)
                #self.itemType = "search"
                
        addStat("upcoming:videos_found", self.getPath(), len([0 for x in subitems if x.isFolder == False]))
        return subitems         
         
    def getPlaybackUrl(self):
        if self.isFolder == True:
            raise Exception("Item '%s' '%s' is not a file" % (self.addon.id, self.title))
        self.cache_key = "cache:%s:%s" % (self.addon.id, self.url)
        playbackUrl = ""

        if self.url.startswith("http://") or self.url.startswith("https://"):
            playbackUrl = self.url
        else:
            itemstrings = redis_connection.lrange( self.cache_key, 0, -1 )
            if itemstrings == [] or settings.CACHE_DISABLED == True:  # actually call addon
                itemstrings = self._execute()
            for itemstring in itemstrings:
                item = json.loads(itemstring.decode("UTF-8"))
                if item["key"] == "Player:play":
                    playbackUrl = item["url"]
                if item["key"] == "xbmcplugin:setResolvedUrl":
                    playbackUrl = item["url"]
            if playbackUrl == None:
                playbackUrl = ""      
            if playbackUrl.startswith("plugin://"):
                addonid =  playbackUrl.split("plugin://")[1].split("/")[0]
                addon = getKodinoPlugin().getInstalledById(addonid)
                subitem = KodinoItem(addon, playbackUrl, "playback dummy", "file", "", False, self)
                playbackUrl = subitem.getPlaybackUrl()   
        if playbackUrl == None:
            playbackUrl = ""
        if playbackUrl.find('|Cookie=') != -1:
            print("Removed cookie parameter from playback url")
            playbackUrl = playbackUrl.split('|Cookie=')[0]
        if playbackUrl.find('|User-agent=') != -1:
            print("Removed User-agent parameter from playback url")
            playbackUrl = playbackUrl.split('|User-agent=')[0]
        if playbackUrl.find('|Referer=') != -1:
            print("Removed Referer parameter from playback url")
            playbackUrl = playbackUrl.split('|Referer=')[0]
        if playbackUrl.find('|') != -1:
            print("Removed parameters from playback url")
            playbackUrl = playbackUrl.split('|')[0]
            
        #print("PlaybackUrl: '%s'" % playbackUrl)
        return playbackUrl
     
    def getDuration(self):
        url = self.getPlaybackUrl()
        duration = redis_connection.get("%s:duration" % (self.cache_key))
        duration = 0
        if url != "":
            #  'ffprobe -v error -select_streams v:0 -show_entries stream=duration -of default=noprint_wrappers=1:nokey=1 input.mp4'
            stdout = self._subprocess(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=duration", "-of", "default=noprint_wrappers=1:nokey=1",  url], settings.TIMEOUT_GETDURATION)
            try:
                duration = int(float(stdout))
            except:
                duration = 0
            if duration == 0 or duration < 0 or duration > 99999:
                #'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 '
                stdout = self._subprocess(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", url], settings.TIMEOUT_GETDURATION)
                try:
                    duration = int(float(stdout))
                    if duration < 0 or duration > 99999:
                        duration = 0
                except:
                    duration = 0
        key = "%s:duration" % (self.cache_key)
        redis_connection.set(key, duration) 
        redis_connection.expire(key, settings.CACHETIME_DURATION)
        return duration 

     
    def _execute(self):
        self.process = None
        def target():
            executable = self.addon.getExtentionsByPoint("xbmc.python.pluginsource")[0].library
            my_env = os.environ.copy()
            my_env["PYTHONIOENCODING"] = "UTF-8"
            #0  wrapper.py
            #1  plugin id eg plugin.video.demo1
            #2  executable, for example default.py
            #3	The base URL of your add-on, e.g. 'plugin://plugin.video.demo1/'
            #4	The process handle for this add-on, as a numeric string
            #5	The query string passed to your add-on, e.g. '?foo=bar&baz=quux'
            baseurl = self.url.split("?")[0]
            try:
                params = "?%s" % self.url.split("?")[1]
            except:
                params = ""
            if settings.DEBUG_TO_CONSOLE == True:
                self.process = subprocess.Popen(["%s/xbmcWrapper.py" % settings.KODINO_FOLDER , self.addon.id, executable, baseurl, self.handle, params],env = my_env)
            else:
                FNULL = open(os.devnull, 'w')
                self.process = subprocess.Popen(["%s/xbmcWrapper.py" % settings.KODINO_FOLDER , self.addon.id, executable, baseurl, self.handle, params],env = my_env,  stdout=FNULL, stderr=subprocess.STDOUT)
            self.process.communicate()
            tmphome = "%s/home/tmp_%s"  % (settings.SPECIAL_FOLDER , self.handle )
            #defaulthome = "%s/home/default"  % (settings.SPECIAL_FOLDER ) # todo: automatically copy non critical files (for example NOT cache/search.sqlite) back to default user profile
            # may be need to support for example kahn academy plugin, it downloads a 10 mb file on first start that we may want to cache automatically
            #if os.path.exists(tmphome):
            #    for path, subdirs, files in os.walk(tmphome):
            #        for name in files:
            #            fullpath = os.path.join(path, name)
            #            subp = path.replace(tmphome,"")
            #            dsubp = "%s/%s" % (defaulthome, subp)
            #            print(fullpath, subp, dsubp)
                        
            try:
                shutil.rmtree(tmphome)
            except:
                pass
        thread = threading.Thread(target=target)
        thread.start()            
        thread.join(settings.TIMEOUT_XBMCWRAPPER)
        if thread.is_alive():
            print('Terminating wrapper after timeout!')
            self.process.terminate()
            thread.join()
        redis_key = "%s:%s" % (self.addon.id, self.handle)
        itemstrings = redis_connection.lrange( redis_key, 0, -1 )
        try:
            redis_connection.rename(redis_key, self.cache_key)
            if self.isFolder == True:
                redis_connection.expire(self.cache_key, settings.CACHETIME_FOLDER)
            else:
                redis_connection.expire(self.cache_key, settings.CACHETIME_NOFOLDER)
        except:
            None
        #print("wrapper exiting, return %s itemsstring" % len(itemstrings))
        return itemstrings
 
    def _subprocess(self, command, timeout):
        data = {
            "process" : None,
            "result" : "",
        }
        def target(command):
            my_env = os.environ.copy()
            my_env["PYTHONIOENCODING"] = "UTF-8"
            FNULL = open(os.devnull, 'w')
            if settings.DEBUG_TO_CONSOLE == True:
                data["process"] = subprocess.Popen(command, env = my_env , stdout=subprocess.PIPE)
            else:
                data["process"] = subprocess.Popen(command, env = my_env, stdout=subprocess.PIPE, stderr=FNULL)
            
            
            data["result"]  = data["process"].communicate()[0]
        thread = threading.Thread(target=target,args=[command,])
        thread.start()            
        thread.join(timeout)
        if thread.is_alive():
            print('Terminating wrapper after timeout!')
            data["process"].terminate()
            thread.join()
        return data["result"]
 
    def toDict(self):
        return {
            "addon" : self.addon.id,
            "url" : self.url,
            "title" : self.title,
            "hash" : self.hash,            
            "thumbnailImage" : self.thumbnailImage,            
            "isFile" : not self.isFolder,
            "isFolder" : self.isFolder,
            "requireKeyboard" : self.requireKeyboard,
            "keyboardInput" : self.keyboardInput,
            "path" : self.getPath(),
            "isAdult" : self.isAdult, # this is not automagically here, to mark addons as adult, add them to settings.py! 
        }

    def __repr__(self):
        return 'KodinoItem(title= %s, isFolder= %s, requireKeyboard= %s)' % (self.title.encode("UTF-8"),self.isFolder, self.requireKeyboard)
        