#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
sys.dont_write_bytecode = True
import json, os, glob
import hashlib

from kodinoPlugins import KodinoPlugins
from kodinoItem import KodinoItem
import settings
   
   
class Kodino():
    def __init__(self, username = "default"):
        self.username = username
        self.title = ""
        self.hash = hashlib.sha256("KodinoRoot".encode("UTF-8")).hexdigest()[0:16]
        self.path = [ self.hash, self.title ]
        self.isFolder = True
        self.requireKeyboard = False
        self.plugins = KodinoPlugins()
        self.rootItems = []
        self.parent = None
        self.videoAddons = [va for va in self.plugins.getInstalledByProvides("video") if va.getExtentionsByPoint("xbmc.python.pluginsource") != [] and va.id not in settings.HIDDEN_PLUGINS]
        for videoAddon in self.videoAddons:
            kodiItem = KodinoItem( videoAddon, "plugin://%s/?" % videoAddon.id, videoAddon.name, True, "%s/%s/icon.png" % (settings.PLUGINS_FOLDER,videoAddon.id ), False, self )
            self.rootItems.append(kodiItem)
        self.rootItems.sort(key=lambda x: x.title)
        self.isAdult = False
            
    def getSubItems(self):
        return self.rootItems
        
    def getPath(self):
        return [[self.hash, ""],]
    
    def resolveHashPath(self, path): # path = list of title names, is item in tree is search next i ssearchstring ["videodevil","youtube","search", "search for this thing"]  
        #path = list of [hash:stringvalue]
        path = path[1:] # we are already root
        item = self
        items = item.getSubItems()
        #resolved_path_items = []
        index = 0
        resultitem = item
        resultitems = items
        #print("resolvePath %s" % path)
        while index < len(path):
            try:
                item  = [i for i in items if i.hash == path[index][0]][0]
            except Exception as e:
                print("Exception in resolveHashPath by hash for path %s" % path)
                try:
                    item = [i for i in items if i.title == path[index][1]][0]
                except Exception as e:
                    print("Exception in resolveHashPath by title for path %s" % path)
                    break
                break
            if item.requireKeyboard == True:
                print("requireKeyboard !!")
                try:
                    searchString = path[index+1][1]
                except:
                    print("break")
                    break  
                index += 1
                items = item.getSubItems(searchString)
                #resolved_path_items.append(item)
                resultitem = item
                resultitems = items
            elif item.isFolder == True:
                print("isfolder")
                #resolved_path_items.append(item)
                items = item.getSubItems()                    
                resultitem = item
                resultitems = items
            elif item.isFolder == False:    
                print("isfile")
                #resolved_path_items.append(item)
                items = []
                resultitem = item
                resultitems = items
                break
            else:
                print("NOTHING?")
            index += 1
        return resultitem, resultitems
        
    def toDict(self):
        return {
            "addon" : "root",
            "url" : "",
            "title" : "",
            "isFolder" : True,
            "parent" : "",
            "itemData" : None,
            "thumbnailImage" : "",
            "path" : [[self.hash,self.title]],
            "isAdult": False 

        }        
        
        
if __name__ == "__main__":
    kodino = Kodino()  
    from IPython import embed
    embed()
