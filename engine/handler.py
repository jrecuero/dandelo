"""handler.py module implements the game main controller.
"""

import pygame
from . import ihandler
from . import menu


class GameHandler(ihandler.IHandler):
    """GameHandler class implements the game handler in charge to keep
    control for all elements in the game.
    """

    def __init__(self):
        """___init__ method initializes a GameHandler instance.

        - sprites list contains all game sprites. A sprite always belong to a
        game object.

        - scenes list contains all game scenes.

        - active_scene list contains the queue with scenes that are active so
        they have to be displayed.

        - events list contains all events handle has to process.
        """
        super().__init__()
        self.sprites = pygame.sprite.Group()
        self.scenes = []
        self.active_scene = []

    def add_object(self, a_object):
        """add_object method adds the given object to be handle.
        """
        if not super().add_object(a_object):
            return False
        if hasattr(a_object, "get_sprite"):
            object_sprite = a_object.get_sprite()
            if object_sprite:
                self.sprites.add(object_sprite)
        return True

    def remove_object(self, a_object):
        """remove_object method removes the given object to be handled.
        """
        if not super().remove_object(a_object):
            return False
        if hasattr(a_object, "get_sprite"):
            object_sprite = a_object.get_sprite()
            if object_sprite:
                self.sprites.remove(object_sprite)
        return True

    def add_scene(self, a_scene):
        """add_scene method adds an scene to be handled.
        """
        if a_scene in self.scenes:
            return False
        self.scenes.append(a_scene)
        if hasattr(a_scene, "notifier") and a_scene.notifier is None:
            a_scene.notifier = self.event_notifier 

        return True

    def remove_scene(self, a_scene):
        """remove_scene method removes an scene to be handled.
        """
        if a_scene not in self.scenes:
            return False
        self.scenes.remove(a_scene)
        return True

    def get_scene_by_name(self, a_name):
        """get_scene_by_name method looks for a scene with the given name
        in all scenes.
        """
        for l_scene in self.scenes:
            if l_scene.name == a_name:
                return l_scene
        return None

    def get_active_scene(self):
        """get_active_scene method returns the scene that is at the
        bottom of the queue.
        """
        if len(self.active_scene) == 0:
            return None
        return self.active_scene[-1]

    def activate_this_scene(self, a_scene, **kwargs):
        """activate_this_scene methods sets the given scene as the active one.
        """
        if a_scene not in self.scenes:
            return False
        self.active_scene.append(a_scene)
        a_scene.open(**kwargs)
        for l_object in a_scene.objects:
            self.add_object(l_object)
        self.keyboard_control_object = a_scene.keyboard_control_object

    def reactivate_this_scene(self, a_scene):
        """reactivate_scene methods reactivate an scene that was already
        active but queued.
        """
        if a_scene not in self.active_scene:
            return False
        if self.get_active_scene() != a_scene:
            self.active_scene.remove(a_scene)
            self.active_scene.append(a_scene)
        self.keyboard_control_object = a_scene.keyboard_control_object
        return True

    def reactivate_top_scene(self):
        """reactivate_top_scene method activates the scene at the top of the
        queue.
        """
        v_scene = self.get_active_scene()
        return self.reactivate_this_scene(v_scene)

    def deactivate_this_scene(self, a_scene):
        """deactivate_this_scene method sets the given scene as non-active.
        """
        if a_scene is None or a_scene != self.get_active_scene():
            return False
        # call to the scene close method in order to notify to the scene that
        # is being deactivated.
        a_scene.close()
        # remove the scene from the queue of active scenes and remove
        # all scene objects from the handler.
        self.active_scene.remove(a_scene)
        for l_object in a_scene.objects:
            self.remove_object(l_object)
        return True

    def deactivate_active_scene(self):
        """deactivate_active_scene methods deactivate the actual active
        scene.
        """
        v_scene = self.get_active_scene()
        return self.deactivate_this_scene(v_scene)

    def end_active_and_activate_this_scene(self, a_scene):
        """end_active_and_active_this_scene method deactivates the active scene
        and set the given scene as active now.
        """
        v_active_scene = self.get_active_scene()
        if self.deactivate_scene(v_active_scene) is False:
            return False
        return self.activate_scene(a_scene)

    def end_active_and_reactivate_this_scene(self, a_scene):
        """end_active_and_reactivate_this_scene method deactivates the active
        scene and reactivate the given scene.
        """
        v_active_scene = self.get_active_scene()
        if self.deactivate_scene(v_active_scene) is False:
            return False
        return self.reactivate_scene(a_scene)

    def end_active_and_reactivate_next(self):
        """end_active_and_reactivate_next method deactivates the active scene
        and reactivates the next scene in the active queue.
        """
        if not self.deactivate_active_scene():
            return False
        return self.reactivate_top_scene()

    def draw(self, a_screen):
        """draw method calls to draw for every game object contained in
        the handler.
        """
        self.sprites.draw(a_screen)

    def update(self):
        """update method updates the game handler and calls any update for
        any children.
        """
        self.sprites.update()

    def add_event(self, a_event):
        """add_event methods add a new event to be handled.
        """
        self.events.append(a_event)

    def next_event(self):
        """next_event method returns the first event.
        """
        return self.events.pop(0)

    def handle_keyboard_event(self, a_pygame_event):
        """handle_keyboard_event method pass all keyboard events to the
        object that had control of the keyboard.
        """
        v_active_scene = self.get_active_scene()
        if v_active_scene:
            v_event = v_active_scene.handle_keyboard_event(a_pygame_event)
            return v_event
        return super().handle_keyboard_event(a_pygame_event)

    def handle_all_events(self):
        """handle_events method handles all events in the event list.
        """
        v_active_scene = self.get_active_scene()
        if v_active_scene:
            v_active_scene.handle_all_events()
        super().handle_all_events()

    def tick_timers(self, a_fps):
        """tick_timers method updates all timers being handled.
        """
        v_active_scene = self.get_active_scene()
        if v_active_scene:
            v_active_scene.tick_timers(a_fps)
        for l_timer in self.timers:
            l_timer.tick(self, a_fps)

    def start_frame(self, a_fps):
        """start_frame method is called by the engine at the start of every
        frame.
        """
        self.tick_timers(a_fps)
        v_active_scene = self.get_active_scene()
        if v_active_scene:
            v_active_scene.start_frame(a_fps)

        
    def end_frame(self):
        """end_frame method is called by the engine at the end of every frame.
        """
        pass