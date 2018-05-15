from xbmcgui_Constants import *


class Control(object):
    """
    Code based skin access

    Offers classes and functions that manipulate the add-on gui controls. 

    **Code based skin access.**

    Kodi is noted as having a very flexible and robust framework for its GUI,
    making theme-skinning and personal customization very accessible.
    Users can create their own skin (or modify an existing skin) and share it
    with others.

    Kodi includes a new GUI library written from scratch. This library allows
    you to skin/change everything you see in Kodi, from the images, the sizes
    and positions of all controls, colours, fonts, and text, through to altering
    navigation and even adding new functionality. The skin system is quite
    complex, and this portion of the manual is dedicated to providing in depth
    information on how it all works, along with tips to make the experience
    a little more pleasant.
    """
    
    def __init__(self):
        # type: () -> None
        pass
    
    def getId(self):
        # type: () -> int
        """
        Returns the control's current id as an integer. 

        :return: int - Current id

        Example::

            ...
            id = self.button.getId()
            ...
        """
        return id(self)
    
    def getX(self):
        # type: () -> int
        """
        Returns the control's current X position. 

        :return: int - Current X position

        Example::

            ...
            posX = self.button.getX()
            ...
        """
        return 0
    
    def getY(self):
        # type: () -> int
        """
        Returns the control's current Y position. 

        :return: int - Current Y position

        Example::

            ...
            posY = self.button.getY()
            ...
        """
        return 0
    
    def getHeight(self):
        # type: () -> int
        """
        Returns the control's current height as an integer. 

        :return: int - Current height

        Example::

            ...
            height = self.button.getHeight()
            ...
        """
        return 0
    
    def getWidth(self):
        # type: () -> int
        """
        Returns the control's current width as an integer. 

        :return: int - Current width

        Example::

            ...
            width = self.button.getWidth()
            ...
        """
        return 0
    
    def setEnabled(self, enabled):
        # type: (bool) -> None
        """
        Set's the control's enabled/disabled state. 

        :param enabled: bool - True=enabled / False=disabled.

        Example::

            ...
            self.button.setEnabled(False)
            ...
        """
        pass
    
    def setVisible(self, visible):
        # type: (bool) -> None
        """
        Set's the control's visible/hidden state. 

        :param visible: bool - True=visible / False=hidden.

        Example::

            ...
            self.button.setVisible(False)
            ...
        """
        pass
    
    def setVisibleCondition(self, visible, allowHiddenFocus=False):
        # type: (str, bool) -> None
        """
        Set's the control's visible condition. 

        Allows Kodi to control the visible status of the control.

        List of Conditions

        :param visible: string - Visible condition 
        :param allowHiddenFocus: [opt] bool - True=gains focus even if hidden

        Example::

            ...
            # setVisibleCondition(visible[,allowHiddenFocus])
            self.button.setVisibleCondition('[Control.IsVisible(41) + !Control.IsVisible(12)]', True)
            ...
        """
        pass
    
    def setEnableCondition(self, enable):
        # type: (str) -> None
        """
        Set's the control's enabled condition. 

        Allows Kodi to control the enabled status of the control.

        List of Conditions

        :param enable: string - Enable condition.

        Example::

            ...
            # setEnableCondition(enable)
            self.button.setEnableCondition('System.InternetState')
            ...
        """
        pass
    
    def setAnimations(self, eventAttr):
        # type: (List[Tuple[str_type, str_type]]) -> None
        """
        Set's the control's animations. 

        **[(event,attr,)*]**: list - A list of tuples consisting of event
        and attributes pairs.

        Animating your skin

        :param event: string - The event to animate. 
        :param attr: string - The whole attribute string separated by spaces.

        Example::

            ...
            # setAnimations([(event, attr,)*])
            self.button.setAnimations([('focus', 'effect=zoom end=90,247,220,56 time=0',)])
            ...
        """
        pass
    
    def setPosition(self, x, y):
        # type: (int_type, int_type) -> None
        """
        Set's the controls position. 

        :param x: integer - x coordinate of control. 
        :param y: integer - y coordinate of control.

        You may use negative integers. (e.g sliding a control into view)

        Example::

            ...
            self.button.setPosition(100, 250)
            ...
        """
        pass
    
    def setWidth(self, width):
        # type: (int_type) -> None
        """
        Set's the controls width. 

        :param width: integer - width of control.

        Example::

            ...
            self.image.setWidth(100)
            ...
        """
        pass
    
    def setHeight(self, height):
        # type: (int_type) -> None
        """
        Set's the controls height. 

        :param height: integer - height of control.

        Example::

            ...
            self.image.setHeight(100)
            ...
        """
        pass
    
    def setNavigation(self, up, down, left, right):
        # type: (Control, Control, Control, Control) -> None
        """
        Set's the controls navigation. 

        :param up: control object - control to navigate to on up. 
        :param down: control object - control to navigate to on down. 
        :param left: control object - control to navigate to on left. 
        :param right: control object - control to navigate to on right. 
        :raises TypeError: if one of the supplied arguments is not a control type. 
        :raises ReferenceError: if one of the controls is not added to a window.

        Same as controlUp(), controlDown(), controlLeft(), controlRight().
        Set to self to disable navigation for that direction.

        Example::

            ...
            self.button.setNavigation(self.button1, self.button2, self.button3, self.button4)
            ...
        """
        pass
    
    def controlUp(self, up):
        # type: (Control) -> None
        """
        Set's the controls up navigation. 

        :param control: control object - control to navigate to on up. 
        :raises TypeError: if one of the supplied arguments is not a control type. 
        :raises ReferenceError: if one of the controls is not added to a window.

        You can also use setNavigation(). Set to self to disable navigation.

        Example::

            ...
            self.button.controlUp(self.button1)
            ...
        """
        pass
    
    def controlDown(self, control):
        # type: (Control) -> None
        """
        Set's the controls down navigation. 

        :param control: control object - control to navigate to on down. 
        :raises TypeError: if one of the supplied arguments is not a control type. 
        :raises ReferenceError: if one of the controls is not added to a window.

        You can also use setNavigation(). Set to self to disable navigation.

        Example::

            ...
            self.button.controlDown(self.button1)
            ...
        """
        pass
    
    def controlLeft(self, control):
        # type: (Control) -> None
        """
        Set's the controls left navigation. 

        :param control: control object - control to navigate to on left. 
        :raises TypeError: if one of the supplied arguments is not a control type. 
        :raises ReferenceError: if one of the controls is not added to a window.

        You can also use setNavigation(). Set to self to disable navigation.

        Example::

            ...
            self.button.controlLeft(self.button1)
            ...
        """
        pass
    
    def controlRight(self, control):
        # type: (Control) -> None
        """
        Set's the controls right navigation. 

        :param control: control object - control to navigate to on right. 
        :raises TypeError: if one of the supplied arguments is not a control type. 
        :raises ReferenceError: if one of the controls is not added to a window.

        You can also use setNavigation(). Set to self to disable navigation.

        Example::

            ...
            self.button.controlRight(self.button1)
            ...
        """
        pass
    

class ControlSpin(Control):
    """
    Used for cycling up/down controls

    Offers classes and functions that manipulate the add-on gui controls. 

    **Code based skin access.**

    The spin control is used for when a list of options can be chosen
    (such as a page up/down control). You can choose the position, size,
    and look of the spin control.

    This class include also all calls from Control

    .. warning::
        **Not working yet**. You can't create this object, it is returned
        by objects like ControlTextBox and ControlList.
    """
    
    def __init__(self):
        # type: () -> None
        pass
    
    def setTextures(self, up, down, upFocus, downFocus, upDisabled, downDisabled):
        # type: (str, str, str, str, str, str) -> None
        """
        Set's textures for this control. 

        Texture are image files that are used for example in the skin

        .. warning:: **Not working yet**.

        :param up: label - for the up arrow when it doesn't have focus. 
        :param down: label - for the down button when it is not focused. 
        :param upFocus: label - for the up button when it has focus. 
        :param downFocus: label - for the down button when it has focus. 
        :param upDisabled: label - for the up arrow when the button is disabled. 
        :param downDisabled: label - for the up arrow when the button is disabled.

        Example::

            ...
            # setTextures(up, down, upFocus, downFocus, upDisabled, downDisabled)
            
            ...
        """
        pass
    

class ControlLabel(Control):
    """
    Used to show some lines of text

    The label control is used for displaying text in Kodi. You can choose
    the font, size, colour, location and contents of the text to be displayed.

    This class include also all calls from Control

    :param x: integer - x coordinate of control. 
    :param y: integer - y coordinate of control. 
    :param width: integer - width of control. 
    :param height: integer - height of control. 
    :param label: string or unicode - text string. 
    :param font: [opt] string - font used for label text. (e.g. 'font13') 
    :param textColor: [opt] hexstring - color of enabled label's label.
        (e.g. '0xFFFFFFFF')
    :param disabledColor: [opt] hexstring - color of disabled label's label.
        (e.g. '0xFFFF3300')
    :param alignment: [opt] integer - alignment of labelFlags for alignment
        used as bits to have several together:

    =================  ===========  ===============
    Defination name    Bitflag      Description    
    =================  ===========  ===============
    XBFONT_LEFT        0x00000000   Align X left   
    XBFONT_RIGHT       0x00000001   Align X right  
    XBFONT_CENTER_X    0x00000002   Align X center 
    XBFONT_CENTER_Y    0x00000004   Align Y center 
    XBFONT_TRUNCATED   0x00000008   Truncated text 
    XBFONT_JUSTIFIED   0x00000010   Justify text   
    =================  ===========  ===============

    :param hasPath: [opt] bool - True=stores a path / False=no path 
    :param angle: [opt] integer - angle of control.
        (**+** rotates CCW, **-** rotates CW)

    Example::

        ...
        # ControlLabel(x, y, width, height, label[, font, textColor,
        #              disabledColor, alignment, hasPath, angle])
        self.label = xbmcgui.ControlLabel(100, 250, 125, 75, 'Status', angle=45)
        ...
    """
    
    def __init__(self, x, y, width, height, label, font=None, textColor=None,
                 disabledColor=None, alignment=0, hasPath=False, angle=0):
        # type: (int_type, int_type, int_type, int_type, str_type, str, str, str, int_type, bool, int_type) -> None
        pass
    
    def getLabel(self):
        # type: () -> str
        """
        Returns the text value for this label. 

        :return: This label

        Example::

            ...
            label = self.label.getLabel()
            ...
        """
        return ""
    
    def setLabel(self, label="", font=None, textColor=None, disabledColor=None,
                 shadowColor=None, focusedColor=None, label2=""):
        # type: (str_type, str, str, str, str, str, str_type) -> None
        """
        Set's text for this label. 

        :param label: string or unicode - text string. 
        :param font: [opt] string - font used for label text. (e.g. 'font13') 
        :param textColor: [opt] hexstring - color of enabled label's label.
            (e.g. '0xFFFFFFFF')
        :param disabledColor: [opt] hexstring - color of disabled label's label.
            (e.g. '0xFFFF3300')
        :param shadowColor: [opt] hexstring - color of button's label's shadow.
            (e.g. '0xFF000000')
        :param focusedColor: [opt] hexstring - color of focused button's label.
            (e.g. '0xFF00FFFF')
        :param label2: [opt] string or unicode - text string.

        Example::

            ...
            self.label.setLabel('Status')
            ...
        """
        pass
    

class ControlEdit(Control):
    """
    Used as an input control for the osd keyboard and other input fields

    The edit control allows a user to input text in Kodi. You can choose
    the font, size, colour, location and header of the text to be displayed.

    This class include also all calls from Control

    :param x: integer - x coordinate of control. 
    :param y: integer - y coordinate of control. 
    :param width: integer - width of control. 
    :param height: integer - height of control. 
    :param label: string or unicode - text string. 
    :param font: [opt] string - font used for label text. (e.g. 'font13') 
    :param textColor: [opt] hexstring - color of enabled label's label.
        (e.g. '0xFFFFFFFF')
    :param disabledColor: [opt] hexstring - color of disabled label's label.
        (e.g. '0xFFFF3300')
    :param alignment: [opt] integer - alignment of labelFlags for alignment
        used as bits to have several together:

    =================  ===========  ===============
    Defination name    Bitflag      Description    
    =================  ===========  ===============
    XBFONT_LEFT        0x00000000   Align X left   
    XBFONT_RIGHT       0x00000001   Align X right  
    XBFONT_CENTER_X    0x00000002   Align X center 
    XBFONT_CENTER_Y    0x00000004   Align Y center 
    XBFONT_TRUNCATED   0x00000008   Truncated text 
    XBFONT_JUSTIFIED   0x00000010   Justify text   
    =================  ===========  ===============

    :param focusTexture: [opt] string - filename for focus texture. 
    :param noFocusTexture: [opt] string - filename for no focus texture. 
    :param isPassword: [opt] bool - True=mask text value with  ``****``.

    You can use the above as keywords for arguments and skip certain optional
    arguments. Once you use a keyword, all following arguments require
    the keyword. After you create the control, you need to add it to the window
    with addControl().

    Example::

        ...
        self.edit = xbmcgui.ControlEdit(100, 250, 125, 75, 'Status')
        ...
    """
    
    def __init__(self, x, y, width, height, label, font=None, textColor=None,
                 disabledColor=None, _alignment=0, focusTexture=None,
                 noFocusTexture=None, isPassword=False):
        # type: (int_type, int_type, int_type, int_type, str_type, str, str, str, int_type, str, str, bool) -> None
        pass
    
    def setLabel(self, label="", font=None, textColor=None, disabledColor=None,
                 shadowColor=None, focusedColor=None, label2=""):
        # type: (str_type, str, str, str, str, str, str_type) -> None
        """
        Set's text heading for this edit control. 

        :param label: string or unicode - text string. 
        :param font: [opt] string - font used for label text. (e.g. 'font13') 
        :param textColor: [opt] hexstring - color of enabled label's label.
            (e.g. '0xFFFFFFFF')
        :param disabledColor: [opt] hexstring - color of disabled label's label.
            (e.g. '0xFFFF3300')
        :param shadowColor: [opt] hexstring - color of button's label's shadow.
            (e.g. '0xFF000000')
        :param focusedColor: [opt] hexstring - color of focused button's label.
            (e.g. '0xFF00FFFF')
        :param label2: [opt] string or unicode - text string.

        Example::

            ...
            self.edit.setLabel('Status')
            ...
        """
        pass
    
    def getLabel(self):
        # type: () -> str
        """
        Returns the text heading for this edit control. 

        :return: Heading text

        Example::

            ...
            label = self.edit.getLabel()
            ...
        """
        return ""
    
    def setText(self, text):
        # type: (str_type) -> None
        """
        Set's text value for this edit control. 

        :param value: string or unicode - text string.

        Example::

            ...
            self.edit.setText('online')
            ...
        """
        pass
    
    def getText(self):
        # type: () -> str
        """
        Returns the text value for this edit control. 

        :return: Text value of control

        New function added.

        Example::

            ...
            value = self.edit.getText()
            ...
        """
        return ""
    

class ControlList(Control):
    """
    Used for a scrolling lists of items. Replaces the list control

    The list container is one of several containers used to display items from
    file lists in various ways. The list container is very flexible - it's only
    restriction is that it is a list - i.e. a single column or row of items.
    The layout of the items is very flexible and is up to the skinner.

    This class include also all calls from Control

    :param x: integer - x coordinate of control. 
    :param y: integer - y coordinate of control. 
    :param width: integer - width of control. 
    :param height: integer - height of control. 
    :param font: [opt] string - font used for items label. (e.g. 'font13') 
    :param textColor: [opt] hexstring - color of items label. (e.g. '0xFFFFFFFF') 
    :param buttonTexture: [opt] string - filename for focus texture. 
    :param buttonFocusTexture: [opt] string - filename for no focus texture. 
    :param selectedColor: [opt] integer - x offset of label. 
    :param imageWidth: [opt] integer - width of items icon or thumbnail. 
    :param imageHeight: [opt] integer - height of items icon or thumbnail. 
    :param itemTextXOffset: [opt] integer - x offset of items label. 
    :param itemTextYOffset: [opt] integer - y offset of items label. 
    :param itemHeight: [opt] integer - height of items. 
    :param space: [opt] integer - space between items.
    :param alignmentY: [opt] integer - Y-axis alignment of items labelFlags
        for alignment used as bits to have several together:

    =================  ===========  ===============
    Defination name    Bitflag      Description    
    =================  ===========  ===============
    XBFONT_LEFT        0x00000000   Align X left   
    XBFONT_RIGHT       0x00000001   Align X right  
    XBFONT_CENTER_X    0x00000002   Align X center 
    XBFONT_CENTER_Y    0x00000004   Align Y center 
    XBFONT_TRUNCATED   0x00000008   Truncated text 
    XBFONT_JUSTIFIED   0x00000010   Justify text   
    =================  ===========  ===============

    :param shadowColor: [opt] hexstring - color of items label's shadow.
        (e.g. '0xFF000000')

    You can use the above as keywords for arguments and skip certain optional
    arguments. Once you use a keyword, all following arguments require
    the keyword. After you create the control, you need to add it to the window
    with addControl().

    Example::

        ...
        self.cList = xbmcgui.ControlList(100, 250, 200, 250, 'font14', space=5)
        ...
    """
    
    def __init__(self, x, y, width, height, font=None, textColor=None,
                 buttonTexture=None, buttonFocusTexture=None,
                 selectedColor=None, _imageWidth=10, _imageHeight=10,
                 _itemTextXOffset=10, _itemTextYOffset=2, _itemHeight=27,
                 _space=2, _alignmentY=4):
        # type: (int_type, int_type, int_type, int_type, str, str, str, str, str, int_type, int_type, int_type, int_type, int_type, int_type, int_type) -> None
        pass
    
    def addItem(self, item, sendMessage=True):
        # type: (Union[str_type, ListItem], bool) -> None
        """
        Add a new item to this list control. 

        :param item: string, unicode or ListItem - item to add.

        Example::

            ...
            cList.addItem('Reboot Kodi')
            ...
        """
        pass
    
    def addItems(self, items):
        # type: (List[Union[str_type, ListItem]]) -> None
        """
        Adds a list of listitems or strings to this list control. 

        :param items: List - list of strings, unicode objects or ListItems to add.

        You can use the above as keywords for arguments.

        Large lists benefit considerably, than using the standard addItem()

        Example::

            ...
            cList.addItems(items=listitems)
            ...
        """
        pass
    
    def selectItem(self, item):
        # type: (int_type) -> None
        """
        Select an item by index number. 

        :param item: integer - index number of the item to select.

        Example::

            ...
            cList.selectItem(12)
            ...
        """
        pass
    
    def removeItem(self, index):
        # type: (int) -> None
        """
        Remove an item by index number. 

        :param index: integer - index number of the item to remove.

        New function added.

        Example::

            ...
            cList.removeItem(12)
            ...
        """
        pass
    
    def reset(self):
        # type: () -> None
        """
        Clear all ListItems in this control list. 

        Example::

            ...
            cList.reset()
            ...
        """
        pass
    
    def getSpinControl(self):
        # type: () -> Control
        """
        Returns the associated ControlSpin object.

        .. warning::
            Not working completely yet After adding this control list to
            a window it is not possible to change the settings
            of this spin control.

        Example::

            ...
            ctl = cList.getSpinControl()
            ...
        """
        return Control()
    
    def getSelectedPosition(self):
        # type: () -> long
        """
        Returns the position of the selected item as an integer.

        Returns -1 for empty lists.

        Example::

            ...
            pos = cList.getSelectedPosition()
            ...
        """
        return 0L
    
    def getSelectedItem(self):
        # type: () -> ListItem
        """
        Returns the selected item as a ListItem object. 

        :return: The selected item

        Same as getSelectedPosition(), but instead of an integer a ListItem
        object is returned. Returns None for empty lists.
        See windowexample.py on how to use this.

        Example::

            ...
            item = cList.getSelectedItem()
            ...
        """
        return ListItem()
    
    def setImageDimensions(self, imageWidth, imageHeight):
        # type: (int_type, int_type) -> None
        """
        Sets the width/height of items icon or thumbnail. 

        :param imageWidth: [opt] integer - width of items icon or thumbnail. 
        :param imageHeight: [opt] integer - height of items icon or thumbnail.

        Example::

            ...
            cList.setImageDimensions(18, 18)
            ...
        """
        pass
    
    def setSpace(self, space):
        # type: (int) -> None
        """
        Set's the space between items. 

        :param space: [opt] integer - space between items.

        Example::

            ...
            cList.setSpace(5)
            ...
        """
        pass
    
    def setPageControlVisible(self, visible):
        # type: (bool) -> None
        """
        Sets the spin control's visible/hidden state. 

        :param visible: boolean - True=visible / False=hidden.

        Example::

            ...
            cList.setPageControlVisible(True)
            ...
        """
        pass
    
    def size(self):
        # type: () -> long
        """
        Returns the total number of items in this list control as an integer.

        :return: Total number of items

        Example::

            ...
            cnt = cList.size()
            ...
        """
        return 0L
    
    def getItemHeight(self):
        # type: () -> long
        """
        Returns the control's current item height as an integer. 

        :return: Current item heigh

        Example::

            ..
            item_height = self.cList.getItemHeight()
            ...
        """
        return 0L
    
    def getSpace(self):
        # type: () -> long
        """
        Returns the control's space between items as an integer. 

        :return: Space between items

        Example::

            ...
            gap = self.cList.getSpace()
            ...
        """
        return 0L
    
    def getListItem(self, index):
        # type: (int) -> ListItem
        """
        Returns a given ListItem in this List. 

        :param index: integer - index number of item to return. 
        :return: List item
        :raises ValueError: if index is out of range.

        Example::

            ...
            listitem = cList.getListItem(6)
            ...
        """
        return ListItem()
    
    def setStaticContent(self, items):
        # type: (List[ListItem]) -> None
        """
        Fills a static list with a list of listitems. 

        :param items: List - list of listitems to add.

        You can use the above as keywords for arguments.

        Example::

            ...
            cList.setStaticContent(items=listitems)
            ...
        """
        pass
    

class ControlFadeLabel(Control):
    """
    Used to show multiple pieces of text in the same position, by fading
    from one to the other

    The fade label control is used for displaying multiple pieces of text in
    the same space in Kodi. You can choose the font, size, colour, location
    and contents of the text to be displayed. The first piece of information
    to display fades in over 50 frames, then scrolls off to the left. Once it is
    finished scrolling off screen, the second piece of information fades in and
    the process repeats. A fade label control is not supported in
    a list container.

    This class include also all calls from Control

    :param x: integer - x coordinate of control. 
    :param y: integer - y coordinate of control. 
    :param width: integer - width of control. 
    :param height: integer - height of control. 
    :param font: [opt] string - font used for label text. (e.g. 'font13') 
    :param textColor: [opt] hexstring - color of fadelabel's labels.
        (e.g. '0xFFFFFFFF')
    :param alignment: [opt] integer - alignment of labelFlags for alignment
        used as bits to have several together:

    =================  ===========  ===============
    Defination name    Bitflag      Description    
    =================  ===========  ===============
    XBFONT_LEFT        0x00000000   Align X left   
    XBFONT_RIGHT       0x00000001   Align X right  
    XBFONT_CENTER_X    0x00000002   Align X center 
    XBFONT_CENTER_Y    0x00000004   Align Y center 
    XBFONT_TRUNCATED   0x00000008   Truncated text 
    XBFONT_JUSTIFIED   0x00000010   Justify text   
    =================  ===========  ===============

    You can use the above as keywords for arguments and skip certain optional
    arguments. Once you use a keyword, all following arguments require
    the keyword. After you create the control, you need to add it to the window
    with addControl().

    Example::

        ...
        self.fadelabel = xbmcgui.ControlFadeLabel(100, 250, 200, 50, textColor='0xFFFFFFFF')
        ...
    """
    
    def __init__(self, x, y, width, height, font=None, textColor=None, _alignment=0):
        # type: (int_type, int_type, int_type, int_type, str, str, int_type) -> None
        pass
    
    def addLabel(self, label):
        # type: (str_type) -> None
        """
        Add a label to this control for scrolling. 

        :param label: string or unicode - text string to add.

        To remove added text use  ``reset()`` for them.

        Example::

            ...
            self.fadelabel.addLabel('This is a line of text that can scroll.')
            ...
        """
        pass
    
    def setScrolling(self, scroll):
        # type: (bool) -> None
        """
        Set scrolling. If set to false, the labels won't scroll. Defaults to true. 

        :param scroll: boolean - True = enabled / False = disabled

        Example::

            ...
            self.fadelabel.setScrolling(False)
            ...
        """
        pass
    

class ControlTextBox(Control):
    """
    Used to show a multi-page piece of text

    The text box is used for showing a large multipage piece of text in Kodi.
    You can choose the position, size, and look of the text.

    This class include also all calls from Control

    :param x: integer - x coordinate of control. 
    :param y: integer - y coordinate of control. 
    :param width: integer - width of control. 
    :param height: integer - height of control. 
    :param font: [opt] string - font used for text. (e.g. 'font13') 
    :param textColor: [opt] hexstring - color of textbox's text.
        (e.g. '0xFFFFFFFF')

    You can use the above as keywords for arguments and skip certain optional
    arguments. Once you use a keyword, all following arguments require
    the keyword. After you create the control, you need to add it to the window
    with addControl().

    Example::

        ...
        # ControlTextBox(x, y, width, height[, font, textColor])
        self.textbox = xbmcgui.ControlTextBox(100, 250, 300, 300, textColor='0xFFFFFFFF')
        ...
    """
    
    def __init__(self, x, y, width, height, font=None, textColor=None):
        # type: (int_type, int_type, int_type, int_type, str, str) -> None
        pass
    
    def setText(self, text):
        # type: (str_type) -> None
        """
        Set's the text for this textbox. 

        :param text: string or unicode - text string.

        Example::

            ...
            # setText(text)
            self.textbox.setText('This is a line of text that can wrap.')
            ...
        """
        pass
    
    def getText(self):
        # type: () -> str
        """
        Returns the text value for this textbox. 

        :return: To get text from box

        Example::

            ...
            # getText()
            text = self.text.getText()
            ...
        """
        return ""
    
    def reset(self):
        # type: () -> None
        """
        Clear's this textbox.

        Example::

            ...
            # reset()
            self.textbox.reset()
            ...
        """
        pass
    
    def scroll(self, id):
        # type: (int_type) -> None
        """
        Scrolls to the given position. 

        :param id: integer - position to scroll to.

        Example::

            ...
            # scroll(position)
            self.textbox.scroll(10)
            ...
        """
        pass
    
    def autoScroll(self, delay, time, repeat):
        # type: (int, int, int) -> None
        """
        Set autoscrolling times. 

        :param delay: integer - Scroll delay (in ms) 
        :param time: integer - Scroll time (in ms) 
        :param repeat: integer - Repeat time

        New function added.

        Example::

            ...
            self.textbox.autoScroll(1, 2, 1)
            ...
        """
        pass
    

class ControlImage(Control):
    """
    Used to show an image

    The image control is used for displaying images in Kodi. You can choose
    the position, size, transparency and contents of the image to be displayed.

    This class include also all calls from Control

    :param x: integer - x coordinate of control. 
    :param y: integer - y coordinate of control. 
    :param width: integer - width of control. 
    :param height: integer - height of control. 
    :param filename: string - image filename. 
    :param aspectRatio: [opt] integer - (values 0 = stretch (default),
        1 = scale up (crops), 2 = scale down (black bar)
    :param colorDiffuse: hexString - (example, '0xC0FF0000' (red tint))

    You can use the above as keywords for arguments and skip certain optional
    arguments. Once you use a keyword, all following arguments require
    the keyword. After you create the control, you need to add it to the window
    with addControl().

    Example::

        ...
        # ControlImage(x, y, width, height, filename[, aspectRatio, colorDiffuse])
        self.image = xbmcgui.ControlImage(100, 250, 125, 75, aspectRatio=2)
        ...
    """
    
    def __init__(self, x, y, width, height, filename, aspectRatio=0, colorDiffuse=None):
        # type: (int_type, int_type, int_type, int_type, str, int_type, str) -> None
        pass
    
    def setImage(self, imageFilename, useCache=True):
        # type: (str, bool) -> None
        """
        Changes the image. 

        :param filename: string - image filename. 
        :param useCache: [opt] bool - True=use cache (default) /
            False=don't use cache.

        Added new option **useCache**.

        Example::

            ...
            # setImage(filename[, useCache])
            self.image.setImage('special://home/scripts/test.png')
            self.image.setImage('special://home/scripts/test.png', False)
            ...
        """
        pass
    
    def setColorDiffuse(self, hexString):
        # type: (str) -> None
        """
        Changes the images color. 

        :param colorDiffuse: hexString - (example, '0xC0FF0000' (red tint))

        Example::

            ...
            # setColorDiffuse(colorDiffuse)
            self.image.setColorDiffuse('0xC0FF0000')
            ...
        """
        pass
    

class ControlProgress(Control):
    """
    Used to show the progress of a particular operation

    The progress control is used to show the progress of an item that may take
    a long time, or to show how far through a movie you are. You can choose
    the position, size, and look of the progress control.

    This class include also all calls from Control

    :param x: integer - x coordinate of control. 
    :param y: integer - y coordinate of control. 
    :param width: integer - width of control. 
    :param height: integer - height of control. 
    :param filename: string - image filename. 
    :param texturebg: [opt] string - specifies the image file whichshould
        be displayed in the background of the progress control.
    :param textureleft: [opt] string - specifies the image file whichshould
        be displayed for the left side of the progress bar. This is rendered on the left side of the bar.
    :param texturemid: [opt] string - specifies the image file which should
        be displayed for the middl portion of the progress bar. This is the  ``fill`` texture used to fill up the bar. It's positioned on the right of the  ``<lefttexture>`` texture, and fills the gap between the  ``<lefttexture>`` and  ``<righttexture>`` textures, depending on how far progressed the item is.
    :param textureright: [opt] string - specifies the image file which
        should be displayed for the right side of the progress bar.
        This is rendered on the right side of the bar.
    :param textureoverlay: [opt] string - specifies the image file which
        should be displayed over the top of all other images in the progress bar.
        It is centered vertically and horizontally within the space taken up
        by the background image.

    You can use the above as keywords for arguments and skip certain optional
    arguments. Once you use a keyword, all following arguments require the keyword.
    After you create the control, you need to add it to the window with addControl().

    Example::

        ...
        # ControlProgress(x, y, width, height, filename[, texturebg, textureleft,
        # texturemid, textureright, textureoverlay])
        self.image = xbmcgui.ControlProgress(100, 250, 250, 30,
                                             'special://home/scripts/test.png')
        ...
    """
    
    def __init__(self, x, y, width, height, texturebg=None, textureleft=None,
                 texturemid=None, textureright=None, textureoverlay=None):
        # type: (int_type, int_type, int_type, int_type, str, str, str, str, str) -> None
        pass
    
    def setPercent(self, pct):
        # type: (float) -> None
        """
        Sets the percentage of the progressbar to show. 

        :param percent: float - percentage of the bar to show.

        valid range for percent is 0-100

        Example::

            ...
            # setPercent(percent)
            self.progress.setPercent(60)
            ...
        """
        pass
    
    def getPercent(self):
        # type: () -> float
        """
        Returns a float of the percent of the progress. 

        :return: Percent position

        Example::

            ...
            # getPercent()
            print self.progress.getPercent()
            ...
        """
        return 0.0
    

class ControlButton(Control):
    """
    A standard push button control

    The button control is used for creating push buttons in Kodi. You can
    choose the position, size, and look of the button, as well as choosing
    what action(s) should be performed when pushed.

    This class include also all calls from Control

    :param x: integer - x coordinate of control. 
    :param y: integer - y coordinate of control. 
    :param width: integer - width of control. 
    :param height: integer - height of control. 
    :param label: string or unicode - text string. 
    :param focusTexture: [opt] string - filename for focus texture. 
    :param noFocusTexture: [opt] string - filename for no focus texture. 
    :param textOffsetX: [opt] integer - x offset of label. 
    :param textOffsetY: [opt] integer - y offset of label. 
    :param alignment: [opt] integer - alignment of labelFlags for alignment
        used as bits to have several together:

    =================  ===========  ===============
    Defination name    Bitflag      Description    
    =================  ===========  ===============
    XBFONT_LEFT        0x00000000   Align X left   
    XBFONT_RIGHT       0x00000001   Align X right  
    XBFONT_CENTER_X    0x00000002   Align X center 
    XBFONT_CENTER_Y    0x00000004   Align Y center 
    XBFONT_TRUNCATED   0x00000008   Truncated text 
    XBFONT_JUSTIFIED   0x00000010   Justify text   
    =================  ===========  ===============

    :param font: [opt] string - font used for label text. (e.g. 'font13') 
    :param textColor: [opt] hexstring - color of enabled button's label.
        (e.g. '0xFFFFFFFF')
    :param disabledColor: [opt] hexstring - color of disabled button's label.
        (e.g. '0xFFFF3300')
    :param angle: [opt] integer - angle of control. (+ rotates CCW, - rotates CW) 
    :param shadowColor: [opt] hexstring - color of button's label's shadow.
        (e.g. '0xFF000000')
    :param focusedColor: [opt] hexstring - color of focused button's label.
        (e.g. '0xFF00FFFF')

    You can use the above as keywords for arguments and skip certain optional
    arguments. Once you use a keyword, all following arguments require
    the keyword. After you create the control, you need to add it to the window
    with addControl().

    Example::

        ...
        # ControlButton(x, y, width, height, label[, focusTexture, noFocusTexture, textOffsetX, textOffsetY,
        #               alignment, font, textColor, disabledColor, angle, shadowColor, focusedColor])
        self.button = xbmcgui.ControlButton(100, 250, 200, 50, 'Status', font='font14')
        ...
    """
    
    def __init__(self, x, y, width, height, label, focusTexture=None,
                 noFocusTexture=None, textOffsetX=10, textOffsetY=2,
                 alignment=(0 | 4), font=None, textColor=None,
                 disabledColor=None, angle=0, shadowColor=None,
                 focusedColor=None):
        # type: (int_type, int_type, int_type, int_type, str_type, str, str, int_type, int_type, int_type, str, str, str, int_type, str, str) -> None
        pass
    
    def setLabel(self, label="", font=None, textColor=None, disabledColor=None,
                 shadowColor=None, focusedColor=None, label2=""):
        # type: (str_type, str, str, str, str, str, str_type) -> None
        """
        Set's this buttons text attributes. 

        :param label: [opt] string or unicode - text string. 
        :param font: [opt] string - font used for label text. (e.g. 'font13') 
        :param textColor: [opt] hexstring - color of enabled button's label.
            (e.g. '0xFFFFFFFF')
        :param disabledColor: [opt] hexstring - color of disabled button's label.
            (e.g. '0xFFFF3300')
        :param shadowColor: [opt] hexstring - color of button's label's shadow.
            (e.g. '0xFF000000')
        :param focusedColor: [opt] hexstring - color of focused button's label.
            (e.g. '0xFFFFFF00')
        :param label2: [opt] string or unicode - text string.

        You can use the above as keywords for arguments and skip certain
        optional arguments. Once you use a keyword, all following arguments
        require the keyword.

        Example::

            ...
            # setLabel([label, font, textColor, disabledColor, shadowColor, focusedColor])
            self.button.setLabel('Status', 'font14', '0xFFFFFFFF', '0xFFFF3300', '0xFF000000')
            ...
        """
        pass
    
    def setDisabledColor(self, color):
        # type: (str) -> None
        """
        Set's this buttons disabled color.

        :param disabledColor: hexstring - color of disabled button's label.
            (e.g. '0xFFFF3300')

        Example::

            ...
            # setDisabledColor(disabledColor)
            self.button.setDisabledColor('0xFFFF3300')
            ...
        """
        pass
    
    def getLabel(self):
        # type: () -> unicode
        """
        Returns the buttons label as a unicode string. 

        :return: Unicode string

        Example::

            ...
            # getLabel()
            label = self.button.getLabel()
            ...
        """
        return u""
    
    def getLabel2(self):
        # type: () -> unicode
        """
        Returns the buttons label2 as a unicode string. 

        :return: Unicode string of label 2

        Example::

            ...
            # getLabel2()
            label = self.button.getLabel2()
            ...
        """
        return u""
    

class ControlGroup(Control):
    """
    Used to group controls together

    The group control is one of the most important controls.
    It allows you to group controls together, applying attributes
    to all of them at once. It also remembers the last navigated button
    in the group, so you can set the ``<onup>`` of a control to a group
    of controls to have it always go back to the one you were at before.
    It also allows you to position controls more accurately relative
    to each other, as any controls within a group take their coordinates
    from the group's top left corner (or from elsewhere if you use the
    ``"r"`` attribute). You can have as many groups as you like within the skin,
    and groups within groups are handled with no issues.

    This class include also all calls from Control

    :param x: integer - x coordinate of control. 
    :param y: integer - y coordinate of control. 
    :param width: integer - width of control. 
    :param height: integer - height of control.

    Example::

        ...
        self.group = xbmcgui.ControlGroup(100, 250, 125, 75)
        ...
    """
    
    def __init__(self, x, y, width, height):
        # type: (int_type, int_type, int_type, int_type) -> None
        pass
    

class ControlRadioButton(Control):
    """
    For control a radio button (as used for on/off settings)

    The radio button control is used for creating push button on/off settings
    in Kodi. You can choose the position, size, and look of the button.
    When the user clicks on the radio button, the state will change, toggling
    the extra textures (textureradioon and textureradiooff).
    Used for settings controls.

    This class include also all calls from Control

    :param x: integer - x coordinate of control. 
    :param y: integer - y coordinate of control. 
    :param width: integer - width of control. 
    :param height: integer - height of control. 
    :param label: string or unicode - text string. 
    :param focusOnTexture: [opt] string - filename for radio ON focused texture. 
    :param noFocusOnTexture: [opt] string - filename for radio ON not focused texture. 
    :param focusOfTexture: [opt] string - filename for radio OFF focused texture. 
    :param noFocusOffTexture: [opt] string - filename for radio OFF not focused texture. 
    :param focusTexture: [opt] string - filename for radio ON texture
        (deprecated, use focusOnTexture and noFocusOnTexture).
    :param noFocusTexture: [opt] string - filename for radio OFF texture
        (deprecated, use focusOffTexture and noFocusOffTexture).
    :param textOffsetX: [opt] integer - horizontal text offset 
    :param textOffsetY: [opt] integer - vertical text offset 
    :param alignment: [opt] integer - alignment of labelFlags for alignment
        used as bits to have several together:

    =================  ===========  ===============
    Defination name    Bitflag      Description    
    =================  ===========  ===============
    XBFONT_LEFT        0x00000000   Align X left   
    XBFONT_RIGHT       0x00000001   Align X right  
    XBFONT_CENTER_X    0x00000002   Align X center 
    XBFONT_CENTER_Y    0x00000004   Align Y center 
    XBFONT_TRUNCATED   0x00000008   Truncated text 
    XBFONT_JUSTIFIED   0x00000010   Justify text   
    =================  ===========  ===============

    :param font: [opt] string - font used for label text. (e.g. 'font13') 
    :param textColor: [opt] hexstring - color of label when control is enabled.
        radiobutton's label. (e.g. '0xFFFFFFFF')
    :param disabledColor: [opt] hexstring - color of label when control is disabled.
        (e.g. '0xFFFF3300')

    You can use the above as keywords for arguments and skip certain optional
    arguments. Once you use a keyword, all following arguments require
    the keyword. After you create the control, you need to add it to the window
    with addControl().

    New function added.  Deprecated **focusTexture** and **noFocusTexture**.
    Use **focusOnTexture** and **noFocusOnTexture**.

    Example::

        ...
        self.radiobutton = xbmcgui.ControlRadioButton(100, 250, 200, 50, 'Enable', font='font14')
        ...
    """
    
    def __init__(self, x, y, width, height, label, focusOnTexture=None,
                 noFocusOnTexture=None, focusOffTexture=None,
                 noFocusOffTexture=None, focusTexture=None, noFocusTexture=None,
                 textOffsetX=10, textOffsetY=2, _alignment=(0 |4 ), font=None,
                 textColor=None, disabledColor=None, angle=0, shadowColor=None,
                 focusedColor=None, disabledOnTexture=None,
                 disabledOffTexture=None):
        # type: (int_type, int_type, int_type, int_type, str_type, str, str, str, str, str, str, int_type, int_type, int_type, str, str, str, int_type, str, str, str, str) -> None
        pass
    
    def setSelected(self, selected):
        # type: (bool) -> None
        """
        Sets the radio buttons's selected status

        :param selected: bool - True=selected (on) / False=not selected (off)

        You can use the above as keywords for arguments and skip certain
        optional arguments. Once you use a keyword, all following arguments
        require the keyword.

        Example::

            ...
            self.radiobutton.setSelected(True)
            ...
        """
        pass
    
    def isSelected(self):
        # type: () -> bool
        """
        Returns the radio buttons's selected status. 

        :return: True if selected on

        Example::

            ...
            is = self.radiobutton.isSelected()
            ...
        """
        return True
    
    def setLabel(self, label="", font=None, textColor=None, disabledColor=None,
                 shadowColor=None, focusedColor=None, label2=""):
        # type: (str_type, str, str, str, str, str, str_type) -> None
        """
        Set's the radio buttons text attributes. 

        :param label: string or unicode - text string. 
        :param font: [opt] string - font used for label text. (e.g. 'font13') 
        :param textColor: [opt] hexstring - color of enabled radio button's label.
            (e.g. '0xFFFFFFFF')
        :param disabledColor: [opt] hexstring - color of disabled radio button's label.
            (e.g. '0xFFFF3300')
        :param shadowColor: [opt] hexstring - color of radio button's label's shadow.
            (e.g. '0xFF000000')
        :param focusedColor: [opt] hexstring - color of focused radio button's label.
            (e.g. '0xFFFFFF00')

        You can use the above as keywords for arguments and skip certain
        optional arguments. Once you use a keyword, all following arguments
        require the keyword.

        Example::

            ...
            # setLabel(label[, font, textColor, disabledColor, shadowColor, focusedColor])
            self.radiobutton.setLabel('Status', 'font14', '0xFFFFFFFF', '0xFFFF3300', '0xFF000000')
            ...
        """
        pass
    
    def setRadioDimension(self, x, y, width, height):
        # type: (int_type, int_type, int_type, int_type) -> None
        """
        Sets the radio buttons's radio texture's position and size. 

        :param x: integer - x coordinate of radio texture. 
        :param y: integer - y coordinate of radio texture. 
        :param width: integer - width of radio texture. 
        :param height: integer - height of radio texture.

        You can use the above as keywords for arguments and skip certain
        optional arguments. Once you use a keyword, all following arguments
        require the keyword.

        Example::

            ...
            self.radiobutton.setRadioDimension(x=100, y=5, width=20, height=20)
            ...
        """
        pass
    

class ControlSlider(Control):
    """
    Used for a volume slider

    The slider control is used for things where a sliding bar best represents
    the operation at hand (such as a volume control or seek control).
    You can choose the position, size, and look of the slider control.

    This class include also all calls from Control

    :param x: integer - x coordinate of control 
    :param y: integer - y coordinate of control 
    :param width: integer - width of control 
    :param height: integer - height of control 
    :param textureback: [opt] string - image filename 
    :param texture: [opt] string - image filename 
    :param texturefocus: [opt] string - image filename 
    :param orientation: [opt] integer - orientation of slider
        (xbmcgui.HORIZONTAL / xbmcgui.VERTICAL (default))

    You can use the above as keywords for arguments and skip certain optional
    arguments. Once you use a keyword, all following arguments require
    the keyword. After you create the control, you need to add it to the window
    with addControl().

    **orientation** option added.

    Example::

        ...
        self.slider = xbmcgui.ControlSlider(100, 250, 350, 40)
        ...
    """
    
    def __init__(self, x, y, width, height, textureback=None, texture=None,
                 texturefocus=None, orientation=VERTICAL):
        # type: (int_type, int_type, int_type, int_type, str, str, str, int) -> None
        pass
    
    def getPercent(self):
        # type: () -> float
        """
        Returns a float of the percent of the slider. 

        :return: float - Percent of slider

        Example::

            ...
            print self.slider.getPercent()
            ...
        """
        return 0.0
    
    def setPercent(self, pct):
        # type: (float) -> None
        """
        Sets the percent of the slider. 

        :param pct: float - Percent value of slider

        Example::

            ...
            self.slider.setPercent(50)
            ...
        """
        pass
    