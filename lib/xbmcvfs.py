import sys,os

from xbmcvfs_File import File
from xbmcvfs_Stat import Stat

import xbmc
import settings

def is_valid_path(path):
    ap = os.path.abspath(path)
    if ap.startswith(settings.PLUGINS_FOLDER) or ("%s/home" % ap).startswith(settings.SPECIAL_FOLDER):
        return True
    print("'%s' is not a valid path" % path)
    return False    

def copy(strSource, strDestnation):
    print("xbmcvfs.py copy('%s', '%s') Not implemented" % (strSource, strDestnation))
    # type: (str_type, str_type) -> bool
    return True


def delete(file):
    print("xbmcvfs.py delete('%s') Not implemented" % (file))
    # type: (str_type) -> bool
    return True


def rename(file, newFile):
    print("xbmcvfs.py rename('%s', '%s') Not implemented" % (file, newFile))
    # type: (str_type, str_type) -> bool
    return True


def exists(path):
    path = xbmc.translatePath(path)
    if is_valid_path(path):
        return os.path.exists(path)
    # type: (str_type) -> bool
    print("not valid")    
    return False


def mkdir(path):
    path = xbmc.translatePath(path)
    # type: (str_type) -> bool
    if is_valid_path(path):
        if not os.path.exists(path):
            return os.makedirs(path)
    return False


def mkdirs(path):
    path = xbmc.translatePath(path)
    # type: (str_type) -> bool
    if is_valid_path(path):
        return os.makedirs(path)
    return False
    print("not valid")

def rmdir(path, force=False):
    # type: (str_type, bool) -> bool
    print("xbmcvfs.py rmdir('%s') Not implemented" % (force))    
    return True


def listdir(path):
    # type: (str_type) -> Tuple[List[str], List[str]]
    return [""], [""]
        
        
        
