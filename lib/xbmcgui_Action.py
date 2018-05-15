
class Action(object):
    """
    Action class

    ``xbmcgui.Action():``

    This class serves in addition to identify carried out kodi_key_action_ids
    of Kodi and to be able to carry out thereby own necessary steps.

    The data of this class are always transmitted by callback
    Window::onAction at a window.
    """
    
    def __init__(self):
        # type: () -> None
        pass
    
    def getId(self):
        # type: () -> long
        """
        To get kodi_key_action_ids 

        This function returns the identification code used by the explained order,
        it is necessary to determine the type of command from kodi_key_action_ids.

        :return: The action's current id as a long or 0 if no action is mapped in the xml's.

        Example::

            ..
            def onAction(self, action):
                if action.getId() == ACTION_PREVIOUS_MENU:
                    print('action recieved: previous')
            ..
        """
        return 0L
    
    def getButtonCode(self):
        # type: () -> long
        """
        Returns the button code for this action. 

        :return: [integer] button code 
        """
        return 0L
    
    def getAmount1(self):
        # type: () -> float
        """
        Returns the first amount of force applied to the thumbstick. 

        :return: [float] first amount 
        """
        return 0.0
    
    def getAmount2(self):
        # type: () -> float
        """
        Returns the second amount of force applied to the thumbstick. 

        :return: [float] second amount 
        """
        return 0.0
