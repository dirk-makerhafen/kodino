#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
sys.dont_write_bytecode = True
import json, os, glob, io 
import xml.etree.ElementTree
import time
from distutils.version import LooseVersion, StrictVersion

import settings

class KodinoPlugins():

    def __init__(self):
        self.installed = []
        self.repositorys = []
        self.lastupdate = 0
        self.reload()
        
    def getInstalledPlugins(self):
        self.reloadIfNeeded()
        return self.installed
        
    def getAvailablePlugins(self):
        self.reloadIfNeeded()
        result = []
        [result.extend(r.addons) for r in self.repositorys]
        return result
        

    def getLastUpdated(self):
        try:
            f = open("%s/autoloader.py" % settings.PLUGINS_FOLDER,"r")
            return int(f.read().split("#ts:")[1].split("\n")[0])
        except:
            return 0
            
    def reload(self):
        self.lastupdate = self.getLastUpdated() 
        self.reloadInstalled()
        self.reloadRepositorys()
        print("%s plugins installed" % len(self.installed))
        print("%s plugins available" % sum([len(r.addons) for r in self.repositorys]))
        
    def reloadIfNeeded(self):
        if self.getLastUpdated() != self.lastupdate:
            self.lastupdate = self.getLastUpdated() 
            self.reload()
            
    def reloadInstalled(self):    
        self.installed = []
        for d in glob.glob("%s/*/" %  settings.PLUGINS_FOLDER):
            filename = "%s/addon.xml" % d
            if not os.path.exists(filename):
                print("Folder '%s' has no addon.xml" % d)
                continue
            xmlelement = xml.etree.ElementTree.fromstring(open(filename,"rb").read())
            addon = Addon(None, xmlelement)
            self.installed.append(addon)
            
    def reloadRepositorys(self):
        self.repositorys = []
        addons = self.getInstalledByExtentionPoint("xbmc.addon.repository")
        for addon in addons:
            filename = "%s/%s/dl/addons.xml" % ( settings.PLUGINS_FOLDER, addon.id)
            if not os.path.exists(filename):
                print("Repository '%s' has no addons.xml file" % addon.id)
                continue
            xmlelement = xml.etree.ElementTree.fromstring(open(filename,"rb").read())    
            self.repositorys.append(RepositoryAddon(addon, xmlelement))
            
    def reloadAutoloader(self):
        addons = self.getInstalledByExtentionPoint("xbmc.python.module")
        f = open("%s/autoloader.py" %  settings.PLUGINS_FOLDER,"w")
        self.lastupdate = int(time.time())
        f.write("#ts:%s\n" % self.lastupdate)
        f.write("import sys\n")
        for addon in addons:
            extensions = addon.getExtentionsByPoint("xbmc.python.module")
            for extension in extensions:
                line = 'sys.path.append("%s/%s/%s/")' % ( settings.PLUGINS_FOLDER, addon.id, extension.library) 
                f.write("%s\n" % line)
        f.close()
       
    def install(self, addon_id, force = False, version = None, repository_id = None):#
    
        self.reloadIfNeeded()
        
        installable_addons = self.getInstallableById(addon_id)
        if len(installable_addons) == 0:
            print("Can not install addon '%s', not found" % addon_id)
            return 
            
        if len(installable_addons) == 1:
            installable_addon = installable_addons[0]
        else:
            if repository_id == None and version == None:
                newest = sorted([i.version for i in installable_addons], key=LooseVersion)[-1]
                #print("More than 1 source repository available for '%s', selecting newest '%s'" % (addon_id,newest))
                installable_addons = [i for i in installable_addons if i.version == newest ]                
                installable_addon = installable_addons[0]                
            else:
                if version != None:
                    installable_addons = [i for i in installable_addons if i.version == version ]
                if repository_id != None:
                    installable_addons = [i for i in installable_addons if i.parent.id == repository_id ]
            if len(installable_addons) == 0:
                print("No installable version found")
                return 
            installable_addon = installable_addons[0]        
        
        for requirement in installable_addon.requirements:
            if not requirement.addon_id.startswith("xbmc"):
                #print("Addon '%s' requires '%s':'%s'" % (addon_id, requirement.addon_id, requirement.version))                                
                self.install(requirement.addon_id, force)   
        
        installed_addon = self.getInstalledById(addon_id)
        if installed_addon != None and force == False:
            if installable_addon.version != "" and installed_addon.version != "":
                if LooseVersion(installed_addon.version) >= LooseVersion(installable_addon.version):
                    print("Installation of '%s' '%s' not needed, already exists in version '%s'" % (installable_addon.id, installable_addon.version, installed_addon.version ))
                    return 
        sourcerepo = installable_addon.parent 
        datadir = sourcerepo.getExtentionsByPoint("xbmc.addon.repository")[0].datadir
                  
        print("Need to install '%s' '%s'" % (installable_addon.id, installable_addon.version)) 
        filename = "%s-%s.zip" % ( installable_addon.id, installable_addon.version)
        url = ("%s/%s/%s" % (datadir, installable_addon.id, filename )).replace("'","")
        os.system("cd '%s/' && wget -q -c -N '%s' && unzip -o -u '%s' && rm '%s'" % ( settings.PLUGINS_FOLDER, url, filename, filename))
        self.reload()
        self.reloadAutoloader()
    
    def uninstall(self, addon_id):
        self.reloadIfNeeded()
        path = "%s/%s/" % ( settings.PLUGINS_FOLDER, addon_id)
        if os.path.isdir(path):
            os.system("rm -r '%s'" % path)
            print("'%s' removed" % path)
        else:
            print("'%s' not found " % path)
        self.reload()
        self.reloadAutoloader()            

    def upgrade(self, force = False):
        self.reloadIfNeeded()
        for installed in self.installed:
            self.install(installed.id, force)
            
    def update(self):
        self.reloadIfNeeded()
        for addon in self.getInstalledByExtentionPoint("xbmc.addon.repository"):
            for extension in addon.getExtentionsByPoint("xbmc.addon.repository"):
                print("Updating repository '%s'" % addon.id)
                cmd = "cd '%s/%s' ; mkdir dl 2>/dev/null ; cd dl ; rm addons.xml 2>/dev/null ; wget -q -c -N  '%s' " % ( settings.PLUGINS_FOLDER, addon.id, extension.info.replace("'",""))
                os.system(cmd)
                if extension.info.endswith(".gz"):
                    cmd = "cd '%s/%s/dl/' && gzip -d addons.xml.gz" % ( settings.PLUGINS_FOLDER, addon.id )
                    os.system(cmd)
                if extension.info.endswith(".zip"):
                    cmd = "cd '%s/%s/dl/' && unzip addons.xml.zip" %( settings.PLUGINS_FOLDER, addon.id )
                    os.system(cmd)
        self.reloadRepositorys()
        self.reloadAutoloader()            
        
    def getInstalledByExtentionPoint(self, extension_point):
        self.reloadIfNeeded()
        return [addon for addon in self.installed if len(addon.getExtentionsByPoint(extension_point)) != 0]
        
    def getInstalledByProvides(self, provides):
        self.reloadIfNeeded()
        return [addon for addon in self.installed if len(addon.getExtentionsByProvides(provides)) != 0]
          
    def getInstalledById(self, addon_id):
        self.reloadIfNeeded()
        r = [a for a in self.installed if a.id == addon_id]
        if r != []:
            return r[0]
        return None
        
    def getInstallableById(self, addon_id):
        self.reloadIfNeeded()
        result = []
        for repo in self.repositorys:
            result.extend( repo.getInstallableById(addon_id))
        return result
  

    def _isVersionLarger(self, a, b):
        return 
        aarray = [x for x in a.split(".")]
        barray = [x for x in b.split(".")]
        while len(aarray) < len(barray):    
            aarray.append(0)
        while len(barray) < len(aarray):    
            barray.append(0)
        for i in range(0,len(aarray)):
            if int(aarray[i]) > int(barray[i]):
                return True
        return False
      
        
def printHelp():
    print('''
        Usage: 
            kodinoPlugins.py update                # Download repositorys
            kodinoPlugins.py upgrade               # Download new addon version from repos
            kodinoPlugins.py installed <filter> # List all installed addons, optional filter by addon id starts with <filter>
            kodinoPlugins.py available <filter> # List all available addons, optional filter by addon id starts with <filter>
            kodinoPlugins.py install   <addon id>  # Install addon
            kodinoPlugins.py uninstall <addon id>  # Unistall addon
    ''')

def commandline():
    kodinoPlugins = KodinoPlugins()
    
    try:
        command = sys.argv[1]   
    except:
        printHelp()
        exit(1)
    if command == "update":
        kodinoPlugins.update()
    elif command == "upgrade":
        kodinoPlugins.upgrade()        
    elif command == "install":
        addon_id = sys.argv[2]
        try:
            version = sys.argv[3]
        except:
            version = None
        try:
            repository_id = sys.argv[4]
        except:
            repository_id = None
        kodinoPlugins.install(addon_id, version=version,repository_id= repository_id)
    elif command == "uninstall":
        addon_id = sys.argv[2]
        kodinoPlugins.uninstall(addon_id)        
    elif command == "installed":
        try:
            filter = sys.argv[2]
        except:
            filter = ""
        found = []
        for addon in kodinoPlugins.getInstalledPlugins():    
            if addon.id.startswith(filter):
                if addon.parent != None:
                    parentid = addon.parent.id
                else:
                    parentid = "No source"
                found.append("%s\t\t%s\t\t%s" % (addon.id, addon.version,parentid))
        print("\n".join(sorted(found)))
        print("%s plugins installed" % len(found))
    elif command == "available":
        try:
            filter = sys.argv[2]
        except:
            filter = ""
        found = []            
        for addon in kodinoPlugins.getAvailablePlugins():    
            if addon.id.startswith(filter):
                found.append("%s\t\t%s\t\t%s" % (addon.id, addon.version,addon.parent.id ))
        print("\n".join(sorted(found)))
        print("%s plugins available" % len(found))
    else:
        print("unknown command %s" % command)
        printHelp()
        exit(1)
  
class Requirement():
    def __init__(self, parent, xmlelement):
        self.parent = parent
        self.addon_id = xmlelement.attrib["addon"]
        self.version  = xmlelement.attrib["version"]  if "version"  in xmlelement else ""
        self.optional = xmlelement.attrib["optional"] if "optional" in xmlelement else False
        
class Extension():
    def __init__(self, parent, xmlelement):
        self.parent = parent
        self.descriptions = {}
        self.summarys = {}
        
        self.point    = xmlelement.attrib["point"]
        self.name     = xmlelement.attrib["name"]                   if "name"    in xmlelement.attrib else ""
        self.library  = xmlelement.attrib["library"]                if "library" in xmlelement.attrib else ""
        self.provides = xmlelement.find('provides').text.split(" ") if xmlelement.find('provides')       != None and xmlelement.find('provides').text != None else []
        
        _info = [x for x in xmlelement.iter('info')]
        _checkum = [x for x in xmlelement.iter('checksum')]
        _datadir = [x for x in xmlelement.iter('datadir')]

        self.info     = _info[0].text    if _info    != [] else ""
        self.checksum = _checkum[0].text if _checkum != [] else ""
        self.datadir  = _datadir[0].text if _datadir != [] else ""
        
        self.platform = xmlelement.find('platform').text            if xmlelement.find('platform')       != None else ""
        self.broken   = xmlelement.find('broken') != None

        for description in xmlelement.findall('description'):
            lang = description.attrib["lang"] if "lang" in description.attrib else "en"
            self.descriptions[lang] = description.text
        for summary in xmlelement.findall('summary'):
            lang = summary.attrib["lang"] if "lang" in summary.attrib else "en"
            self.summarys[lang] = summary.text
            
        self.summary = "no summary"
        self.description = "no description"
        for l in ["en","en_us", "en_GB"]:       
            if l in self.descriptions:
                self.description = self.descriptions[l]
                break
        for l in ["en","en_us", "en_GB"]:       
            if l in self.summarys:
                self.summary = self.summarys[l]
                break
            
class Addon():
    def __init__(self, parent, xmlelement):

        self.parent = parent
        self.id      = xmlelement.attrib["id"]
        self.name    = xmlelement.attrib["name"]
        self.version = xmlelement.attrib["version"]
        self.provider_name = xmlelement.attrib["provider-name"] if "provider-name" in xmlelement.attrib else ""
        self.broken  = xmlelement.find('broken') != None
        self.extensions = []
        self.requirements = []
        self.isAdult = self.id in settings.ADULT_PLUGINS
        for extension in xmlelement.findall('extension'):
            self.extensions.append(Extension(self, extension))
        for requirement in xmlelement.findall('requires'):
            for requirement_import in requirement.findall('import'):
                self.requirements.append(Requirement(self, requirement_import))
            
                
    def getExtentionsByPoint(self,extension_point):
        return [e for e in self.extensions if e.point == extension_point]
        
    def getExtentionsByProvides(self, provides):
        return [e for e in self.extensions if provides in e.provides]
          
    def __str__(self):
        p = "None"
        if self.parent != None:
            p = self.parent.id
        return "%s\t%s\tParent:%s" % (self.id, self.version, p)
        
    def __repr__(self):
        return self.__str__()
   
class RepositoryAddon():
    def __init__(self, parent, xmlelement):
        self.parent = parent
        self.addons = [] 
        for addonElement in xmlelement.findall('addon'):
            addon = Addon(parent, addonElement)
            self.addons.append(addon)
          
    def getInstallableById(self, addon_id):
        r = [a for a in self.addons if a.id == addon_id]
        return r
        
if __name__ == "__main__":
    commandline()

