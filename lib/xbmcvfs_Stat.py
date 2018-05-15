
class Stat(object):
    """
    Get file or file system status

    These class return information about a file. Execute (search) permission
    is required on all of the directories in path that lead to the file.

    :param path: [string] file or folder

    New function added

    Example::

        ..
          st = xbmcvfs.Stat(path)
          modified = st.st_mtime()
        ..
    """
    
    def __init__(self, path):
        # type: (str_type) -> None
        pass
    
    def st_mode(self):
        # type: () -> long
        """
        To get file protection. 

        :return: st_mode 
        """
        return 0L
    
    def st_ino(self):
        # type: () -> long
        """
        To get inode number. 

        :return: st_ino 
        """
        return 0L
    
    def st_dev(self):
        # type: () -> long
        """
        To get ID of device containing file. 

        The st_dev field describes the device on which this file resides.

        :return: st_dev 
        """
        return 0L
    
    def st_nlink(self):
        # type: () -> long
        """
        To get number of hard links. 

        :return: st_nlink 
        """
        return 0L
    
    def st_uid(self):
        # type: () -> long
        """
        To get user ID of owner. 

        :return: st_uid 
        """
        return 0L
    
    def st_gid(self):
        # type: () -> long
        """
        To get group ID of owner. 

        :return: st_gid 
        """
        return 0L
    
    def st_size(self):
        # type: () -> long
        """
        To get total size, in bytes. 

        The st_size field gives the size of the file (if it is a regular file
        or a symbolic link) in bytes. The size of a symbolic link (only on Linux
        and Mac OS X) is the length of the pathname it contains, without
        a terminating null byte.

        :return: st_size 
        """
        return 0L
    
    def atime(self):
        # type: () -> long
        """
        To get time of last access. 

        :return: st_atime 
        """
        return 0L
    
    def mtime(self):
        # type: () -> long
        """
        To get time of last modification. 

        :return: st_mtime 
        """
        return 0L
    
    def ctime(self):
        # type: () -> long
        """
        To get time of last status change. 

        :return: st_ctime 
        """
        return 0L
