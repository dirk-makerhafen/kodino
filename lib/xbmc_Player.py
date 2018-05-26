import json, redis
from xbmc_PlayList import PlayList

import settings
import xbmcWrapperCommon

redis_connection = redis.StrictRedis(host=settings.REDIS_HOST, port= settings.REDIS_PORT,db= settings.REDIS_DB)

class Player(object):
    """
    Kodi's player

    To become and create the class to play something.

    Example::

        ...
        xbmc.Player().play(url, listitem, windowed)
        ...
    """
    
    def __init__(self, playerCore=0):
        # type: (int) -> None
        pass
    
    def play(self, item="", listitem=None, windowed=False, startpos=-1):
        # type: (Union[str_type, PlayList], Any, bool, int) -> None
        """
        Play a item.

        :param item: [opt] string - filename, url or playlist 
        :param listitem: [opt] listitem - used with setInfo() to set different
            infolabels.
        :param windowed: [opt] bool - true=play video windowed,
            false=play users preference.(default)
        :param startpos: [opt] int - starting position when playing a playlist.
            Default = -1

        If item is not given then the Player will try to play the current item
        in the current playlist. You can use the above as keywords for arguments
        and skip certain optional arguments. Once you use a keyword, all
        following arguments require the keyword.

        Example::

            ...
            listitem = xbmcgui.ListItem('Ironman')
            listitem.setInfo('video', {'Title': 'Ironman', 'Genre': 'Science Fiction'})
            xbmc.Player().play(url, listitem, windowed)
            xbmc.Player().play(playlist, listitem, windowed, startpos)
            ...
        """
        if type(item) == PlayList:
            if len(item.items) > 0:
                url = item.items[0][0]
            else:
                print("PLAYLIST WONT PLAY")
                return
        else:
            url = item
        redis_connection.rpush(xbmcWrapperCommon.CURRENT_QUEUE,json.dumps({"key": "Player:play" , "url" : url}))
      
    
    def stop(self):
        # type: () -> None
        """
        Stop playing.
        """
        pass
    
    def pause(self):
        # type: () -> None
        """
        Pause or resume playing if already paused.
        """
        pass
    
    def playnext(self):
        # type: () -> None
        """
        Play next item in playlist.
        """
        pass
    
    def playprevious(self):
        # type: () -> None
        """
        Play previous item in playlist.
        """
        pass
    
    def playselected(self, selected):
        # type: (int) -> None
        """
        Play a certain item from the current playlist. 

        :param selected: Integer - Item to select 
        """
        pass
    
    def isPlaying(self):
        # type: () -> bool
        """
        Check Kodi is playing something. 

        :return: True if Kodi is playing a file. 
        """
        return False
    
    def isPlayingAudio(self):
        # type: () -> bool
        """
        Check for playing audio. 

        :return: True if Kodi is playing an audio file. 
        """
        return False
    
    def isPlayingVideo(self):
        # type: () -> bool
        """
        Check for playing video. 

        :return: True if Kodi is playing a video. 
        """
        return False
    
    def isPlayingRDS(self):
        # type: () -> bool
        """
        Check for playing radio data system (RDS). 

        :return: True if kodi is playing a radio data system (RDS). 
        """
        return True
    
    def getPlayingFile(self):
        # type: () -> str
        """
        Returns the current playing file as a string. 

        For LiveTV, returns a ``pvr://`` url which is not translatable
        to an OS specific file or external url.

        :return: Playing filename
        :raises Exception: If player is not playing a file. 
        """
        return ""
    
    def getTime(self):
        # type: () -> float
        """
        Get playing time. 

        Returns the current time of the current playing media as fractional
        seconds.

        :return: Current time as fractional seconds
        :raises Exception: If player is not playing a file. 
        """
        self._playbackLock = False # for kkplayer in youtube vault, to stop endless loop
        raise Exception("Dummy player cant play")
        #return 0.0
    
    def seekTime(self, seekTime):
        # type: (float) -> None
        """
        Seek time. 

        Seeks the specified amount of time as fractional seconds.
        The time specified is relative to the beginning of the currently
        playing media file.

        :param seekTime: Time to seek as fractional seconds 
        :raises Exception: If player is not playing a file. 
        """
        pass
    
    def setSubtitles(self, subtitleFile):
        # type: (str) -> None
        """
        Set subtitle file and enable subtitles. 

        :param subtitleFile: File to use as source ofsubtitles 
        """
        pass
    
    def showSubtitles(self, bVisible):
        # type: (bool) -> None
        """
        Enable / disable subtitles. 

        :param visible: [boolean] True for visible subtitles.

        Example::

            ...
            xbmc.Player().showSubtitles(True)
            ...
        """
        pass
    
    def getSubtitles(self):
        # type: () -> str
        """
        Get subtitle stream name.

        :return: Stream name 
        """
        return ""
    
    def getAvailableSubtitleStreams(self):
        # type: () -> List[str]
        """
        Get Subtitle stream names. 

        :return: List of subtitle streams as name 
        """
        return [""]
    
    def setSubtitleStream(self, iStream):
        # type: (int) -> None
        """
        Set Subtitle Stream. 

        :param iStream: [int] Subtitle stream to select for play

        Example::

            ...
            xbmc.Player().setSubtitleStream(1)
            ...
        """
        pass
    
    def getVideoInfoTag(self):
        # type: () -> InfoTagVideo
        """
        To get video info tag. 

        Returns the VideoInfoTag of the current playing Movie.

        :return: Video info tag
        :raises Exception: If player is not playing a file or current file
            is not a movie file.
        """
        return InfoTagVideo()
    
    def getMusicInfoTag(self):
        # type: () -> InfoTagMusic
        """
        To get music info tag. 

        Returns the MusicInfoTag of the current playing 'Song'.

        :return: Music info tag
        :raises Exception: If player is not playing a file or current file
            is not a music file.
        """
        return InfoTagMusic()
    
    def getRadioRDSInfoTag(self):
        # type: () -> InfoTagRadioRDS
        """
        To get Radio RDS info tag 

        Returns the RadioRDSInfoTag of the current playing Radio Song
        if present.

        :return: Radio RDS info tag
        :raises Exception: If player is not playing a file or current file
            is not a rds file.
        """
        return InfoTagRadioRDS()
    
    def getTotalTime(self):
        # type: () -> float
        """
        To get total playing time. 

        Returns the total time of the current playing media in seconds.
        This is only accurate to the full second.

        :return: Total time of the current playing media
        :raises Exception: If player is not playing a file. 
        """
        return 0.0
    
    def getAvailableAudioStreams(self):
        # type: () -> List[str]
        """
        Get Audio stream names 

        :return: List of audio streams as name 
        """
        return [""]
    
    def setAudioStream(self, iStream):
        # type: (int) -> None
        """
        Set Audio Stream. 

        :param iStream: [int] Audio stream to select for play

        Example::

            ...
            xbmc.Player().setAudioStream(1)
            ...
        """
        pass
    
    def getAvailableVideoStreams(self):
        # type: () -> List[str]
        """
        Get Video stream names 

        :return: List of video streams as name 
        """
        return [""]
    
    def setVideoStream(self, iStream):
        # type: (int) -> None
        """
        Set Video Stream. 

        :param iStream: [int] Video stream to select for play

        Example::

            ...
            xbmc.Player().setVideoStream(1)
            ...
        """
        pass
    
