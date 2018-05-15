import sys
import settings

# kodi expects argv:
#0	The base URL of your add-on, e.g. 'plugin://plugin.video.demo1/foobar/'
#1	The process handle for this add-on, as a numeric string
#2	The query string passed to your add-on, e.g. '?foo=bar&baz=quux'

# our argv:
#0  wrapper.py
#1  plugin id eg plugin.video.demo1
#2  executable, for example default.py
#3	The base URL of your add-on, e.g. 'plugin://plugin.video.demo1/'
#4	The process handle for this add-on, as a numeric string
#5	The query string passed to your add-on, e.g. '?foo=bar&baz=quux'

CURRENT_PLUGIN = sys.argv[1]
CURRENT_HANDLE = sys.argv[4]
CURRENT_QUEUE = "%s:%s" % (CURRENT_PLUGIN, CURRENT_HANDLE)
HOME_FOLDER = "%s/home/tmp_%s"  % ( settings.SPECIAL_FOLDER, CURRENT_HANDLE ) 

EXECUTABLE = sys.argv[2]

# make our argv to kodi argv
del sys.argv[0] # remove wrapper
del sys.argv[0] # plugin id
del sys.argv[0] # remove executable

