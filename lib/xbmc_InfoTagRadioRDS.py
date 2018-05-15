
class InfoTagRadioRDS(object):
    """
    Kodi's radio RDS info tag class

    To get radio RDS info tag data of currently played PVR radio channel source.

    Info tag load is only be possible from present player class. Also is all
    the data variable from radio channels and not known on begining of radio
    receiving.

    Example::

        ...
        tag = xbmc.Player().getRadioRDSInfoTag()
        
        title  = tag.getTitle()
        artist = tag.getArtist()
        ...
    """
    
    def __init__(self):
        # type: () -> None
        pass
    
    def getTitle(self):
        # type: () -> str
        """
        Title of the item on the air; i.e. song title. 

        :return: Title 
        """
        return ""
    
    def getBand(self):
        # type: () -> str
        """
        Band of the item on air. 

        :return: Band 
        """
        return ""
    
    def getArtist(self):
        # type: () -> str
        """
        Artist of the item on air. 

        :return: Artist 
        """
        return ""
    
    def getComposer(self):
        # type: () -> str
        """
        Get the Composer of the music. 

        :return: Composer 
        """
        return ""
    
    def getConductor(self):
        # type: () -> str
        """
        Get the Conductor of the Band. 

        :return: Conductor 
        """
        return ""
    
    def getAlbum(self):
        # type: () -> str
        """
        Album of item on air. 

        :return: Album name 
        """
        return ""
    
    def getComment(self):
        # type: () -> str
        """
        Get Comment text from channel. 

        :return: Comment 
        """
        return ""
    
    def getAlbumTrackNumber(self):
        # type: () -> int
        """
        Get the album track number of currently sended music. 

        :return: Track Number 
        """
        return 0
    
    def getInfoNews(self):
        # type: () -> str
        """
        Get News informations. 

        :return: News Information 
        """
        return ""
    
    def getInfoNewsLocal(self):
        # type: () -> str
        """
        Get Local news informations. 

        :return: Local News Information 
        """
        return ""
    
    def getInfoSport(self):
        # type: () -> str
        """
        Get Sport informations. 

        :return: Sport Information 
        """
        return ""
    
    def getInfoStock(self):
        # type: () -> str
        """
        Get Stock informations. 

        :return: Stock Information 
        """
        return ""
    
    def getInfoWeather(self):
        # type: () -> str
        """
        Get Weather informations. 

        :return: Weather Information 
        """
        return ""
    
    def getInfoHoroscope(self):
        # type: () -> str
        """
        Get Horoscope informations. 

        :return: Horoscope Information 
        """
        return ""
    
    def getInfoCinema(self):
        # type: () -> str
        """
        Get Cinema informations. 

        :return: Cinema Information 
        """
        return ""
    
    def getInfoLottery(self):
        # type: () -> str
        """
        Get Lottery informations. 

        :return: Lottery Information 
        """
        return ""
    
    def getInfoOther(self):
        # type: () -> str
        """
        Get other informations. 

        :return: Other Information 
        """
        return ""
    
    def getEditorialStaff(self):
        # type: () -> str
        """
        Get Editorial Staff names. 

        :return: Editorial Staff 
        """
        return ""
    
    def getProgStation(self):
        # type: () -> str
        """
        Name describing station. 

        :return: Program Station 
        """
        return ""
    
    def getProgStyle(self):
        # type: () -> str
        """
        The the radio channel style currently used. 

        :return: Program Style 
        """
        return ""
    
    def getProgHost(self):
        # type: () -> str
        """
        Host of current radio show. 

        :return: Program Host 
        """
        return ""
    
    def getProgWebsite(self):
        # type: () -> str
        """
        Link to URL (web page) for radio station homepage. 

        :return: Program Website 
        """
        return ""
    
    def getProgNow(self):
        # type: () -> str
        """
        Current radio program show. 

        :return: Program Now 
        """
        return ""
    
    def getProgNext(self):
        # type: () -> str
        """
        Next program show. 

        :return: Program Next 
        """
        return ""
    
    def getPhoneHotline(self):
        # type: () -> str
        """
        Telephone number of the radio station's hotline. 

        :return: Phone Hotline 
        """
        return ""
    
    def getEMailHotline(self):
        # type: () -> str
        """
        Email address of the radio station's studio. 

        :return: EMail Hotline 
        """
        return ""
    
    def getPhoneStudio(self):
        # type: () -> str
        """
        Telephone number of the radio station's studio. 

        :return: Phone Studio 
        """
        return ""
    
    def getEMailStudio(self):
        # type: () -> str
        """
        Email address of radio station studio. 

        :return: EMail Studio 
        """
        return ""
    
    def getSMSStudio(self):
        # type: () -> str
        """
        SMS (Text Messaging) number for studio. 

        :return: SMS Studio 
        """
        return ""
    
