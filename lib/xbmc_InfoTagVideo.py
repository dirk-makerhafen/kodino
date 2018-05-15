
class InfoTagVideo(object):
    """
    Kodi's video info tag class

    To get video info tag data of currently played source.

    Info tag load is only be possible from present player class.

    Example::

        ...
        tag = xbmc.Player().getVideoInfoTag()
        
        title = tag.getTitle()
        file  = tag.getFile()
        ...
    """
    
    def __init__(self):
        # type: () -> None
        pass
    
    def getDbId(self):
        # type: () -> int
        """
        Get identification number of tag in database 

        :return: [integer] database id

        New function added.
        """
        return 0
    
    def getDirector(self):
        # type: () -> str
        """
        Get film director who has made the film (if present). 

        :return: [string] Film director name.
        """
        return ""
    
    def getWritingCredits(self):
        # type: () -> str
        """
        Get the writing credits if present from video info tag. 

        :return: [string] Writing credits
        """
        return ""
    
    def getGenre(self):
        # type: () -> str
        """
        To get the Video Genre if available. 

        :return: [string] Genre name
        """
        return ""
    
    def getTagLine(self):
        # type: () -> str
        """
        Get video tag line if available. 

        :return: [string] Video tag line
        """
        return ""
    
    def getPlotOutline(self):
        # type: () -> str
        """
        Get the outline plot of the video if present. 

        :return: [string] Outline plot
        """
        return ""
    
    def getPlot(self):
        # type: () -> str
        """
        Get the plot of the video if present. 

        :return: [string] Plot
        """
        return ""
    
    def getPictureURL(self):
        # type: () -> str
        """
        Get a picture URL of the video to show as screenshot. 

        :return: [string] Picture URL
        """
        return ""
    
    def getTitle(self):
        # type: () -> str
        """
        Get the video title. 

        :return: [string] Video title
        """
        return ""
    
    def getTVShowTitle(self):
        # type: () -> str
        """
        Get the video TV show title. 

        :return: [string] TV show title

        New function added.
        """
        return ""
    
    def getMediaType(self):
        # type: () -> str
        """
        Get the media type of the video. 

        :return: [string] media type

        Available strings about media type for video:

        ===========  =====================================
        String       Description                          
        ===========  =====================================
        video        For normal video                     
        set          For a selection of video             
        musicvideo   To define it as music video          
        movie        To define it as normal movie         
        tvshow       If this is it defined as tvshow      
        season       The type is used as a series season  
        episode      The type is used as a series episode 
        ===========  =====================================

        New function added.
        """
        return ""
    
    def getVotes(self):
        # type: () -> str
        """
        Get the video votes if available from video info tag. 

        :return: [string] Votes
        """
        return ""
    
    def getCast(self):
        # type: () -> str
        """
        To get the cast of the video when available. 

        :return: [string] Video casts
        """
        return ""
    
    def getFile(self):
        # type: () -> str
        """
        To get the video file name. 

        :return: [string] File name
        """
        return ""
    
    def getPath(self):
        # type: () -> str
        """
        To get the path where the video is stored. 

        :return: [string] Path
        """
        return ""
    
    def getIMDBNumber(self):
        # type: () -> str
        """
        To get the IMDb number of the video (if present). 

        :return: [string] IMDb number
        """
        return ""
    
    def getSeason(self):
        # type: () -> int
        """
        To get season number of a series 

        :return: [integer] season number

        New function added.
        """
        return 0
    
    def getEpisode(self):
        # type: () -> int
        """
        To get episode number of a series 

        :return: [integer] episode number

        New function added.
        """
        return 0
    
    def getYear(self):
        # type: () -> int
        """
        Get production year of video if present. 

        :return: [integer] Production Year
        """
        return 0
    
    def getRating(self):
        # type: () -> float
        """
        Get the video rating if present as float (double where supported).

        :return: [float] The rating of the video
        """
        return 0.0
    
    def getUserRating(self):
        # type: () -> int
        """
        Get the user rating if present as integer. 

        :return: [integer] The user rating of the video
        """
        return 0
    
    def getPlayCount(self):
        # type: () -> int
        """
        To get the number of plays of the video. 

        :return: [integer] Play Count
        """
        return 0
    
    def getLastPlayed(self):
        # type: () -> str
        """
        Get the last played date / time as string. 

        :return: [string] Last played date / time
        """
        return ""
    
    def getOriginalTitle(self):
        # type: () -> str
        """
        To get the original title of the video. 

        :return: [string] Original title
        """
        return ""
    
    def getPremiered(self):
        # type: () -> str
        """
        To get premiered date of the video, if available. 

        :return: [string]
        """
        return ""
    
    def getFirstAired(self):
        # type: () -> str
        """
        Returns first aired date as string from info tag. 

        :return: [string] First aired date
        """
        return ""
    
    def getTrailer(self):
        # type: () -> str
        """
        To get the path where the trailer is stored. 

        :return: [string] Trailer path

        New function added.
        """
        return ""
    