import json, redis

keyboardUsageCount = 0        

import settings
import xbmcWrapperCommon

redis_connection = redis.StrictRedis(host=settings.REDIS_HOST, port= settings.REDIS_PORT,db= settings.REDIS_DB)


def countKeyboardUsage():
    global keyboardUsageCount
    keyboardUsageCount += 1
    if keyboardUsageCount > 10:
        raise Exception("keyboard loop interrupted")


class Keyboard(object):
    """
    Kodi's keyboard class

    Creates a new Keyboard object with default text heading and hidden input
    flag if supplied.

    :param default: : [opt] string - default text entry. 
    :param heading: : [opt] string - keyboard heading. 
    :param hidden: : [opt] boolean - True for hidden text entry.

    Example::

        ..
        kb = xbmc.Keyboard('default', 'heading', True)
        kb.setDefault('password') # optional
        kb.setHeading('Enter password') # optional
        kb.setHiddenInput(True) # optional
        kb.doModal()
        if (kb.isConfirmed()):
            text = kb.getText()
        ..
    """
    
    def __init__(self, line="", heading="", hidden=False):
        # type: (str_type, str_type, bool) -> None
        countKeyboardUsage()

    
    def doModal(self, autoclose=0):
        # type: (int) -> None
        """
        Show keyboard and wait for user action. 

        :param autoclose: [opt] integer - milliseconds to autoclose dialog.
            (default=do not autoclose)

        Example::

            ..
            kb.doModal(30000)
            ..
        """
        countKeyboardUsage()
    
    def setDefault(self, line=""):
        # type: (str_type) -> None
        """
        Set the default text entry. 

        :param line: string - default text entry.

        Example::

            ..
            kb.setDefault('password')
            ..
        """
        pass
    
    def setHiddenInput(self, hidden=False):
        # type: (bool) -> None
        """
        Allows hidden text entry. 

        :param hidden: boolean - True for hidden text entry.

        Example::

            ..
            kb.setHiddenInput(True)
            ..
        """
        countKeyboardUsage()

    
    def setHeading(self, heading):
        # type: (str_type) -> None
        """
        Set the keyboard heading. 

        :param heading: string - keyboard heading.

        Example::

            ..
            kb.setHeading('Enter password')
            ..
        """
        pass
    
    def getText(self):
        # type: () -> str
        """
        Returns the user input as a string. 

        This will always return the text entry even if you cancel the keyboard.
        Use the isConfirmed() method to check if user cancelled the keyboard.

        :return: get the in keyboard entered text

        Example::

            ..
            text = kb.getText()
            ..
        """
        countKeyboardUsage()
        input = redis_connection.get("%s:keyboard" % xbmcWrapperCommon.CURRENT_QUEUE)
        if input != None:
            return input
        redis_connection.rpush(xbmcWrapperCommon.CURRENT_QUEUE,json.dumps({"key": "Keyboard:getText" }))
        print("No keyboard input supplied")
        return ""
    
    def isConfirmed(self):
        # type: () -> bool
        """
        Returns False if the user cancelled the input. 

        :return: true if confirmed, if cancelled false 

        Example::

            ..
            if (kb.isConfirmed()):
              ..
        """
        countKeyboardUsage()
        return True