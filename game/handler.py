"""handler.py module implements the game main controller.
"""

from distutils.command.config import config
import pygame
import ihandler
import config
import menu


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
        """
        super().__init__()
        self.sprites = pygame.sprite.Group()
        self.scenes = []
        self.active_scene = []

    def add_object(self, the_object):
        """add_object method adds the given object to be handle.
        """
        if not super().add_object(the_object):
            return False
        if hasattr(the_object, "get_sprite"):
            object_sprite = the_object.get_sprite()
            if object_sprite:
                self.sprites.add(object_sprite)
        return True

    def remove_object(self, the_object):
        """remove_object method removes the given object to be handled.
        """
        if not super().remove_object(the_object):
            return False
        if hasattr(the_object, "get_sprite"):
            object_sprite = the_object.get_sprite()
            if object_sprite:
                self.sprites.remove(object_sprite)
        return True

    def add_scene(self, the_scene):
        """add_scene method adds an scene to be handled.
        """
        if the_scene in self.scenes:
            return False
        self.scenes.append(the_scene)
        return True

    def remove_scene(self, the_scene):
        """remove_scene method removes an scene to be handled.
        """
        if the_scene not in self.scenes:
            return False
        self.scenes.remove(the_scene)
        return True

    def get_active_scene(self):
        """get_active_scene method returns the scene that is at the
        bottom of the queue.
        """
        if len(self.active_scene) == 0:
            return None
        return self.active_scene[-1]

    def activate_scene(self, the_scene, the_queue=False, the_load=True):
        """activate_scene method sets the given scene as the active one.
        If the_queue is True, it means it is placed on top of the previous
        scenario, instead of replacing it.
        """
        if the_scene not in self.scenes:
            return False
        if the_queue is False:
            self.deactivate_scene(self.get_active_scene())
        # Add the scene to the queue of active scenes and add all
        # scene objects to the handler.
        self.active_scene.append(the_scene)
        if the_load:
            for object in the_scene.objects:
                self.add_object(object)
        self.keyboard_control_object = the_scene.keyboard_control_object
        self.keyboard_release_callback = the_scene.keyboard_release_callback
        return True

    def deactivate_scene(self, the_scene, the_queue=False):
        """deactivate_scene methods sets the given scene as non-active.
        If the_queue is True, it means it is removed from the queue and the 
        previous scene is automatically activated.
        """
        if the_scene is None or the_scene != self.get_active_scene():
            return False
        # remove the scene from the queue of active scenes and remove
        # all scene objects from the handler.
        self.active_scene.remove(the_scene)
        for object in the_scene.objects:
            self.remove_object(object)
        if self.get_active_scene():
            # Set the_load as False, because scene object have been 
            # previously loaded by the handler.
            self.active_scene(self.get_active_scene(), the_load=False)

    def draw(self, the_screen):
        """draw method calls to draw for every game object contained in 
        the handler.
        """
        self.sprites.draw(the_screen)

    def update(self):
        """update method updates the game handler and calls any update for
        any children.
        """
        self.sprites.update()

    def release_player(self):
        handler = self
        def _release_player(the_next):
            game_menu = menu.PopUpMenu((300, 10), ["open", "world", "battle", "end"])
            handler.add_object(game_menu)
            handler.keyboard_control_object = game_menu
            handler.keyboard_release_callback = handler.release_menu()
        return _release_player

    def release_menu(self):
        handler = self
        def _release_menu(the_next):
            pass
        return _release_menu
