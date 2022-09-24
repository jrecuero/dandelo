"""ihandler.py module contains all functionality for the common handler
interface functionality.
"""

import pygame


def callback(a_func):
    """callback function is a decorator to be used inside class methods and it
    allows to pass a result the object that handles the event.
    """
    def inner(a_handler, a_object):
        """inner function is the inner part of the decorator which is called
        with the object to handle the event.
        """
        def wrapper(**kwargs):
            """wrapper function is the wrapper part of the decorator which is
            making the call to the function being decorated and it insert the
            object handling the event as part of the result.
            It is valid only for class methods.
            """
            v_event = a_func(a_handler, **kwargs)
            v_event.data = {} if v_event.data is None else v_event.data
            v_event.data["object"] = a_object
            v_event.data["handler"] = a_handler
            return v_event
        return wrapper
    return inner


class IHandler:
    """IHandler class implements the handler interface with all common
    functionality for any handler in the game.
    """

    def __init__(self, a_type="top"):
        """___init__ method initializes a GameHandler instance.

        - a_type attribute stores the kind of handler. "top" is used for the
        main and top handler.

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

        - events list stores all events to be processed by the handler.

        - timers attribute is a list with all timers to be handled.

        - notifier attribute keeps the callback to be used to notify events to
        the proper parent.
        """
        self.type = a_type
        self.objects = []
        self.sprites = pygame.sprite.Group()
        self.keyboard_control_object = None
        self.actions = {}
        self.events = []
        self.timers = []
        self.notifier = None

    def add_object(self, a_object):
        """add_object method adds the given object to be handle.
        """
        if a_object in self.objects:
            return False
        self.objects.append(a_object)
        if hasattr(a_object, "notifier") and a_object.notifier is None:
            a_object.notifier = self.event_notifier
        if hasattr(a_object, "get_sprite"):
            object_sprite = a_object.get_sprite()
            if object_sprite:
                self.sprites.add(object_sprite)
        return True

    def remove_object(self, a_object):
        """remove_object method removes the given object to be handled.
        """
        if a_object not in self.objects:
            return False
        self.objects.remove(a_object)
        if hasattr(a_object, "get_sprite"):
            object_sprite = a_object.get_sprite()
            if object_sprite:
                self.sprites.remove(object_sprite)
        return True

    def draw(self, a_screen):
        """draw method calls to draw for every game object contained in
        the handler.
        """
        self.sprites.draw(a_screen)

    def handle_keyboard_event(self, a_event):
        """handle_keyboard_event method pass all keyboard events to the
        object that had control of the keyboard.
        """
        if self.keyboard_control_object is None:
            return None
        result = self.keyboard_control_object.handle_keyboard_event(a_event)
        return result

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

    def add_event(self, a_event):
        """add_event method adds a new event to processed by the handler.
        """
        self.events.append(a_event)
        return True

    def remove_event(self, a_event):
        """remove_event method removes an event to be processed by the handler.
        """
        if a_event in self.events:
            self.events.remove(a_event)
            return True
        return False

    def next_event(self):
        """next_event method returns the first event.
        """
        return self.events.pop(0)

    def event_notifier(self, a_event, **kwargs):
        """event_notifier method allows to create events for any object in the
        handler.
        """
        if a_event.data.get("handler", None) is None:
            a_event.data["handler"] = []
        a_event.data["handler"].append(self)
        if a_event.destination == self.type:
            self.add_event(a_event)
        else:
            if self.notifier:
                self.notifier(a_event)

    def handle_all_events(self):
        """handle_events method handles all events in the event list.
        """
        for l_event in self.events[:]:
            if self.handle_event(l_event):
                self.events.remove(l_event)

    def handle_event(self, a_event):
        """handle_event method processes a given event.
        """
        if a_event.trigger == "action":
            v_role = a_event.role
            if v_role in self.actions:
                return self.actions[v_role](a_event)
        return False

    def add_timer(self, a_timer):
        """add_timer method adds a new timer to be handled.
        """
        if a_timer in self.timers:
            return False
        self.timers.append(a_timer)
        return True

    def remove_timer(self, a_timer):
        """remove_timer method removes a timer to be handled.
        """
        if a_timer not in self.timers:
            return False
        self.timers.remove(a_timer)
        return True

    def tick_timers(self, a_fps):
        """tick_timers method updates all timers being handled.
        """
        for l_timer in self.timers:
            l_timer.tick(self, a_fps)
