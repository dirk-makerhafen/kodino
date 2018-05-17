import os
import redis

DEBUG_TO_CONSOLE = False

KODINO_FOLDER =  os.path.abspath(os.path.dirname(os.path.abspath(__file__)) )
PLUGINS_FOLDER =  os.path.abspath(KODINO_FOLDER + "/plugins" )
LIBRARY_FOLDER =  os.path.abspath(KODINO_FOLDER + "/lib" )
SPECIAL_FOLDER =  os.path.abspath(KODINO_FOLDER + "/special" )
DEFAULT_HOME_FOLDER = "%s/home/default"  % ( SPECIAL_FOLDER ) 

# if multiple user use this, like in the TV app, disable single instance or caching,
# addons may store for example last searches in HOME/addon_data/<addon_id>/..
# if all users share the same cache, or the same home they may see each others seaches, which may not be desired. 
# if you disable single instance, a new temporary home folder will be created from the default home folder on wrapper call and deleted afterwards. 
# Hint: some plugins download something large on first start, like the KahnAcademy plugin, it downloads a 10 MB functions file. 
# If you disable single instance you might want to put this file into the default home so it does not get downloaded on every addon call. 
SINGLE_INSTANCE = False

CACHE_DISABLED = False
CACHETIME_FOLDER      = 3600 * 6 
CACHETIME_NOFOLDER    = 3600     # video items, their cachetime should be short because playback urls are often not valid for very long
CACHETIME_DURATION    = 3600 * 6
CACHETIME_STATS       = 3600 * 24 * 14

TIMEOUT_XBMCWRAPPER  = 15
TIMEOUT_GETDURATION  = 15

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB   = 4  

ADULT_PLUGINS = [
    "metadata.movie.adultdvdempire.com",
    "metadata.movie.aebn.net",
    "metadata.movie.cduniverse.com",
    "metadata.movie.data18.com",
    "metadata.movie.data18.content.com",
    "metadata.movie.excaliburfilms.com",
    "plugin.video.aob",
    "plugin.video.empflix",
    "plugin.video.fantasticc",
    "plugin.video.lubetube",
    "plugin.video.tube8",
    "plugin.video.videodevil",
    "plugin.video.you.jizz",
    "repository.xbmcadult",
    "script.module.urlresolver.xxx",
    "metadata.movie.aebn.gay.net",
    "metadata.movie.hotmovies.com",
    "plugin.video.adultswim",
    "plugin.video.aswim",
    "plugin.video.filmfree4uER",
    "plugin.video.uwc",
    "plugin.video.xhamstergay",
    "plugin.video.youporngay",
]

HIDDEN_PLUGINS = [
    "plugin.program.indigo",
    "plugin.video.gdrive",
    "plugin.video.f4mTester",
]   
   