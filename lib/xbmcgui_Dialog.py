import json, redis

import settings
import xbmcWrapperCommon

redis_connection = redis.StrictRedis(host=settings.REDIS_HOST, port= settings.REDIS_PORT,db= settings.REDIS_DB)

class Dialog(object):
    """
    Kodi's dialog class

    The graphical control element dialog box (also called dialogue box or
    just dialog) is a small window that communicates information to the user
    and prompts them for a response.
    """
    
    def __init__(self):
        # type: () -> None
        pass
    
    def yesno(self, heading, line1, line2="", line3="", nolabel="", yeslabel="",
              autoclose=0):
        # type: (str_type, str_type, str_type, str_type, str_type, str_type, int) -> bool
        """
        Yes / no dialog

        The Yes / No dialog can be used to inform the user about questions
        and get the answer.

        :param heading: string or unicode - dialog heading. 
        :param line1: string or unicode - line #1 multi-line text. 
        :param line2: [opt] string or unicode - line #2 text. 
        :param line3: [opt] string or unicode - line #3 text. 
        :param nolabel: [opt] label to put on the no button. 
        :param yeslabel: [opt] label to put on the yes button. 
        :param autoclose: [opt] integer - milliseconds to autoclose dialog.
            (default=do not autoclose)
        :return: Returns True if 'Yes' was pressed, else False.

        It is preferred to only use line1 as it is actually a multi-line text.
        In this case line2 and line3 must be omitted.

        Added new option **autoclose**.

        Example::

            ..
            dialog = xbmcgui.Dialog()
            ret = dialog.yesno('Kodi', 'Do you want to exit this script?')
            ..
        """
        return True
    
    def info(self, item):
        # type: (ListItem) -> bool
        """
        Info dialog

        Show the corresponding info dialog for a given listitem

        :param listitem: xbmcgui.ListItem - ListItem to show info for. 
        :return: Returns whether the dialog opened successfully.

        New function added.

        Example::

            ..
            dialog = xbmcgui.Dialog()
            ret = dialog.info(listitem)
            ..
        """
        return True
    
    def select(self, heading, list, autoclose=0, preselect=-1, useDetails=False):
        # type: (str_type, List[Union[str_type, ListItem]], int, int, bool) -> int
        print("xbmcgui_Dialog.select('%s', %s, %s, %s, %s)" % (heading, list, autoclose, preselect, useDetails))
        """
        Select dialog

        Show of a dialog to select of an entry as a key

        :param heading: string or unicode - dialog heading. 
        :param list: list of strings / xbmcgui.ListItems - list of items shown
            in dialog.
        :param autoclose: [opt] integer - milliseconds to autoclose dialog.
            (default=do not autoclose)
        :param preselect: [opt] integer - index of preselected item.
            (default=no preselected item)
        :param useDetails: [opt] bool - use detailed list instead of a compact list.
            (default=false)
        :return: Returns the position of the highlighted item as an integer.

        **preselect** option added.  Added new option **useDetails**.
        Allow listitems for parameter **list**

        Example::

            ..
            dialog = xbmcgui.Dialog()
            ret = dialog.select('Choose a playlist', ['Playlist #1', 'Playlist #2, 'Playlist #3'])
            ..
        """
        for choiceprio in ["high quality", "standard quality","english","united states"]:
            for index, choice in enumerate(list):
                if choice.lower().find(choiceprio) != -1:
                    return index
        if preselect != -1:
            return preselect
        return 0
    
    def contextmenu(self, list):
        # type: (List[str_type]) -> int
        """
        Show a context menu.

        :param list: string list - list of items. 
        :return: the position of the highlighted item as an integer
            (-1 if cancelled).

        New function added

        Example::

            ..
            dialog = xbmcgui.Dialog()
            ret = dialog.contextmenu(['Option #1', 'Option #2', 'Option #3'])
            ..
        """
        return 0
    
    def multiselect(self, heading, options, autoclose=0, preselect=None,
                    useDetails=False):
        # type: (str_type, List[Union[str_type, ListItem]], int, List[int], bool) -> List[int]
        """
        Show a multi-select dialog.

        :param heading: string or unicode - dialog heading. 
        :param options: list of strings / xbmcgui.ListItems - options to choose from. 
        :param autoclose: [opt] integer - milliseconds to autoclose dialog.
            (default=do not autoclose)
        :param preselect: [opt] list of int - indexes of items to preselect
            in list (default: do not preselect any item)
        :param useDetails: [opt] bool - use detailed list instead of a compact list.
            (default=false)
        :return: Returns the selected items as a list of indices, or None if cancelled.

        New function added.  Added new option **preselect**.
        Added new option **useDetails**.  Allow listitems for parameter **options**

        Example::

            ..
            dialog = xbmcgui.Dialog()
            ret = dialog.multiselect("Choose something", ["Foo", "Bar", "Baz"], preselect=[1,2])
            ..
        """
        return [0]
    
    def ok(self, heading, line1, line2="", line3=""):
        # type: (str_type, str_type, str_type, str_type) -> bool
        """
        OK dialog

        The functions permit the call of a dialog of information, a confirmation
        of the user by press from OK required.

        :param heading: string or unicode - dialog heading. 
        :param line1: string or unicode - line #1 multi-line text. 
        :param line2: [opt] string or unicode - line #2 text. 
        :param line3: [opt] string or unicode - line #3 text. 
        :return: Returns True if 'Ok' was pressed, else False.

        It is preferred to only use line1 as it is actually a multi-line text.
        In this case line2 and line3 must be omitted.

        Example::

            ..
            dialog = xbmcgui.Dialog()
            ok = dialog.ok('Kodi', 'There was an error.')
            ..
        """
        return True
    
    def textviewer(self, heading, text):
        # type: (str_type, str_type) -> None
        """
        **TextViewe dialog**

        The text viewer dialog can be used to display descriptions,
        help texts or other larger texts.

        :param heading: string or unicode - dialog heading. 
        :param text: string or unicode - text.

        New function added.

        Example::

            ..
            dialog = xbmcgui.Dialog()
            dialog.textviewer('Plot', 'Some movie plot.')
            ..
        """
        pass
    
    def browse(self, type, heading, shares, mask="", useThumbs=False,
               treatAsFolder=False, defaultt="", enableMultiple=False):
        # type: (int, str_type, str_type, str_type, bool, bool, str_type, bool) -> Union[str, List[str]]
        """
        Browser dialog

        The function offer the possibility to select a file by the user of the add-on.

        It allows all the options that are possible in Kodi itself and offers all support file types.

        :param type: integer - the type of browse dialog.

        ======  =============================
        Param   Name                         
        ======  =============================
        0       ShowAndGetDirectory          
        1       ShowAndGetFile               
        2       ShowAndGetImage              
        3       ShowAndGetWriteableDirectory 
        ======  =============================

        :param heading: string or unicode - dialog heading. 
        :param shares: string or unicode - from sources.xml . (i.e. 'myprograms') 
        :param mask: [opt] string or unicode - '|' separated file mask. (i.e. '.jpg|.png') 
        :param useThumbs: [opt] boolean - if True autoswitch to Thumb view if files exist. 
        :param treatAsFolder: [opt] boolean - if True playlists and archives act as folders. 
        :param defaultt: [opt] string - default path or file. 
        :param enableMultiple: [opt] boolean - if True multiple file selection is enabled.
        :return: If enableMultiple is False (default): returns filename and/or
            path as a string to the location of the highlighted item,
            if user pressed 'Ok' or a masked item was selected.
            Returns the default value if dialog was canceled. If enableMultiple
            is True: returns tuple of marked filenames as a strin if user
            pressed 'Ok' or a masked item was selected.
            Returns empty tuple if dialog was canceled.
            If type is 0 or 3 the enableMultiple parameter is ignore

        Example::

            ..
            dialog = xbmcgui.Dialog()
            fn = dialog.browse(3, 'Kodi', 'files', '', False, False, False,
                            'special://masterprofile/script_data/Kodi Lyrics')
            ..
        """
        return ""
    
    def browseSingle(self, type, heading, shares, mask="", useThumbs=False,
                     treatAsFolder=False, defaultt=""):
        # type: (int, str_type, str_type, str_type, bool, bool, str_type) -> str
        """
        Browse single dialog

        The function offer the possibility to select a file by the user of the add-on.

        It allows all the options that are possible in Kodi itself and offers
        all support file types.

        :param type: integer - the type of browse dialog.

        ======  =============================
        Param   Name                         
        ======  =============================
        0       ShowAndGetDirectory          
        1       ShowAndGetFile               
        2       ShowAndGetImage              
        3       ShowAndGetWriteableDirectory 
        ======  =============================

        :param heading: string or unicode - dialog heading. 
        :param shares: string or unicode - from sources.xml . (i.e. 'myprograms') 
        :param mask: [opt] string or unicode - '|' separated file mask. (i.e. '.jpg|.png') 
        :param useThumbs: [opt] boolean - if True autoswitch to Thumb view if
            files exist (default=false).
        :param treatAsFolder: [opt] boolean - if True playlists and archives
            act as folders (default=false).
        :param defaultt: [opt] string - default path or file.
        :return: Returns filename and/or path as a string to the location
            of the highlighted item, if user pressed 'Ok' or a masked item
            was selected. Returns the default value if dialog was canceled.

        Example::

            ..
            dialog = xbmcgui.Dialog()
            fn = dialog.browseSingle(3, 'Kodi', 'files', '', False, False,
                            'special://masterprofile/script_data/Kodi Lyrics')
            ..
        """
        return ""
    
    def browseMultiple(self, type, heading, shares, mask="", useThumbs=False,
                       treatAsFolder=False, defaultt=""):
        # type: (int, str_type, str_type, str_type, bool, bool, str_type) -> List[str]
        """
        Browser dialog

        The function offer the possibility to select multiple files by the user
        of the add-on.

        It allows all the options that are possible in Kodi itself and offers
        all support file types.

        :param type: integer - the type of browse dialog.

        ======  ================
        Param   Name            
        ======  ================
        1       ShowAndGetFile  
        2       ShowAndGetImage 
        ======  ================

        :param heading: string or unicode - dialog heading. 
        :param shares: string or unicode - from sources.xml . (i.e. 'myprograms') 
        :param mask: [opt] string or unicode - '|' separated file mask. (i.e. '.jpg|.png') 
        :param useThumbs: [opt] boolean - if True autoswitch to Thumb view
            if files exist (default=false).
        :param treatAsFolder: [opt] boolean - if True playlists and archives
            act as folders (default=false).
        :param defaultt: [opt] string - default path or file. 
        :return: Returns tuple of marked filenames as a string," if user
            pressed 'Ok' or a masked item was selected.
            Returns empty tuple if dialog was canceled.

        Example::

            ..
            dialog = xbmcgui.Dialog()
            fn = dialog.browseMultiple(2, 'Kodi', 'files', '', False, False,
                            'special://masterprofile/script_data/Kodi Lyrics')
            ..
        """
        return [""]
    
    def numeric(self, type, heading, defaultt=""):
        # type: (int, str_type, str_type) -> str
        """
        **Numeric dialog**

        The function have to be permitted by the user for the representation
        of a numeric keyboard around an input.

        :param type: integer - the type of numeric dialog.

        ======  ====================  =============================
        Param   Name                  Format                       
        ======  ====================  =============================
        0       ShowAndGetNumber      (default format: #)          
        1       ShowAndGetDate        (default format: DD/MM/YYYY) 
        2       ShowAndGetTime        (default format: HH:MM)      
        3       ShowAndGetIPAddress   (default format: #.#.#.#)    
        ======  ====================  =============================

        :param heading: string or unicode - dialog heading. 
        :param defaultt: [opt] string - default value. 
        :return: Returns the entered data as a string.
            Returns the default value if dialog was canceled.

        Example::

            ..
            dialog = xbmcgui.Dialog()
            d = dialog.numeric(1, 'Enter date of birth')
            ..
        """
        return ""
    
    def notification(self, heading, message, icon="", time=0, sound=True):
        # type: (str_type, str_type, str_type, int, bool) -> None
        """
        Show a Notification alert.

        :param heading: string - dialog heading. 
        :param message: string - dialog message. 
        :param icon: [opt] string - icon to use. (default xbmcgui.NOTIFICATION_INFO) 
        :param time: [opt] integer - time in milliseconds (default 5000) 
        :param sound: [opt] bool - play notification sound (default True)

        Builtin Icons:xbmcgui.NOTIFICATION_INFO

        xbmcgui.NOTIFICATION_WARNING

        xbmcgui.NOTIFICATION_ERROR

          New function added.

        Example::

            ..
            dialog = xbmcgui.Dialog()
            dialog.notification('Movie Trailers', 'Finding Nemo download finished.',
                                xbmcgui.NOTIFICATION_INFO, 5000)
            ..
        """
        pass
    
    def input(self, heading, defaultt="", type=0, option=0, autoclose=0):
        # type: (str_type, str_type, int, int, int) -> str
        """
        Show an Input dialog.

        :param heading: string - dialog heading. 
        :param defaultt: [opt] string - default value. (default=empty string) 
        :param type: [opt] integer - the type of keyboard dialog.
            (default=xbmcgui.INPUT_ALPHANUM)

        =======================  ========
        Parameter                Format  
        =======================  ========
        xbmcgui.INPUT_ALPHANUM   (standard keyboard)
        xbmcgui.INPUT_NUMERIC    (format: #)
        xbmcgui.INPUT_DATE       (format: DD/MM/YYYY)
        xbmcgui.INPUT_TIME       (format: HH:MM)
        xbmcgui.INPUT_IPADDRESS  (format: #.#.#.#)
        xbmcgui.INPUT_PASSWORD   (return md5 hash of input, input is masked)
        =======================  ========

        :param option: [opt] integer - option for the dialog. (see Options below)
            Password dialog: ``xbmcgui.PASSWORD_VERIFY`` (verifies an existing
            (default) md5 hashed password)Alphanum dialog:
            ``xbmcgui.ALPHANUM_HIDE_INPUT`` (masks input)
        :param autoclose: [opt] integer - milliseconds to autoclose dialog.
            (default=do not autoclose)
        :return: Returns the entered data as a string.
            Returns an empty string if dialog was canceled.

        New function added.

        Example::

            ..
            dialog = xbmcgui.Dialog()
            d = dialog.input('Enter secret code', type=xbmcgui.INPUT_ALPHANUM,
                             option=xbmcgui.ALPHANUM_HIDE_INPUT)
            ..
        """
        input = redis_connection.get("%s:keyboard" % xbmcWrapperCommon.CURRENT_QUEUE)
        if input != None:    
            return input        
        redis_connection.rpush(xbmcWrapperCommon.CURRENT_QUEUE,json.dumps({"key": "Keyboard:getText" }))
        print("No keyboard input supplied")
        return ""
    

class DialogProgress(object):
    """
    Kodi's progress dialog class
    """
    
    def __init__(self):
        # type: () -> None
        pass
    
    def create(self, heading, line1="", line2="", line3=""):
        # type: (str_type, str_type, str_type, str_type) -> None
        """
        Create and show a progress dialog.

        :param heading: string or unicode - dialog heading. 
        :param line1: [opt] string or unicode - line #1 multi-line text. 
        :param line2: [opt] string or unicode - line #2 text. 
        :param line3: [opt] string or unicode - line #3 text.

        It is preferred to only use line1 as it is actually a multi-line text.
        In this case line2 and line3 must be omitted.

        Use update() to update lines and progressbar.

        Example::

            ..
            pDialog = xbmcgui.DialogProgress()
            pDialog.create('Kodi', 'Initializing script...')
            ..
        """
        pass
    
    def update(self, percent, line1="", line2="", line3=""):
        # type: (int, str_type, str_type, str_type) -> None
        """
        Updates the progress dialog.

        :param percent: integer - percent complete. (0:100) 
        :param line1: [opt] string or unicode - line #1 multi-line text. 
        :param line2: [opt] string or unicode - line #2 text. 
        :param line3: [opt] string or unicode - line #3 text.

        It is preferred to only use line1 as it is actually a multi-line text.
        In this case line2 and line3 must be omitted.

        Example::

            ..
            pDialog.update(25, 'Importing modules...')
            ..
        """
        pass
    
    def close(self):
        # type: () -> None
        """
        Close the progress dialog.

        Example::

            ..
            pDialog.close()
            ..
        """
        pass
    
    def iscanceled(self):
        # type: () -> bool
        """
        Checks progress is canceled.

        :return: True if the user pressed cancel.

        Example::

            ..
            if (pDialog.iscanceled()): return
            ..
        """
        return True
    

class DialogBusy(object):
    """
    Kodi's busy dialog class

      New class added.
    """
    
    def __init__(self):
        # type: () -> None
        pass
    
    def create(self):
        # type: () -> None
        """
        Create and show a busy dialog.

        Use update() to update the progressbar.

        New method added

        Example::

            ..
            dialog = xbmcgui.DialogBusy()
            dialog.create()
            ..
        """
        pass
    
    def update(self, percent):
        # f(int) -> None
        """
        Updates the busy dialog.

        :param percent: integer - percent complete. (-1:100)

        If percent == -1 (default), the progressbar will be hidden.

        New method added
        """
        pass
    
    def close(self):
        # type: () -> None
        """
        Close the progress dialog.

        New method added
        """
        pass
    
    def iscanceled(self):
        # f() -> bool
        """
        Checks if busy dialog is canceled.

        :return: True if the user pressed cancel.

        New method added
        """
        return True
    

class DialogProgressBG(object):
    """
    Kodi's background progress dialog class
    """
    
    def __init__(self):
        # type: () -> None
        pass
    
    def create(self, heading, message=""):
        # type: (str_type, str_type) -> None
        """
        Create and show a background progress dialog.

        :param heading: string or unicode - dialog heading. 
        :param message: [opt] string or unicode - message text.

        'heading' is used for the dialog's id. Use a unique heading.
        Use update() to update heading, message and progressbar.

        Example::

            ..
            pDialog = xbmcgui.DialogProgressBG()
            pDialog.create('Movie Trailers', 'Downloading Monsters Inc... .')
            ..
        """
        pass
    
    def update(self, percent=0, heading="", message=""):
        # type: (int, str_type, str_type) -> None
        """
        Updates the background progress dialog.

        :param percent: [opt] integer - percent complete. (0:100) 
        :param heading: [opt] string or unicode - dialog heading. 
        :param message: [opt] string or unicode - message text.

        To clear heading or message, you must pass a blank character.

        Example::

            ..
            pDialog.update(25, message='Downloading Finding Nemo ...')
            ..
        """
        pass
    
    def close(self):
        # type: () -> None
        """
        Close the background progress dialog

        Example::

            ..
            pDialog.close()
            ..
        """
        pass
    
    def isFinished(self):
        # type: () -> bool
        """
        Checks progress is finished

        :return: True if the background dialog is active.

        Example::

            ..
            if (pDialog.isFinished()): return
            ..
        """
        return True
    
