#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
sys.dont_write_bytecode = True
import os
import json
import redis
import traceback
import StringIO
import shutil
import atexit

from lib import xbmcplugin
from lib import xbmcgui
from lib import xbmcaddon
from lib import xbmcvfs
from lib import xbmc

import settings
import xbmcWrapperCommon

# to work arround "sys.stderr.__class__ = replacement_stderr" in YoutubeDLWrapper.py and others
class Stderr(StringIO.StringIO):
    def __init__(self,stderr):
        self.__stderr =  stderr
        self.closed = False
    def write(self,s):
        self.__stderr.write(s)
def exit(value): #prevent exists of wrapper by addon 
    raise Exception("Exit called")
    
sys.stderr = Stderr(sys.stderr)
     
print("Wrapper called with: %s" % sys.argv)

sys.path.append("%s/%s/" % (settings.PLUGINS_FOLDER, xbmcWrapperCommon.CURRENT_PLUGIN))
sys.path.append("%s/" % (settings.KODINO_FOLDER))
sys.path.append("%s/" % (settings.LIBRARY_FOLDER))
execfile("%s/autoloader.py" % settings.PLUGINS_FOLDER)
try:
    execfile("%s/%s/%s" % (settings.PLUGINS_FOLDER, xbmcWrapperCommon.CURRENT_PLUGIN, xbmcWrapperCommon.EXECUTABLE))
except Exception as e:
    traceback.print_exc()
    print("Wrapper failed: %s" % e)
    


