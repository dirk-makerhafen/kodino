from xbmcgui_Constants import *
from xbmcgui_Control import *

class Window(object):
    """
    GUI window class for Add-Ons

    This class allows over their functions to create and edit windows that
    can be accessed from an Add-On.

    Likewise, all functions from here as well in the other window classes
    WindowDialog, WindowXML and WindowXMLDialog with inserted and available.

    Constructor for window 

    ``xbmcgui.Window([existingWindowId]):``

    Creates a new from Add-On usable window class. This is to create window
    for related controls by system calls.

    :param existingWindowId: [opt] Specify an id to use an existing window. 
    :raises ValueError: if supplied window Id does not exist. 
    :raises Exception: if more then 200 windows are created.

    Deleting this window will activate the old window that was active and resets
    (not delete) all controls that are associated with this window.

    Example::

        ..
        win = xbmcgui.Window()
        width = win.getWidth()
        ..
    """
    
    def __init__(self, existingWindowId=-1):
        # type: (int) -> None
        self.controls = {}
        self.X_MARGIN = 0
        self.Y_MARGIN = 0
        self.X_SHIFT = 0
        self.Y_SHIFT = 0
        self.HEADER_HEIGHT = 10
        self.background = Control()
        self.title_background = Control()
        self.title_bar = Control()
        self.window_close_button = Control()
        self.actions_connected = []
        self.controls_connected = []
        
    
    def show(self):
        # type: () -> None
        """
        Show this window. 

        Shows this window by activating it, calling close() after it wil
        activate the current window again.

        If your script ends this window will be closed to. To show it forever,
        make a loop at the end of your script or use doModal() instead.
        """
        pass
    
    def setFocus(self, pControl):
        # type: (Control) -> None
        """
        Give the supplied control focus. 

        :param Control: Control class to focus 
        :raises TypeError: If supplied argument is not a Control type 
        :raises SystemError: On Internal error
        :raises RuntimeError: If control is not added to a window
        """
        pass
    
    def setFocusId(self, iControlId):
        # type: (int) -> None
        """
        Gives the control with the supplied focus. 

        :param ControlId: [integer] On skin defined id of control 
        :raises SystemError: On Internal error 
        :raises RuntimeError: If control is not added to a window
        """
        pass
    
    def getFocus(self):
        # type: () -> Control
        """
        Returns the control which is focused. 

        :return: Focused control class
        :raises SystemError: On Internal error 
        :raises RuntimeError: If no control has focus
        """
        return Control()
    
    def getFocusId(self):
        # type: () -> long
        """
        Returns the id of the control which is focused. 

        :return: Focused control id
        :raises SystemError: On Internal error 
        :raises RuntimeError: If no control has focus
        """
        return 0L
    
    def removeControl(self, pControl):
        # type: (Control) -> None
        """
        Removes the control from this window. 

        :param Control: Control class to remove 
        :raises TypeError: If supplied argument is not a Control type 
        :raises RuntimeError: If control is not added to this window

        This will not delete the control. It is only removed from the window. 
        """
        pass
    
    def removeControls(self, pControls):
        # type: (List[Control]) -> None
        """
        Removes a list of controls from this window. 

        :param List: List with controls to remove 
        :raises TypeError: If supplied argument is not a Control type 
        :raises RuntimeError: If control is not added to this window

        This will not delete the controls. They are only removed from the window. 
        """
        pass
    
    def getHeight(self):
        # type: () -> long
        """
        Returns the height of this screen. 

        :return: Screen height 
        """
        return 0L
    
    def getWidth(self):
        # type: () -> long
        """
        Returns the width of this screen. 

        :return: Screen width 
        """
        return 0L
    
    def getResolution(self):
        # type: () -> long
        """
        Returns The resolution of the screen 

        :return: Used Resolution The returned value is one of the following:

        ======  =====================
        value   Resolution           
        ======  =====================
        0       1080i (1920x1080)    
        1       720p (1280x720)      
        2       480p 4:3 (720x480)   
        3       480p 16:9 (720x480)  
        4       NTSC 4:3 (720x480)   
        5       NTSC 16:9 (720x480)  
        6       PAL 4:3 (720x576)    
        7       PAL 16:9 (720x576)   
        8       PAL60 4:3 (720x480)  
        9       PAL60 16:9 (720x480) 
        ======  =====================
        """
        return 0L
    
    def setCoordinateResolution(self, res):
        # type: (int_type) -> None
        """
        Sets the resolution 

        That the coordinates of all controls are defined in. Allows Kodi
        to scale control positions and width/heights to whatever resolution
        Kodi is currently using.

        :param res: Coordinate resolution to set Resolution is one of the following:

        ======  =====================
        value   Resolution           
        ======  =====================
        0       1080i (1920x1080)    
        1       720p (1280x720)      
        2       480p 4:3 (720x480)   
        3       480p 16:9 (720x480)  
        4       NTSC 4:3 (720x480)   
        5       NTSC 16:9 (720x480)  
        6       PAL 4:3 (720x576)    
        7       PAL 16:9 (720x576)   
        8       PAL60 4:3 (720x480)  
        9       PAL60 16:9 (720x480) 
        ======  =====================

        Example::

            ..
            win = xbmcgui.Window(xbmcgui.getCurrentWindowId())
            win.setCoordinateResolution(0)
            ..
        """
        pass
    
    def setProperty(self, key, value):
        # type: (str, str_type) -> None
        """
        Sets a window property, similar to an infolabel. 

        :param key: string - property name. 
        :param value: string or unicode - value of property.

        Key is NOT case sensitive. Setting value to an empty string is equivalent
        to clearProperty(key). You can use the above as keywords for arguments
        and skip certain optional arguments. Once you use a keyword,
        all following arguments require the keyword.

        Example::

            ..
            win = xbmcgui.Window(xbmcgui.getCurrentWindowId())
            win.setProperty('Category', 'Newest')
            ..
        """
        pass
    
    def getProperty(self, key):
        # type: (str) -> str
        """
        Returns a window property as a string, similar to an infolabel. 

        :param key: string - property name.

        Key is NOT case sensitive. You can use the above as keywords for
        arguments and skip certain optional arguments. Once you use a keyword,
        all following arguments require the keyword.

        Example::

            ..
            win = xbmcgui.Window(xbmcgui.getCurrentWindowId())
            category = win.getProperty('Category')
            ..
        """
        return ""
    
    def clearProperty(self, key):
        # type: (str) -> None
        """
        Clears the specific window property. 

        :param key: string - property name.

        Key is NOT case sensitive. Equivalent to setProperty(key,''). You can use
        the above as keywords for arguments and skip certain optional arguments.
        Once you use a keyword, all following arguments require the keyword.

        Example::

            ..
            win = xbmcgui.Window(xbmcgui.getCurrentWindowId())
            win.clearProperty('Category')
            ..
        """
        pass
    
    def clearProperties(self):
        # type: () -> None
        """
        Clears all window properties. 

        Example::

            ..
            win = xbmcgui.Window(xbmcgui.getCurrentWindowId())
            win.clearProperties()
            ..
        """
        pass
    
    def close(self):
        # type: () -> None
        """
        Closes this window. 

        Closes this window by activating the old window.

        The window is not deleted with this method. 
        """
        pass
    
    def doModal(self):
        # type: () -> None
        """
        Display this window until close() is called.
        """
        pass
    
    def addControl(self, pControl):
        # type: (Control) -> None
        """
        Add a Control to this window. 

        :param Control: Control to add 
        :raises TypeError: If supplied argument is not a Control type 
        :raises ReferenceError: If control is already used in another window
        :raises RuntimeError: Should not happen :-)

        The next controls can be added to a window atm

        ==================  =============
        Control-class       Description  
        ==================  =============
        ControlLabel        Label control to show text
        ControlFadeLabel    The fadelabel has multiple labels which it cycles through
        ControlTextBox      To show bigger text field
        ControlButton       Brings a button to do some actions
        ControlEdit         The edit control allows a user to input text in Kodi
        ControlFadeLabel    The fade label control is used for displaying
                            multiple pieces of text in the same space in Kodi
        ControlList         Add a list for something like files
        ControlGroup        Is for a group which brings the others together
        ControlImage        Controls a image on skin
        ControlRadioButton  For a radio button which handle boolean values
        ControlProgress     Progress bar for a performed work or something else
        ControlSlider       The slider control is used for things where
                            a sliding bar best represents the operation at hand
        ControlSpin         The spin control is used for when a list of options
                            can be chosen
        ControlTextBox      The text box is used for showing a large multipage
                            piece of text in Kodi
        ==================  =============
        """
        self.controls[pControl.getId()] = pControl

    
    def addControls(self, pControls):
        # type: (List[Control]) -> None
        """
        Add a list of Controls to this window. 

        :param List: List with controls to add 
        :raises TypeError: If supplied argument is not of List type,
            or a control is not of Control type
        :raises ReferenceError: If control is already used in another window
        :raises RuntimeError: Should not happen :-)
        """
        for pControl in pControls:
            self.controls[pControl.getId()] = pControl
    
    def getControl(self, iControlId):
        print("getControl")
        # type: (int) -> Control
        """
        Gets the control from this window. 

        :param controlId: Control id to get 
        :raises Exception: If Control doesn't exist

        controlId doesn't have to be a python control, it can be a control
        id from a Kodi window too (you can find id's in the xml files.

        Not python controls are not completely usable yet You can only use
        the Control functions
        """
        print("getControl")
        print(iControlId)
        print(self.controls)
        # type: (int) -> Control
        if iControlId in self.controls:
            return self.controls[iControlId]
        return None
    

class WindowDialog(Window):
    """
    GUI window dialog class for Add-Ons

    ``xbmcgui.WindowDialog(int windowId):``

    Creates a new window from Add-On usable dialog class. This is to create
    window for related controls by system calls.

    :param windowId: [opt] Specify an id to use an existing window. 
    :raises ValueError: if supplied window Id does not exist. 
    :raises Exception: if more then 200 windows are created.

    Deleting this window will activate the old window that was active and resets
    (not delete) all controls that are associated with this window.

    Example::

        ..
        dialog = xbmcgui.WindowDialog()
        width = dialog.getWidth()
        ..
    """
    
    def __init__(self):
        # type: () -> None
        pass
    

class WindowXML(Window):
    """
    GUI xml window class

    Creates a new xml file based window class.

    This class include also all calls from ``Window``.

    :param xmlFilename: string - the name of the xml file to look for. 
    :param scriptPath: string - path to script. used to fallback to if the xml
        doesn't exist in the current skin.
        (eg xbmcaddon.Addon().getAddonInfo('path').decode('utf-8'))
    :param defaultSkin: [opt] string - name of the folder in the skins path
        to look in for the xml. (default='Default')
    :param defaultRes: [opt] string - default skins resolution. (default='720p') 
    :raises Exception: if more then 200 windows are created.

    Skin folder structure is e.g. **resources/skins/Default/720p**

    Deleting this window will activate the old window that was active and resets
    (not delete) all controls that are associated with this window.

    Example::

        ..
        win = xbmcgui.WindowXML('script-Lyrics-main.xml',
                xbmcaddon.Addon().getAddonInfo('path').decode('utf-8'),
                'default', '1080p')
        win.doModal()
        del win
        ..

    On functions defined input variable **
    ``controlId`` (GUI control identifier)** is the on window.xml defined value
    behind type added with  ``**id="..."**`` and used to identify for changes
    there and on callbacks.

    .. code-block:: xml

        <control type="label" id="31">
          <description>Title Label</description>
          ...
        </control>
        <control type="progress" id="32">
          <description>progress control</description>
          ...
        </control>
    """
    
    def __init__(self, xmlFilename, scriptPath, defaultSkin="Default",
                 defaultRes="720p"):
        # type: (str_type, str_type, str_type, str_type) -> None
        pass
    
    def addItem(self, item, position=INT_MAX):
        # type: (Union[str_type, ListItem], int) -> None
        """
        Add a new item to this WindowList. 

        :param item: string, unicode or ListItem - item to add. 
        :param position: [opt] integer - position of item to add.
            (NO Int = Adds to bottom,0 adds to top, 1 adds to one below from top,
            -1 adds to one above from bottom etc etc ). If integer positions are
            greater than list size, negative positions will add to top of list,
            positive positions will add to bottom of list

        Example::

            ..
            self.addItem('Reboot Kodi', 0)
            ..
        """
        pass
    
    def addItems(self, items):
        # type: (List[Union[str_type, ListItem]]) -> None
        """
        Add a list of items to to the window list. 

        :param items: List - list of strings, unicode objects or ListItems to add.

        Example::

            ..
            self.addItems(['Reboot Kodi', 'Restart Kodi'])
            ..
        """
        pass
    
    def removeItem(self, position):
        # type: (int) -> None
        """
        Removes a specified item based on position, from the WindowList. 

        :param position: integer - position of item to remove.

        Example::

            ..
            self.removeItem(5)
            ..
        """
        pass
    
    def getCurrentListPosition(self):
        # type: () -> int
        """
        Gets the current position in the WindowList.

        Example::

            ..
            pos = self.getCurrentListPosition()
            ..
        """
        return 0
    
    def setCurrentListPosition(self, position):
        # type: (int) -> None
        """
        Set the current position in the WindowList. 

        :param position: integer - position of item to set.

        Example::

            ..
            self.setCurrentListPosition(5)
            ..
        """
        pass
    
    def getListItem(self, position):
        # type: (int) -> ListItem
        """
        Returns a given ListItem in this WindowList. 

        :param position: integer - position of item to return.

        Example::

            ..
            listitem = self.getListItem(6)
            ..
        """
        return ListItem()
    
    def getListSize(self):
        # type: () -> int
        """
        Returns the number of items in this WindowList.

        Example::

            ..
            listSize = self.getListSize()
            ..
        """
        return 0
    
    def clearList(self):
        # type: () -> None
        """
        Clear the WindowList. 

        Example::

            ..
            self.clearList()
            ..
        """
        pass
    
    def setContainerProperty(self, strProperty, strValue):
        # type: (str_type, str_type) -> None
        """
        Sets a container property, similar to an infolabel. 

        :param key: string - property name. 
        :param value: string or unicode - value of property.

        Key is NOT case sensitive. You can use the above as keywords for arguments
        and skip certain optional arguments. Once you use a keyword,
        all following arguments require the keyword.

        Changed function from **setProperty** to **setContainerProperty**.

        Example::

            ..
            self.setContainerProperty('Category', 'Newest')
            ..
        """
        pass
    
    def getCurrentContainerId(self):
        # type: () -> int
        """
        Get the id of the currently visible container. 

        Added new function.

        Example::

            ..
            container_id = self.getCurrentContainerId()
            ..
        """
        return 0
    

class WindowXMLDialog(WindowXML):
    """
    GUI xml window dialog

    Creates a new xml file based window dialog class.

    :param xmlFilename: string - the name of the xml file to look for. 
    :param scriptPath: string - path to script. used to fallback to if the xml
        doesn't exist in the current skin.
        (eg xbmcaddon.Addon().getAddonInfo('path').decode('utf-8'))
    :param defaultSkin: [opt] string - name of the folder in the skins path
        to look in for the xml. (default='Default')
    :param defaultRes: [opt] string - default skins resolution.
        (default='720p')
    :raises Exception: if more then 200 windows are created.

    Skin folder structure is e.g. **resources/skins/Default/720p**

    Example::

        ..
        dialog = xbmcgui.WindowXMLDialog('script-Lyrics-main.xml',
            xbmcaddon.Addon().getAddonInfo('path').decode('utf-8'),
            'default', '1080p')
        dialog.doModal()
        del dialog
        ..

    On functions defined input variable ** ``controlId``
    (GUI control identifier)** is the on window.xml defined value behind type
    added with  ``**id="..."**`` and used to identify for changes there and
    on callbacks.

    .. code-block:: xml

        <control type="label" id="31">
          <description>Title Label</description>
          ...
        </control>
        <control type="progress" id="32">
          <description>progress control</description>
          ...
        </control>
    """
    
    def __init__(self, xmlFilename, scriptPath, defaultSkin="Default", defaultRes="720p"):
        # type: (str_type, str_type, str_type, str_type) -> None
        pass
    
