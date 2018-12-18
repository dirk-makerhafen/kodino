import os
import redis

DEBUG_TO_CONSOLE = False

KODINO_FOLDER =  os.path.abspath(os.path.dirname(os.path.abspath(__file__)) )
PLUGINS_FOLDER =  os.path.abspath(KODINO_FOLDER + "/plugins" )
LIBRARY_FOLDER =  os.path.abspath(KODINO_FOLDER + "/lib" )
SPECIAL_FOLDER =  os.path.abspath(KODINO_FOLDER + "/special" )
DEFAULT_HOME_FOLDER = "%s/home/default"  % ( SPECIAL_FOLDER ) 

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
   
