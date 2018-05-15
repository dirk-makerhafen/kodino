
class InfoTagMusic(object):
    """
    Kodi's music info tag class

    To get music info tag data of currently played source.

    Info tag load is only be possible from present player class.

    Example::

        ...
        tag = xbmc.Player().getMusicInfoTag()
        
        title = tag.getTitle()
        url   = tag.getURL()
        ...
    """
    
    def __init__(self):
        # type: () -> None
        pass
    
    def getURL(self):
        # type: () -> str
        """
        Returns url of source as string from music info tag. 

        :return: [string] Url of source
        """
        return ""
    
    def getTitle(self):
        # type: () -> str
        """
        Returns the title from music as string on info tag. 

        :return: [string] Music title
        """
        return ""
    
    def getArtist(self):
        # type: () -> str
        """
        Returns the artist from music as string if present. 

        :return: [string] Music artist
        """
        return ""
    
    def getAlbum(self):
        # type: () -> str
        """
        Returns the album from music tag as string if present. 

        :return: [string] Music album name
        """
        return ""
    
    def getAlbumArtist(self):
        # type: () -> str
        """
        Returns the album artist from music tag as string if present.

        :return: [string] Music album artist name
        """
        return ""
    
    def getGenre(self):
        # type: () -> str
        """
        Returns the genre name from music tag as string if present. 

        :return: [string] Genre name
        """
        return ""
    
    def getDuration(self):
        # type: () -> int
        """
        Returns the duration of music as integer from info tag. 

        :return: [integer] Duration
        """
        return 0
    
    def getRating(self):
        # type: () -> int
        """
        Returns the scraped rating as integer. 

        :return: [integer] Rating
        """
        return 0
    
    def getUserRating(self):
        # type: () -> int
        """
        Returns the user rating as integer (-1 if not existing) 

        :return: [integer] User rating
        """
        return 0
    
    def getTrack(self):
        # type: () -> int
        """
        Returns the track number (if present) from music info tag as integer. 

        :return: [integer] Track number
        """
        return 0
    
    def getDisc(self):
        # type: () -> int
        """
        Returns the disk number (if present) from music info tag as integer. 

        :return: [integer] Disc number
        """
        return 0
    
    def getReleaseDate(self):
        # type: () -> str
        """
        Returns the release date as string from music info tag (if present). 

        :return: [string] Release date
        """
        return ""
    
    def getListeners(self):
        # type: () -> int
        """
        Returns the listeners as integer from music info tag. 

        :return: [integer] Listeners
        """
        return 0
    
    def getPlayCount(self):
        # type: () -> int
        """
        Returns the number of carried out playbacks. 

        :return: [integer] Playback count
        """
        return 0
    
    def getLastPlayed(self):
        # type: () -> str
        """
        Returns last played time as string from music info tag. 

        :return: [string] Last played date / time on tag
        """
        return ""
    
    def getComment(self):
        # type: () -> str
        """
        Returns comment as string from music info tag. 

        :return: [string] Comment on tag
        """
        return ""
    
    def getLyrics(self):
        # type: () -> str
        """
        Returns a string from lyrics. 

        :return: [string] Lyrics on tag
        """
        return ""
    
