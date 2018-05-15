
class Monitor(object):
    """
    Kodi's monitor class

    Creates a new monitor to notify addon about changes.
    """
    
    def __init__(self):
        # type: () -> None
        pass
    
    def onSettingsChanged(self):
        # type: () -> None
        """
        onSettingsChanged method. 

        Will be called when addon settings are changed 
        """
        pass
    
    def onScreensaverActivated(self):
        # type: () -> None
        """
        onScreensaverActivated method. 

        Will be called when screensaver kicks in 
        """
        pass
    
    def onScreensaverDeactivated(self):
        # type: () -> None
        """
        onScreensaverDeactivated method. 

        Will be called when screensaver goes off 
        """
        pass
    
    def onDPMSActivated(self):
        # type: () -> None
        """
        onDPMSActivated method. 

        Will be called when energysaving/DPMS gets active 
        """
        pass
    
    def onDPMSDeactivated(self):
        # type: () -> None
        """
        onDPMSDeactivated method. 

        Will be called when energysaving/DPMS is turned off 
        """
        pass
    
    def onScanStarted(self, library):
        # type: (str_type) -> None
        """
        onScanStarted method. 

        :param library: Video / music as string

        Will be called when library clean has ended and return video or music
        to indicate which library is being scanned

        New function added. 
        """
        pass
    
    def onScanFinished(self, library):
        # type: (str_type) -> None
        """
        onScanFinished method. 

        :param library: Video / music as string

        Will be called when library clean has ended and return video or music
        to indicate which library has been scanned

        New function added. 
        """
        pass
    
    def onDatabaseScanStarted(self, database):
        # type: (str_type) -> None
        """
        .. warning:: Deprecated. Use **onScanStarted()**.
        """
        pass
    
    def onDatabaseUpdated(self, database):
        # type: (str_type) -> None
        """
        .. warning:: Deprecated. Use **onScanFinished()**.
        """
        pass
    
    def onCleanStarted(self, library):
        # type: (str_type) -> None
        """
        onCleanStarted method.

        :param library: Video / music as string

        Will be called when library clean has ended and return video or music
        to indicate which library has been cleaned

        New function added. 
        """
        pass
    
    def onCleanFinished(self, library):
        # type: (str_type) -> None
        """
        onCleanFinished method. 

        :param library: Video / music as string

        Will be called when library clean has ended and return video or music
        to indicate which library has been finished

        New function added. 
        """
        pass
    
    def onAbortRequested(self):
        # type: () -> None
        """
        .. warning::
            Deprecated. Use **waitForAbort()** to be notified about this event.
        """
        pass
    
    def onNotification(self, sender, method, data):
        # type: (str_type, str_type, str_type) -> None
        """
        ``onNotification(sender, method, data`` 

        onNotification method. 

        :param sender: Sender of the notification 
        :param method: Name of the notification 
        :param data: JSON-encoded data of the notification

        Will be called when Kodi receives or sends a notification 

        New function added. 
        """
        pass
    
    def waitForAbort(self, timeout=-1):
        # type: (float) -> bool
        """
        Wait for Abort 

        Block until abort is requested, or until timeout occurs. If an abort
        requested have already been made, return immediately.

        :param timeout: [opt] float - timeout in seconds. Default: no timeout. 
        :return: True when abort have been requested, False if a timeout
            is given and the operation times out.

        New function added. 
        """
        return True
    
    def abortRequested(self):
        # type: () -> bool
        """
        Returns True if abort has been requested. 

        True if requested 

        New function added. 
        """
        return True
 