
import settings
import redis
import xbmcWrapperCommon

redis_connection = redis.StrictRedis(host=settings.REDIS_HOST, port= settings.REDIS_PORT,db= settings.REDIS_DB)


class ListItem(object):
    """
    Selectable window list item

    The list item control is used for creating item lists in Kodi

    :param label: [opt] string 
    :param label2: [opt] string 
    :param iconImage: **Deprecated. Use setArt**
    :param thumbnailImage: **Deprecated. Use setArt**
    :param path: [opt] string

    .. note::
        **iconImage** and **thumbnailImage** are deprecated. Use **setArt()**.

    Example::

        ...
        listitem = xbmcgui.ListItem('Casino Royale')
        ...
    """
    
    def __init__(self, label="", label2="", iconImage="", thumbnailImage="", path=""):
        # type: (str_type, str_type, str_type, str_type, str_type) -> None
        self.values = dict()
        
        self.values["title"] = label
        self.values["title2"] = label2
        self.values["icon"] = iconImage
        self.values["thumbnailimage"] = thumbnailImage
        self.values["path"] = path
        self.values["isfolder"] = True
    
    def __setitem__(self, key, value):
        self.values[key.lower()] = value;
    
    def __getitem__(self,key):
        return self.values[key.lower()]
          
    
    def getLabel(self):
        # type: () -> str
        """
        Returns the listitem label. 

        :return: Label of item

        Example::

            ...
            # getLabel()
            label = listitem.getLabel()
            ...
        """
        return ""
    
    def getLabel2(self):
        # type: () -> str
        """
        Returns the second listitem label. 

        :return: Second label of item

        Example::

            ...
            # getLabel2()
            label = listitem.getLabel2()
            ...
        """
        return ""
    
    def setLabel(self, label):
        # type: (str_type) -> None
        """
        Sets the listitem's label. 

        :param label: string or unicode - text string.

        Example::

            ...
            # setLabel(label)
            listitem.setLabel('Casino Royale')
            ...
        """
        pass
    
    def setLabel2(self, label):
        # type: (str_type) -> None
        """
        Sets the listitem's label2. 

        :param label: string or unicode - text string.

        Example::

            ...
            # setLabel2(label)
            listitem.setLabel2('Casino Royale')
            ...
        """
        pass
    
    def setIconImage(self, iconImage):
        # type: (str_type) -> None
        """
        Deprecated. Use **setArt()**. 


        """
        pass
    
    def setThumbnailImage(self, thumbFilename):
        # type: (str_type) -> None
        """
        .. warning:: Deprecated. Use **setArt()**.
        """
        pass
    
    def setArt(self, dictionary):
        print("xbmcgui_ListItem.setArt(%s)" % dictionary)
        # type: (Dict[str, str_type]) -> None
        """
        Sets the listitem's art 

        :param values: dictionary - pairs of  ``label: value``.
            Some default art values (any string possible):

        ==========  ========================
        Label       Type                    
        ==========  ========================
        thumb       string - image filename 
        poster      string - image filename 
        banner      string - image filename 
        fanart      string - image filename 
        clearart    string - image filename 
        clearlogo   string - image filename 
        landscape   string - image filename 
        icon        string - image filename 
        ==========  ========================

        New function added.  Added new label **icon**.

        Example::

            ...
            # setArt(values)
            listitem.setArt(``'poster': 'poster.png', 'banner' : 'banner.png'``)
            ...
        """
        if "thumb" in dictionary:
            if dictionary["thumb"] != "" and self.values["thumbnailimage"] == "":
                self.values["thumbnailimage"] = dictionary["thumb"]
    
    def setUniqueIDs(self, dictionary):
        # type: (Dict[str, str_type]) -> None
        """
        Sets the listitem's uniqueID 

        :param values: dictionary - pairs of  ``label: value``.
            Some example values (any string possible):

        ======  =======================
        Label   Type                   
        ======  =======================
        imdb    string - uniqueid name 
        tvdb    string - uniqueid name 
        tmdb    string - uniqueid name 
        anidb   string - uniqueid name 
        ======  =======================

        Example::

            ...
            # setUniqueIDs(values)
            listitem.setUniqueIDs(``'imdb': 'tt8938399', 'tmdb' : '9837493'``)
            ...
        """
        pass
    
    def setRating(self, type, rating, votes=0, defaultt=False):
        # type: (str_type, float, int, bool) -> None
        """
        Sets a listitem's rating. It needs at least type and rating param 

        :param type: string - the type of the rating. Any string. 
        :param rating: float - the value of the rating. 
        :param votes: int - the number of votes. Default 0. 
        :param defaultt: bool - is the default rating?. Default False.
            Some example type (any string possible):

        ======  =====================
        Label   Type                 
        ======  =====================
        imdb    string - rating type 
        tvdb    string - rating type 
        tmdb    string - rating type 
        anidb   string - rating type 
        ======  =====================

        Example::

            ...
            # setRating(type, rating, votes, defaultt))
            listitem.setRating("imdb", 4.6, 8940, True)
            ...
        """
        pass
    
    def getArt(self, key):
        # type: (str) -> str
        """
        Returns a listitem art path as a string, similar to an infolabel.

        :param key: string - art name.Some default art values (any string possible):

        ==========  ====================
        Label       Type                
        ==========  ====================
        thumb       string - image path 
        poster      string - image path 
        banner      string - image path 
        fanart      string - image path 
        clearart    string - image path 
        clearlogo   string - image path 
        landscape   string - image path 
        icon        string - image path 
        ==========  ====================

        New function added.


        Example::

            ...
            poster = listitem.getArt('poster')
            ...
        """
        return ""
    
    def getUniqueID(self, key):
        # type: (str) -> str
        """
        Returns a listitem uniqueID as a string, similar to an infolabel.

        :param key: string - uniqueID name.Some default uniqueID values
            (any string possible):

        ======  =======================
        Label   Type                   
        ======  =======================
        imdb    string - uniqueid name 
        tvdb    string - uniqueid name 
        tmdb    string - uniqueid name 
        anidb   string - uniqueid name 
        ======  =======================

        Example::

            ...
            uniqueID = listitem.getUniqueID('imdb')
            ...
        """
        return ""
    
    def getRating(self, key):
        # type: (str) -> float
        """
        Returns a listitem rating as a float.

        :param key: string - rating type.Some default key values
            (any string possible):

        ======  ===================
        Label   Type               
        ======  ===================
        imdb    string - type name 
        tvdb    string - type name 
        tmdb    string - type name 
        anidb   string - type name 
        ======  ===================

        Example::

            ...
            rating = listitem.getRating('imdb')
            ...
        """
        return 0.0
    
    def getVotes(self, key):
        # type: (str) -> int
        """
        Returns a listitem votes as a integer.

        :param key: string - rating type.Some default key values
            (any string possible):

        ======  ===================
        Label   Type               
        ======  ===================
        imdb    string - type name 
        tvdb    string - type name 
        tmdb    string - type name 
        anidb   string - type name 
        ======  ===================

        Example::

            ...
            votes = listitem.getVotes('imdb')
            ...
        """
        return 0
    
    def select(self, selected):
        # type: (bool) -> None
        """
        Sets the listitem's selected status. 

        :param selected: bool - True=selected/False=not selected

        Example::

            ...
            # select(selected)
            listitem.select(True)
            ...
        """
        pass
    
    def isSelected(self):
        # type: () -> bool
        """
        Returns the listitem's selected status. 

        :return: bool - true if selected, otherwise false

        Example::

            ...
            # isSelected()
            selected = listitem.isSelected()
            ...
        """
        return True
    
    def setInfo(self, type, infoLabels):
        # type: (str, Dict[str, str_type]) -> None
        """
        Sets the listitem's infoLabels. 

        :param type: string - type of 
        :param infoLabels: dictionary - pairs of  ``label: value``

        **Available types**

        =============  ======================
        Command name   Description           
        =============  ======================
        video          Video information     
        music          Music information     
        pictures       Pictures informantion 
        =============  ======================

        To set pictures exif info, prepend  ``exif:`` to the label.
        Exif values must be passed as strings, separate value pairs with
        a comma. **(eg.  ``{'exif:resolution': '720,480'}``**
        See kodi_pictures_infotag for valid strings. You can use the above
        as keywords for arguments and skip certain optional arguments.
        Once you use a keyword, all following arguments require the keyword.

        **General Values** (that apply to all types):

        ===========  ===========================================================
        Info label   Description                                                                  
        ===========  ===========================================================
        count        integer (12) - can be used to store an id for later,
                     or for sorting purposes
        size         long (1024) - size in bytes                                                  
        date         string (d.m.Y / 01.01.2009) - file date                                      
        ===========  ===========================================================

        **Video Values**:

        ==============  ========================================================
        Info label      Description                                                                                                           
        ==============  ========================================================
        genre           string (Comedy)                                                                                                       
        country         string (Germany)                                                                                                      
        year            integer (2009)                                                                                                        
        episode         integer (4)                                                                                                           
        season          integer (1)                                                                                                           
        top250          integer (192)                                                                                                         
        setid           integer (14)                                                                                                          
        tracknumber     integer (3)                                                                                                           
        rating          float (6.4) - range is 0..10                                                                                          
        userrating      integer (9) - range is 1..10 (0 to reset)                                                                             
        watched         depreciated - use playcount instead                                                                                   
        playcount       integer (2) - number of times this item has been played                                                               
        overlay         integer (2) - range is                                                                                                  0..7  . See Overlay icon types for values 
        cast            list (["Michal C. Hall","Jennifer Carpenter"]) -
                        if provided a list of tuples cast will be interpreted
                        as castandrole
        castandrole     list of tuples ([("Michael C. Hall","Dexter"),
                        ("Jennifer Carpenter","Debra")])
        director        string (Dagur Kari)                                                                                                   
        mpaa            string (PG-13)                                                                                                        
        plot            string (Long Description)                                                                                             
        plotoutline     string (Short Description)                                                                                            
        title           string (Big Fan)                                                                                                      
        originaltitle   string (Big Fan)                                                                                                      
        sorttitle       string (Big Fan)                                                                                                      
        duration        integer (245) - duration in seconds                                                                                   
        studio          string (Warner Bros.)                                                                                                 
        tagline         string (An awesome movie) - short description of movie                                                                
        writer          string (Robert D. Siegel)                                                                                             
        tvshowtitle     string (Heroes)                                                                                                       
        premiered       string (2005-03-04)                                                                                                   
        status          string (Continuing) - status of a TVshow                                                                              
        set             string (Batman Collection) - name of the collection                                                                   
        imdbnumber      string (tt0110293) - IMDb code                                                                                        
        code            string (101) - Production code                                                                                        
        aired           string (2008-12-07)                                                                                                   
        credits         string (Andy Kaufman) - writing credits                                                                               
        lastplayed      string (Y-m-d h:m:s = 2009-04-05 23:16:04)                                                                            
        album           string (The Joshua Tree)                                                                                              
        artist          list (['U2'])                                                                                                         
        votes           string (12345 votes)                                                                                                  
        path            string (/home/user/movie.avi)                                                                                         
        trailer         string (/home/user/trailer.avi)                                                                                       
        dateadded       string (Y-m-d h:m:s = 2009-04-05 23:16:04)                                                                            
        mediatype       string - "video", "movie", "tvshow", "season", "episode"
                        or "musicvideo"
        dbid            integer (23) - Only add this for items which are part
                        of the local db. You also need to set the correct 'mediatype'!
        ==============  ========================================================

        **Music Values**:

        =========================  =============================================
        Info label                 Description                                             
        =========================  =============================================
        tracknumber                integer (8)                                             
        discnumber                 integer (2)                                             
        duration                   integer (245) - duration in seconds                     
        year                       integer (1998)                                          
        genre                      string (Rock)                                           
        album                      string (Pulse)                                          
        artist                     string (Muse)                                           
        title                      string (American Pie)                                   
        rating                     float - range is between 0 and 10                       
        userrating                 integer - range is 1..10                                
        lyrics                     string (On a dark desert highway...)                    
        playcount                  integer (2) - number of times this item has
                                   been played
        lastplayed                 string (Y-m-d h:m:s = 2009-04-05 23:16:04)              
        mediatype                  string - "music", "song", "album", "artist"             
        listeners                  integer (25614)                                         
        musicbrainztrackid         string (cd1de9af-0b71-4503-9f96-9f5efe27923c)           
        musicbrainzartistid        string (d87e52c5-bb8d-4da8-b941-9f4928627dc8)           
        musicbrainzalbumid         string (24944755-2f68-3778-974e-f572a9e30108)           
        musicbrainzalbumartistid   string (d87e52c5-bb8d-4da8-b941-9f4928627dc8)           
        comment                    string (This is a great song)                           
        =========================  =============================================

        **Picture Values**:

        ============  =====================================================
        Info label    Description                                          
        ============  =====================================================
        title         string (In the last summer-1)                        
        picturepath   string (/home/username/pictures/img001.jpg  )
        exif*         string (See kodi_pictures_infotag for valid strings) 
        ============  =====================================================

        Added new label **discnumber**.  **duration** has to be set in seconds.
        Added new label **mediatype**.
        Added labels **setid**, **set**, **imdbnumber**, **code**, **dbid**,
        **path** and **userrating**.
        Expanded the possible infoLabels for the option **mediatype**.

        Example::

            ...
            listitem.setInfo('video', ``'genre': 'Comedy'``)
            ...
        """
        try:
            keys =  infoLabels.keys()
            for key in keys:
                self.values[key.lower()] = infoLabels[key]
        except:
            pass
    
    def setCast(self, actors):
        # type: (List[Dict[str, str_type]]) -> None
        """
        Set cast including thumbnails

        :param actors: list of dictionaries (see below for relevant keys)

        Keys:

        ==========  =========================
        Label       Description              
        ==========  =========================
        name        string (Michael C. Hall) 
        role        string (Dexter)          
        thumbnail   string (http://www.someurl.com/someimage.png  )
        order       integer (1)              
        ==========  =========================

        New function added.

        Example::

            ...
            actors = [{"name": "Actor 1", "role": "role 1"},
                      {"name": "Actor 2", "role": "role 2"}]
            listitem.setCast(actors)
            ...
        """
        pass
    
    def addStreamInfo(self, cType, dictionary):
        # type: (str, Dict[str, str_type]) -> None
        """
        Add a stream with details.

        :param type: string - type of stream(video/audio/subtitle). 
        :param values: dictionary - pairs of ``label: value``.

        Video Values:

        =========  ==================
        Label      Description       
        =========  ==================
        codec      string (h264)     
        aspect     float (1.78)      
        width      integer (1280)    
        height     integer (720)     
        duration   integer (seconds) 
        =========  ==================

        Audio Values:

        =========  =============
        Label      Description  
        =========  =============
        codec      string (dts) 
        language   string (en)  
        channels   integer (2)  
        =========  =============

        Subtitle Values:

        =========  =============
        Label      Description  
        =========  =============
        language   string (en)  
        =========  =============

        Example::

            ...
            listitem.addStreamInfo('video', ``'codec': 'h264', 'width' : 1280``)
            ...
        """
        pass
    
    def addContextMenuItems(self, items, replaceItems=False):
        # type: (List[Tuple[str_type, str_type]], bool) -> None
        """
        Adds item(s) to the context menu for media lists. 

        :param items: list - [(label, action,)*] A list of tuples consisting
            of label and action pairs.

        * label [string or unicode] - item's label
        * action [string or unicode] - any built-in function to perform.

        List of functions - http://kodi.wiki/view/List_of_Built_In_Functions

        You can use the above as keywords for arguments and skip certain optional
        arguments. Once you use a keyword, all following arguments require
        the keyword.

        Completely removed option **replaceItems**.

        Example::

            ...
            listitem.addContextMenuItems(
                [('Theater Showtimes',
                'RunScript(special://home/scripts/showtimes/default.py,Iron Man)',)]
                )
            ...
        """
        for item in items:
            if item[0] == "Save video":
                self.values["isfolder"] = False
    
    def setProperty(self, key, value):
        # type: (str, str_type) -> None
        """
        Sets a listitem property, similar to an infolabel. 

        :param key: string - property name. 
        :param value: string or unicode - value of property.

        Key is NOT case sensitive. You can use the above as keywords
        for arguments and skip certain optional arguments.
        Once you use a keyword, all following arguments require the keyword.
        Some of these are treated internally by Kodi, such as the 'StartOffset'
        property, which is the offset in seconds at which to start playback of
        an item. Others may be used in the skin to add extra information,
        such as 'WatchedCount' for tvshow items

        Example::

            ...
            listitem.setProperty('AspectRatio', '1.85 : 1')
            listitem.setProperty('StartOffset', '256.4')
            ...
        """
        self.values[key.lower()] = value

    
    def getProperty(self, key):
        # type: (str) -> str
        """
        Returns a listitem property as a string, similar to an infolabel. 

        :param key: string - property name.

        Key is NOT case sensitive. You can use the above as keywords
        for arguments and skip certain optional arguments. Once you use
        a keyword, all following arguments require the keyword.

        Example::

            ...
            AspectRatio = listitem.getProperty('AspectRatio')
            ...
        """
        if key.lower() in self.values:
            return self.values[key.lower()]
        return ""
    
    def setPath(self, path):
        # type: (str_type) -> None
        """
        Sets the listitem's path. 

        :param path: string or unicode - path, activated when item is clicked.

        You can use the above as keywords for arguments.

        Example::

            ...
            listitem.setPath(path='/path/to/some/file.ext')
            ...
        """
        self.values["path"] = path

    
    def setMimeType(self, mimetype):
        # type: (str_type) -> None
        """
        Sets the listitem's mimetype if known. 

        :param mimetype: string or unicode - mimetype

        If known prehand, this can (but does not have to) avoid HEAD requests
        being sent to HTTP servers to figure out file type.
        """
        pass
    
    def setContentLookup(self, enable):
        # type: (bool) -> None
        """
        Enable or disable content lookup for item. 

        If disabled, HEAD requests to e.g determine mime type will not be sent.

        enable bool to enable content lookup 

        New function added. 
        """
        pass
    
    def setSubtitles(self, subtitleFiles):
        # type: (List[str_type]) -> None
        """
        Sets subtitles for this listitem. 

        :param subtitleFiles: list with path to subtitle files

        Example::

            ...
            listitem.setSubtitles(['special://temp/example.srt', 'http://example.com/example.srt'])
            ...
          New function added. 
        """
        pass
    
    def getdescription(self):
        # type: () -> str
        """
        .. warning:: Deprecated.
        """
        return ""
    
    def getduration(self):
        # type: () -> str
        """
        .. warning:: Deprecated. Use **InfoTagMusic**.
        """
        return ""
    
    def getfilename(self):
        # type: () -> str
        """
        .. warning:: Deprecated.
        """
        return ""
    
    def getPath(self):
        # type: () -> str
        """
        Returns the path of this listitem. 

        [string] filename 

        New function added. 
        """
        return ""
    
    def getVideoInfoTag(self):
        # type: () -> InfoTagVideo
        """
        Returns the VideoInfoTag for this item. 

        video info tag 

        New function added. 
        """
        return InfoTagVideo()
    
    def getMusicInfoTag(self):
        # type: () -> InfoTagMusic
        """
        Returns the MusicInfoTag for this item. 

        music info tag 

        New function added. 
        """
        return InfoTagMusic()
    
    def __str__(self):
        return "%s" % self.values