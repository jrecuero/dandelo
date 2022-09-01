"""ihandler.py module contains all functionality for the common handler
interface functionality.
"""

class IHandler:
    """IHandler class implements the handler interface with all common
    functionality for any handler in the game.
    """

    def __init__(self):
        """___init__ method initializes a GameHandler instance.

        - objects list contains all game object.

        - keyboard_control_object attribute stores the game object that should
        receive and process keyboard events.

        - keyboard_control_default attribute stores a default object that
        should handle any keyboard input by default and if input has not been
        captured before.

        - keyboard_release_callback attribute stores the function to be called
        when the game object processing keyboard events is released from that
        functionality.

        - actions dictionary stores functions to be called when an action has
        to be invoked.
        """
        self.objects = []
        self.keyboard_control_object = None
        self.keyboard_control_default = None
        self.keyboard_release_callback = None
        self.actions = {}

    def add_object(self, a_object):
        """add_object method adds the given object to be handle.
        """
        if a_object in self.objects:
            return False
        self.objects.append(a_object)
        return True

    def remove_object(self, a_object):
        """remove_object method removes the given object to be handled.
        """
        if a_object not in self.objects:
            return False
        self.objects.remove(a_object)
        return True

    def handle_keyboard_event(self, a_event):
        """handle_keyboard_event method pass all keyboard events to the
        object that had control of the keyboard.
        """
        self.keyboard_control_object.handle_keyboard_event(a_event, self.keyboard_release_callback)

    def add_action(self, a_action, a_callback):
        """add_action methods adds a function to be invoked for the given
        action.
        """
        if a_action in self.actions:
            return False
        self.actions[a_action] = a_callback
        return True

    def remove_action(self, a_action):
        """remove_action method removes a function for the given action.
        """
        if a_action not in self.actions:
            return False
        del self.actions[a_action]
        return True

    def run_action(self, a_action, **kwargs):
        """run_action method runs the given action.
        """
        if a_action not in self.actions:
            return False
        self.actions[a_action](**kwargs)
        return True
