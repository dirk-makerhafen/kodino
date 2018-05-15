# -*- coding: UTF-8 -*-
import json
import inspect
import os
import redis
import sys
import polib
import traceback
import shutil

from xbmc_Constants import *
from xbmc_InfoTagMusic import *
from xbmc_InfoTagRadioRDS import *
from xbmc_InfoTagVideo import *
from xbmc_Keyboard import *
from xbmc_Monitor import *
from xbmc_Player import *
from xbmc_PlayList import *
from xbmc_RenderCapture import *
import CommonFunctions 

import settings
import xbmcWrapperCommon

XBMC_PLUGIN_FOLDER = settings.PLUGINS_FOLDER

redis_connection = redis.StrictRedis(host=settings.REDIS_HOST, port= settings.REDIS_PORT,db= settings.REDIS_DB)


translation_map = CommonFunctions.loadTranslationsMap(xbmcWrapperCommon.CURRENT_PLUGIN) 

abortRequested = False

def log(msg, level=LOGDEBUG):
    # type: (str, int) -> None
    """
    Write a string to Kodi's log file and the debug window. 

    :param msg: string - text to output. 
    :param level: [opt] integer - log level to ouput at. (default=LOGDEBUG)

    ================  ==========================================================
    Value:            Description:                                                                                                                                      
    ================  ==========================================================
    xbmc.LOGDEBUG     In depth information about the status of Kodi. This
                      information can pretty much only be deciphered by
                      a developer or long time Kodi power user.
    xbmc.LOGINFO      Something has happened. It's not a problem, we just
                      thought you might want to know. Fairly excessive output
                      that most people won't care about.
    xbmc.LOGNOTICE    Similar to INFO but the average Joe might want to know
                      about these events. This level and above are logged by default.
    xbmc.LOGWARNING   Something potentially bad has happened. If Kodi did
                      something you didn't expect, this is probably why.
                      Watch for errors to follow.
    xbmc.LOGERROR     This event is bad. Something has failed. You likely
                      noticed problems with the application be it skin artifacts,
                      failure of playback a crash, etc.
    xbmc.LOGFATAL     We're screwed. Kodi is about to crash.                                                                                                            
    ================  ==========================================================

    You can use the above as keywords for arguments and skip certain optional
    arguments. Once you use a keyword, all following arguments
    require the keyword.

    Text is written to the log for the following conditions:

    loglevel == -1 (NONE, nothing at all is logged)

    loglevel == 0 (NORMAL, shows LOGNOTICE, LOGERROR, LOGSEVERE and LOGFATAL)

    loglevel == 1 (DEBUG, shows all) See pydocs for valid values for level.

    Default level changed from LOGNOTICE to LOGDEBUG

    Example::

        ..
        xbmc.log(msg='This is a test string.', level=xbmc.LOGDEBUG);
        ..
    """
    print("xmbc.log('%s')" % msg)


def shutdown():
    # type: () -> None
    """
    Shutdown the htpc. 

    Example::

        ..
        xbmc.shutdown()
        ..
    """
    pass


def restart():
    # type: () -> None
    """
    Restart the htpc. 

    Example::

        ..
        xbmc.restart()
        ..
    """
    pass


def executescript(script):
    # type: (str) -> None
    """
    Execute a python script. 

    :param script: string - script filename to execute.

    Example::

        ..
        xbmc.executescript('special://home/scripts/update.py')
        ..
    """
    pass


def executebuiltin(function, wait=False):
    # type: (str, bool) -> None
    """
    Execute a built in Kodi function. 

    :param function: string - builtin function to execute.

    List of functions - <http://kodi.wiki/view/List_of_Built_In_Functions>

    Example::

        ..
        xbmc.executebuiltin('RunXBE(c:\\avalaunch.xbe)')
        ..
    """
    redis_connection.rpush(xbmcWrapperCommon.CURRENT_QUEUE, json.dumps({"key": "xbmc:executebuiltin" , "function" : function}))    
  

def executeJSONRPC(jsonrpccommand):
    # type: (str) -> str
    """
    Execute an JSONRPC command. 

    :param jsonrpccommand: string - jsonrpc command to execute. 
    :return: jsonrpc return string

    Example::

        ..
        response = xbmc.executeJSONRPC('{ "jsonrpc": "2.0", "method": "JSONRPC.Introspect", "id": 1 }')
        ..
    """
    json_rpc = json.loads(jsonrpccommand)
    method = json_rpc["method"]
    
    if method == "Application.GetProperties":
        result = {"result" : {}}
        result["result"]["version"] = 16
        result["result"]["name"] = "kodino"
        return json.dumps(result)
    if method == "Addons.GetAddonDetails":
        addonid = json_rpc["params"]["addonid"]
        if addonid.startswith("inputstream."):
            return json.dumps({"error":"not implemented"})
        
    return "{}"

sleepUsageCount = 0        
def sleep(timemillis):
    # type: (int_type) -> None
    """
    Sleeps for 'time' msec. 

    :param time: integer - number of msec to sleep.
    :raises TypeError: If time is not an integer.

    This is useful if you have for example a Player class that is waiting
    for onPlayBackEnded() calls.

    Example::

        ..
        xbmc.sleep(2000) # sleeps for 2 seconds
        ..
    """
    global sleepUsageCount
    sleepUsageCount += 1
    if sleepUsageCount > 50:
        raise Exception("sleep loop interrupted")
    if timemillis > 900: #  most likely because of some error
        print("Sleep detected '%s'" % timemillis)
        

def getLocalizedString(id):
    print("xbmc.py getLocalizedString('%s')" % id)
    # type: (int) -> unicode
    """
    Get a localized 'unicode string'. 

    :param id: integer - id# for string you want to localize. 
    :return: Localized 'unicode string'

    See strings.po in  ``\language\{yourlanguage}\`` for which id you need
    for a string.

    Example::

        ..
        locstr = xbmc.getLocalizedString(6)
        ..
    """
    if id in translation_map:
        r = translation_map[id]
        return r
    return "No String Found"


def getSkinDir():
    # type: () -> str
    """
    Get the active skin directory. 

    :return: The active skin directory as a string

    This is not the full path like ``'special://home/addons/MediaCenter'``,
    but only ``'MediaCenter'``.

    Example::

        ..
        skindir = xbmc.getSkinDir()
        ..
    """
    return ""


def getLanguage(format=ENGLISH_NAME, region=False):
    # type: (int, bool) -> str
    """
    Get the active language. 

    :param format: [opt] format of the returned language string

    ==================  ========================================================
    Value               Description                                                
    ==================  ========================================================
    xbmc.ISO_639_1      Two letter code as defined in ISO 639-1                    
    xbmc.ISO_639_2      Three letter code as defined in ISO 639-2/T
                        or ISO 639-2/B
    xbmc.ENGLISH_NAME   Full language name in English (default)                    
    ==================  ========================================================

    :param region: [opt] append the region delimited by "-" of the language
        (setting) to the returned language string
    :return: The active language as a string

    Added new options **format** and **region**.

    Example::

        ..
        language = xbmc.getLanguage(xbmc.ENGLISH_NAME)
        ..
    """
    return ""


def getIPAddress():
    # type: () -> str
    """
    Get the current ip address. 

    :return: The current ip address as a string

    Example::

        ..
        ip = xbmc.getIPAddress()
        ..
    """
    return ""


def getDVDState():
    # type: () -> long
    """
    Returns the dvd state as an integer. 

    :return: Values for state are:

    ======  ===============================
    Value   Name                           
    ======  ===============================
    1       xbmc.DRIVE_NOT_READY           
    16      xbmc.TRAY_OPEN                 
    64      xbmc.TRAY_CLOSED_NO_MEDIA      
    96      xbmc.TRAY_CLOSED_MEDIA_PRESENT 
    ======  ===============================

    Example::

        ..
        dvdstate = xbmc.getDVDState()
        ..
    """
    return 0L


def getFreeMem():
    # type: () -> long
    """
    Get amount of free memory in MB. 

    :return: The amount of free memory in MB as an integer

    Example::

        ..
        freemem = xbmc.getFreeMem()
        ..
    """
    return 0L


def getInfoLabel(cLine):
    # type: (str) -> str
    """
    Get a info label 

    :param infotag: string - infoTag for value you want returned. 
    :return: InfoLabel as a string

    List of InfoTags -- <http://kodi.wiki/view/InfoLabels>

    Example::

        ..
        label = xbmc.getInfoLabel('Weather.Conditions')
        ..
    """
    if cLine == "System.BuildVersion":
        return "23.42"
    if cLine == 'Playlist.Length(video)':
        if playlistInstance != None:
            return len(playlistInstance.items)
        return 0
    return ""


def getInfoImage(infotag):
    # type: (str) -> str
    """
    Get filename including path to the InfoImage's thumbnail. 

    :param infotag: string - infotag for value you want returned 
    :return: Filename including path to the InfoImage's thumbnail as a string

    List of InfoTags -- <http://kodi.wiki/view/InfoLabels>

    Example::

        ..
        filename = xbmc.getInfoImage('Weather.Conditions')
        ..
    """
    return ""


def playSFX(filename, useCached=True):
    # type: (str, bool) -> None
    """
    Plays a wav file by filename 

    :param filename: string - filename of the wav file to play 
    :param useCached: [opt] bool - False = Dump any previously cached wav
        associated with filename

    Added new option **useCached**.

    Example::

        ..
        xbmc.playSFX('special://xbmc/scripts/dingdong.wav')
        xbmc.playSFX('special://xbmc/scripts/dingdong.wav',False)
        ..
    """
    pass


def stopSFX():
    # type: () -> None
    """
    Stops wav file 

      New function added.

    Example::

        ..
        xbmc.stopSFX()
        ..
    """
    pass


def enableNavSounds(yesNo):
    # type: (bool) -> None
    """
    Enables/Disables nav sounds 

    :param yesNo: integer - enable (True) or disable (False) nav sounds

    Example::

        ..
        xbmc.enableNavSounds(True)
        ..
    """
    pass


def getCondVisibility(condition):
    # type: (str) -> bool
    """
    Get visibility conditions 

    :param condition: string - condition to check 
    :return: True (1) or False (0) as a bool

    List of Conditions -- <http://kodi.wiki/view/List_of_Boolean_Conditions>

    You can combine two (or more) of the above settings by using **"+"**
    as an AND operator, **"|"** as an OR operator, **"!"** as a NOT operator,
    and **"["** and **"]"** to bracket expressions.

    Example::

        ..
        visible = xbmc.getCondVisibility('[Control.IsVisible(41) + !Control.IsVisible(12)]')
        ..
    """
    return True


def getGlobalIdleTime():
    # type: () -> int
    """
    Get the elapsed idle time in seconds. 

    :return: Elapsed idle time in seconds as an integer

    Example::

        ..
        t = xbmc.getGlobalIdleTime()
        ..
    """
    return 0


def getCacheThumbName(path):
    # type: (str_type) -> str
    """
    Get thumb cache filename. 

    :param path: string or unicode - path to file 
    :return: Thumb cache filename

    Example::

        ..
        thumb = xbmc.getCacheThumbName('f:\\videos\\movie.avi')
        ..
    """
    return ""


def makeLegalFilename(filename, fatX=True):
    # type: (str_type, bool) -> str
    """
    Returns a legal filename or path as a string. 

    :param filename: string or unicode - filename/path to make legal
    :param fatX: [opt] bool - True=Xbox file system(Default)
    :return: Legal filename or path as a string

    If fatX is true you should pass a full path. If fatX is false only pass
    the basename of the path. You can use the above as keywords for arguments
    and skip certain optional arguments. Once you use a keyword, all following
    arguments require the keyword.

    Example::

        ..
        filename = xbmc.makeLegalFilename('F:\\Trailers\\Ice Age: The Meltdown.avi')
        ..
    """
    return ""


def translatePath(path):
    # type: (str_type) -> str
    """
    Returns the translated path. 

    :param path: string or unicode - Path to format 
    :return: Translated path

    Only useful if you are coding for both Linux and Windows.
    e.g. Converts ``'special://masterprofile/script_data'`` ->
    ``'/home/user/XBMC/UserData/script_data'`` on Linux.

    Example::

        ..
        fpath = xbmc.translatePath('special://masterprofile/script_data')
        ..
    """
    opath = path
    opath = opath.replace("special://home/addons", settings.PLUGINS_FOLDER) # we install plugins globally 
	
    # from https://kodi.wiki/view/Special_protocol
    opath = opath.replace("special://logpath"       , "%s/logs"  % settings.SPECIAL_FOLDER ) # This path points to the path where the log file is saved.
    opath = opath.replace("special://skin"          , "%s/other" % settings.SPECIAL_FOLDER ) # This path points to the currently active skin's root directory.
    opath = opath.replace("special://cdrips"        , "%s/other" % settings.SPECIAL_FOLDER ) # This path contains the tracks from CDs you rip with Kodi. You will be asked to specify this directory the first time you rip a CD.
    opath = opath.replace("special://videoplaylists", "%s/other" % settings.SPECIAL_FOLDER ) # This path contains saved video playlists. Normally special://profile/playlists/video.
    opath = opath.replace("special://musicplaylists", "%s/other" % settings.SPECIAL_FOLDER ) # This path contains saved music playlists. Normally special://profile/playlists/music.
    opath = opath.replace("special://screenshots"   , "%s/other" % settings.SPECIAL_FOLDER ) # This path contains Kodi screen shots. You will be asked to specify this directory the first time you take a screen shot.
    opath = opath.replace("special://recordings"    , "%s/other" % settings.SPECIAL_FOLDER ) # This path contains saved PVR recordings.
    opath = opath.replace("special://thumbnails"    , "special://masterprofile/Thumbnails"     ) # This path contains cached thumbnails. Normally special://masterprofile/Thumbnails
    opath = opath.replace("special://database"      , "special://masterprofile/Database"       ) # This path contains the database files Kodi uses to store library info. Normally special://masterprofile/Database.
    opath = opath.replace("special://userdata"      , "special://masterprofile"                ) # Alias from special://masterprofile.
    opath = opath.replace("special://subtitles"     , "%s/other" % settings.SPECIAL_FOLDER ) # User defined custom subtitle path. Set it in Video Settings.
    opath = opath.replace("special://profile"       , "special://masterprofile"                ) # Kodi's currently active profile directory. This directory points at special://masterprofile/profile_name (or special://masterprofile if no profile is in use) and contains per profile overrides for settings and sources.
    opath = opath.replace("special://masterprofile" , "special://home/userdata"                ) # Kodi's main configuration directory. Normally located at special://home/userdata, this directory contains global settings and sources, as well as any Kodi profile directories. Normally special://home/userdata
    opath = opath.replace("special://temp"          , "special://home/temp"                    ) # Kodi's temporary directory. This path is used to cache various data during normal usage. Unless you need the log, nothing in this directory is detrimental to Kodi's operation. Normally special://home/temp
        
    if settings.SINGLE_INSTANCE:
        opath = opath.replace("special://home"          , settings.DEFAULT_HOME_FOLDER) # Kodi's user specific (Web interface user) configuration directory. 
    else:
        # create temporary home folder, delete after run (BY CALLER of wrapper.py!)  to prevent for example search string caching by plugins. 
        if opath.startswith("special://home"):
            opath_default = opath.replace("special://home"  , settings.DEFAULT_HOME_FOLDER) # Kodi's user specific (Web interface user) configuration directory. 
            opath_instance = opath.replace("special://home" , xbmcWrapperCommon.HOME_FOLDER) # Kodi's user specific (Web interface user) configuration directory. 
            if not os.path.exists(opath_instance):
                if os.path.exists(opath_default):
                    shutil.copytree(opath_default, opath_instance)            
                    print("copying default settings")
                else:
                    print("Creating home path %s" % opath_instance)
                    os.makedirs(opath_instance)
                    
            opath = opath_instance
            
    opath = opath.replace("special://kodi"          , "special://xbmc"                         ) # does not exist yet.
    opath = opath.replace("special://xbmc"          , "%s/xbmc" % settings.SPECIAL_FOLDER  ) # Kodi's installation root directory. This path is read-only contains the Kodi binary, support libraries and default configuration files, skins, scripts and plugins. Users should not modify files or install addons in this directory.
    
    if opath.startswith("special://"):
        raise Exception("must return clean path: %s" % opath)
        
    print("xbmc.py translatePath('%s') -> '%s'" % (path, opath))
    
    return opath


def getCleanMovieTitle(path, usefoldername=False):
    # type: (str_type, bool) -> Tuple[str, str]
    """
    Get clean movie title and year string if available. 

    :param path: string or unicode - String to clean 
    :param usefoldername: [opt] bool - use folder names (defaults to false) 
    :return: Clean movie title and year string if available.

    Example::

        ..
        title, year = xbmc.getCleanMovieTitle('/path/to/moviefolder/test.avi', True)
        ..
    """
    return "", ""


def validatePath(path):
    # type: (str_type) -> str
    """
    Returns the validated path. 

    :param path: string or unicode - Path to format 
    :return: Validated path

    Only useful if you are coding for both Linux and Windows for fixing slash
    problems. e.g. Corrects ``'Z://something'`` -> ``'Z:'``

    Example::

        ..
        fpath = xbmc.validatePath(somepath)
        ..
    """
    return ""


def getRegion(id):
    # type: (str) -> str
    """
    Returns your regions setting as a string for the specified id. 

    :param id: string - id of setting to return 
    :return: Region setting

    choices are (dateshort, datelong, time, meridiem, tempunit, speedunit)
    You can use the above as keywords for arguments.

    Example::

        ..
        date_long_format = xbmc.getRegion('datelong')
        ..
    """
    return ""


def getSupportedMedia(mediaType):
    # type: (str) -> str
    """
    Get the supported file types for the specific media. 

    :param media: string - media type 
    :return: Supported file types for the specific media as a string

    Media type can be (video, music, picture). The return value is a pipe
    separated string of filetypes (eg. '.mov|.avi'). You can use the above
    as keywords for arguments.

    Example::

        ..
        mTypes = xbmc.getSupportedMedia('video')
        ..
    """
    return ""


def skinHasImage(image):
    # type: (str) -> bool
    """
    Check skin for presence of Image. 

    :param image: string - image filename 
    :return: True if the image file exists in the skin

    If the media resides in a subfolder include it.
    (eg. ``home-myfiles\home-myfiles2.png``).
    You can use the above as keywords for arguments.

    Example::

        ..
        exists = xbmc.skinHasImage('ButtonFocusedTexture.png')
        ..
    """
    return True


def startServer(iTyp, bStart, bWait=False):
    # type: (int, bool, bool) -> bool
    """
    Start or stop a server. 

    :param typ: integer - use SERVER_* constantsUsed format of the returned
        language string

    ==========================  ================================================
    Value                       Description                                                           
    ==========================  ================================================
    xbmc.SERVER_WEBSERVER       To control Kodi's builtin webserver                                     
    xbmc.SERVER_AIRPLAYSERVER   AirPlay is a proprietary protocol stack/suite
                                developed by Apple Inc.
    xbmc.SERVER_JSONRPCSERVER   Control JSON-RPC HTTP/TCP socket-based interface                        
    xbmc.SERVER_UPNPRENDERER    UPnP client (aka UPnP renderer)                                         
    xbmc.SERVER_UPNPSERVER      Control built-in UPnP A/V media server
                                (UPnP-server)
    xbmc.SERVER_EVENTSERVER     Set eventServer part that accepts remote device
                                input on all platforms
    xbmc.SERVER_ZEROCONF        Control Kodi's Avahi Zeroconf                                           
    ==========================  ================================================

    :param bStart: bool - start (True) or stop (False) a server 
    :param bWait: [opt] bool - wait on stop before returning
        (not supported by all servers)
    :return: bool - True or False

    Example::

        ..
        xbmc.startServer(xbmc.SERVER_AIRPLAYSERVER, False)
        ..
    """
    return True


def audioSuspend():
    # type: () -> None
    """
    Suspend Audio engine. 

    Example::

        ..
        xbmc.audioSuspend()
        ..
    """
    pass


def audioResume():
    # type: () -> None
    """
    Resume Audio engine. 

    Example::

        ..
        xbmc.audioResume()
        ..
    """
    pass


def getUserAgent():
    # type: () -> str
    """
    Returns Kodi's HTTP UserAgent string

    :return: HTTP user agent

    Example::

        ..
        xbmc.getUserAgent()
        ..

    example output:
    ``Kodi/17.0-ALPHA1 (X11; Linux x86_64) Ubuntu/15.10 App_Bitness/64 Version/17.0-ALPHA1-Git:2015-12-23-5770d28``
    """
    return ""


def convertLanguage(language, format):
    # type: (str, int) -> str
    """
    Returns the given language converted to the given format as a string.

    :param language: string either as name in English, two letter code
        (ISO 639-1), or three letter code (ISO 639-2/T(B)
    :param format: format of the returned language string

    ==================  ========================================================
    Value               Description                                                
    ==================  ========================================================
    xbmc.ISO_639_1      Two letter code as defined in ISO 639-1                    
    xbmc.ISO_639_2      Three letter code as defined in ISO 639-2/T
                        or ISO 639-2/B
    xbmc.ENGLISH_NAME   Full language name in English (default)                    
    ==================  ========================================================

    :return: Converted Language string

    New function added.

    Example::

        ..
        language = xbmc.convertLanguage(English, xbmc.ISO_639_2)
        ..
    """
    return ""




