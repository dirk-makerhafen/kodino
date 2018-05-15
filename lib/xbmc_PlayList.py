import json, redis
import settings
import xbmcWrapperCommon
playlistInstance = None

redis_connection = redis.StrictRedis(host=settings.REDIS_HOST, port= settings.REDIS_PORT,db= settings.REDIS_DB)


class PlayList(object):
    """
    Kodi's Play List class

    To create and edit a playlist which can be handled by the player.

    :param playList: [integer] To define the stream type

    ======  ====================  ====================================
    Value   Integer String        Description                         
    ======  ====================  ====================================
    0       xbmc.PLAYLIST_MUSIC   Playlist for music files or streams 
    1       xbmc.PLAYLIST_VIDEO   Playlist for video files or streams 
    ======  ====================  ====================================

    Example::

        ...
        play=xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        ...
    """
    
    def __init__(self, playList):
        # type: (int) -> None
        self.items = []
        global playlistInstance
        playlistInstance = self
    
    def getPlayListId(self):
        # f() -> int
        """
        Get the PlayList Identifier 

        :return: Id as an integer. 
        """
        return 0
    
    def add(self, url, listitem=None, index=-1):
        # type: (str_type, Any, int) -> Non
        print("PlayList.add('%s', %s , %s)" % ( url, listitem, index))
        """
        Adds a new file to the playlist. 

        :param url: string or unicode - filename or url to add. 
        :param listitem: [opt] listitem - used with setInfo() to set different
            infolabels.
        :param index: [opt] integer - position to add playlist item.
            (default=end)

        You can use the above as keywords for arguments and skip certain
        optional arguments. Once you use a keyword, all following arguments
        require the keyword.

        Example::

            ..
            playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
            video = 'F:\\movies\\Ironman.mov'
            listitem = xbmcgui.ListItem('Ironman', thumbnailImage='F:\\movies\\Ironman.tbn')
            listitem.setInfo('video', {'Title': 'Ironman', 'Genre': 'Science Fiction'})
            playlist.add(url=video, listitem=listitem, index=7)n
            ..
        """
        if listitem != None:
            l = listitem.values
        else:
            l = None
        redis_connection.rpush(xbmcWrapperCommon.CURRENT_QUEUE, json.dumps({"key": "xbmc_PlayList:add" , "handle" : xbmcWrapperCommon.CURRENT_HANDLE, "url" : url , "listitem" : l}))
        self.items.append([url,listitem])

    
    def load(self, filename):
        # type: (str) -> bool
        """
        Load a playlist. 

        Clear current playlist and copy items from the file to this Playlist
        filename can be like .pls or .m3u

        :param filename: File with list to play inside 
        :return: False if unable to load playlist 
        """
        return True
    
    def remove(self, filename):
        # type: (str) -> None
        """
        Remove an item with this filename from the playlist. 

        :param filename: The file to remove from list. 
        """
        pass
    
    def clear(self):
        # type: () -> None
        """
        Clear all items in the playlist.
        """
        pass
    
    def size(self):
        # type: () -> int
        """
        Returns the total number of PlayListItems in this playlist. 

        :return: Amount of playlist entries. 
        """
        return 0
    
    def shuffle(self):
        # type: () -> None
        """
        Shuffle the playlist.
        """
        pass
    
    def unshuffle(self):
        # type: () -> None
        """
        Unshuffle the playlist
        """
        pass
    
    def getposition(self):
        # type: () -> int
        """
        Returns the position of the current song in this playlist. 

        :return: Position of the current song 
        """
        return 0
    
