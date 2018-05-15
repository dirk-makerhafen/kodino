# -*- coding: utf-8 -*-
import json
import xbmc
import inspect
import redis
import sys
import os
import sys
import polib
import xml.etree.ElementTree
from bs4 import BeautifulSoup

import settings
import xbmcWrapperCommon
import CommonFunctions

addonxml_cache = {}
settingxml_cache = {}

redis_connection = redis.StrictRedis(host=settings.REDIS_HOST, port= settings.REDIS_PORT,db= settings.REDIS_DB)


class Addon(object):
    """
    Kodi's addon class

    Offers classes and functions that manipulate the add-on settings,
    information and localization.

    Creates a new AddOn class.

    :param id: [opt] string - id of the addon as specified in addon.xml

    Specifying the addon id is not needed. Important however is that the addon
    folder has the same name as the AddOn id provided in addon.xml.
    You can optionally specify the addon id from another installed addon
    to retrieve settings from it.

    **id** is optional as it will be auto detected for this add-on instance.

    Example::

        ..
        self.Addon = xbmcaddon.Addon()
        self.Addon = xbmcaddon.Addon('script.foo.bar')
        ..
    """
    
    def __init__(self, id=xbmcWrapperCommon.CURRENT_PLUGIN):
        # type: (str) -> None
        self.id = id
        self.addonxml = None
        self.settingsxml = None
        self.localsettings = {} # local settings set by addons
        if id not in addonxml_cache:
            try:
                addonxml_cache[id] = xml.etree.ElementTree.fromstring(open("%s/%s/addon.xml" % (xbmc.XBMC_PLUGIN_FOLDER, self.id),"rb").read())
            except Exception as e:
                print(("xbmcaddon '%s' failed to load addon.xml %s" % (self.id,e)))
                addonxml_cache[id] = None
        self.addonxml = addonxml_cache[id]
            
        if id not in settingxml_cache:
            try:
                content = open("%s/%s/resources/settings.xml" % (xbmc.XBMC_PLUGIN_FOLDER,self.id),"rb").read()
                settingxml_cache[id] = BeautifulSoup(content, 'html.parser')
            except Exception as e:
                print(("xbmcaddon '%s' failed to load settings.xml %s" % (self.id,e)))
                settingxml_cache[id] = None
        self.settingsxml = settingxml_cache[id]
        
        self.translation_map = CommonFunctions.loadTranslationsMap(self.id) 
        
    
    def getLocalizedString(self, id):
        print("xbmcaddon.py getLocalizedString('%s')" % id)

        # type: (int) -> unicode
        """
        Returns an addon's localized 'unicode string'. 

        :param id: integer - id# for string you want to localize. 
        :return: Localized 'unicode string'

        **id** is optional as it will be auto detected for this add-on instance.

        Example::

            ..
            locstr = self.Addon.getLocalizedString(32000)
            ..
        """
        if id in self.translation_map:
            r = self.translation_map[id]
            return r
        print(self.id)
        print("Not found")
        return "No String Found"
      
    
    def getSetting(self, id):
        # type: (str) -> str
        """
        Returns the value of a setting as a unicode string. 

        :param id: string - id of the setting that the module needs to access. 
        :return: Setting as a unicode string

        **id** is optional as it will be auto detected for this add-on instance.

        Example::

            ..
            apikey = self.Addon.getSetting('apikey')
            ..
        """
        if self.settingsxml != None:
            element = self.settingsxml.find("setting", {"id" : id})
            if element != None:
                try:
                    return element['value']
                except:
                    pass
                try:
                    return element['default']
                except:
                    pass
            
        if id in self.localsettings:
            return self.localsettings[id]
        else:
            print("%s has no setting %s" %( self.id, id))    
        return ""
    
    def setSetting(self, id, value):
        # type: (str, str_type) -> None
        """
        Sets a script setting. 

        :param id: string - id of the setting that the module needs to access. 
        :param value: string or unicode - value of the setting.

        You can use the above as keywords for arguments.

        Example::

            ..
            self.Addon.setSetting(id='username', value='teamkodi')
            ..
        """
        self.localsettings[id] = value

    
    def openSettings(self):
        # type: () -> None
        """
        Opens this scripts settings dialog. 

        Example::

            ..
            self.Addon.openSettings()
            ..
        """
        pass
    
    def getAddonInfo(self, id):
        # type: (str) -> str
        """
        Returns the value of an addon property as a string. 

        :param id: string - id of the property that the module needs to access.

        Choices for the property are:

        =======  ==========  ============  ===========
        author   changelog   description   disclaimer 
        fanart   icon        id            name       
        path     profile     stars         summary    
        type     version                              
        =======  ==========  ============  ===========

        :return: AddOn property as a string

        Example::

            ..
            version = self.Addon.getAddonInfo('version')
            ..
        """
        if self.addonxml != None:
            if id in self.addonxml.attrib:
                return self.addonxml.attrib[id]
            
        if id.lower() == "path":
            res =  "%s/%s" % (settings.PLUGINS_FOLDER, self.id)
            return res
            
        if id.lower() == "profile":            
            return "special://userdata/addon_data/%s" % (self.id)
            
        if id.lower() in ["author", "changelog", "description", "disclaimer", "fanart", "icon", "stars", "summary", "version"]:
            return ""
            
        return "dummy"   

     