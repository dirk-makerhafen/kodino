
class RenderCapture(object):
    """
    Kodi's render capture.

    ``RenderCapture()``
    """
    
    def __init__(self):
        # type: () -> None
        pass
    
    def getWidth(self):
        # type: () -> int
        """
        Get width 

        To get width of captured image as set during RenderCapture.capture().
        Returns 0 prior to calling capture.

        :return: Width or 0 prior to calling capture 
        """
        return 0
    
    def getHeight(self):
        # type: () -> int
        """
        Get height 

        To get height of captured image as set during RenderCapture.capture().
        Returns 0 prior to calling capture.

        :return: height or 0 prior to calling capture 
        """
        return 0
    
    def getAspectRatio(self):
        # type: () -> float
        """
        Get aspect ratio of currently displayed video. 

        :return: Aspect ratio 

        This may be called prior to calling RenderCapture.capture(). 
        """
        return 0.0
    
    def getImageFormat(self):
        # type: () -> str
        """
        Get image format 

        Format of captured image: 'BGRA' 

        Image will now always be returned in BGRA 
        """
        return ""
    
    def getImage(self, msecs=0):
        # type: (int) -> bytearray
        """
        Returns captured image as a bytearray. 

        :param msecs: [opt] Milliseconds to wait. Waits 1000ms if not specified 
        :return: Captured image as a bytearray

        The size of the image is m_width * m_height * 4 

        Added the option to specify wait time in msec. 
        """
        return bytearray()
    
    def capture(self, width, height):
        # type: (int, int) -> None
        """
        Issue capture request. 

        :param width: Width capture image should be rendered to height.
        :param height: Height capture image should should be rendered to

        Removed the option to pass **flags**
        """
        pass
