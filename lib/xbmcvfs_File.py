
class File(object):
    """
    Kodi's file class

    :param filepath: string Selected file path 
    :param mode: [opt] string Additional mode options (if no mode is supplied,
        the default is Open for Read).

    =====  ===============
    Mode   Description    
    =====  ===============
    w      Open for write 
    =====  ===============

    Example::

        ..
        f = xbmcvfs.File(file, 'w')
        ..
    """
    
    def __init__(self, filepath, mode=None):
        # type: (str_type, str) -> None
        pass
    
    def read(self, numBytes=0):
        # type: (int_type) -> str
        """
        Read file parts as string. 

        :param bytes: [opt] How many bytes to read - if not set it will read
            the whole file
        :return: string

        Example::

            ..
            f = xbmcvfs.File(file)
            b = f.read()
            f.close()
            ..
        """
        return ""
    
    def readBytes(self, numBytes=0):
        # type: (int_type) -> bytearray
        """
        Read bytes from file. 

        :param numbytes: How many bytes to read [opt]- if not set it will
            read the whole file
        :return: bytearray

        Example::

            ..
            f = xbmcvfs.File(file)
            b = f.read()
            f.close()
            ..
        """
        return bytearray()
    
    def write(self, buffer):
        # type: (Union[str, bytearray]) -> bool
        """
        To write given data in file. 

        :param buffer: Buffer to write to file 
        :return: True on success.

        Example::

            ..
            f = xbmcvfs.File(file, 'w')
            result = f.write(buffer)
            f.close()
            ..
        """
        return True
    
    def size(self):
        # type: () -> long
        """
        Get the file size. 

        :return: The file size

        Example::

            ..
            f = xbmcvfs.File(file)
            s = f.size()
            f.close()
            ..
        """
        return 0L
    
    def seek(self, seekBytes, iWhence):
        # type: (int_type, int) -> long
        """
        Seek to position in file. 

        :param seekBytes: position in the file 
        :param iWhence: where in a file to seek from [0 begining, 1 current ,
            2 end possition]

        Example::

            ..
            f = xbmcvfs.File(file)
            result = f.seek(8129, 0)
            f.close()
            ..
        """
        return 0L
    
    def close(self):
        # type: () -> None
        """
        Close opened file. 



        Example::

            ..
            f = xbmcvfs.File(file)
            f.close()
            ..
        """
        pass