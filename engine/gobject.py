"""gobject.py module contains all common functionality to objects that have to
be displayed in the screen.
"""

import pygame
from . import iobject


class GObject(iobject.IObject):
    """GObject class contains all common attributes and functionality to any
    object that have to be displayed in the screen. They should contain an
    sprite.
    """

    def __init__(self, **kwargs):
        """___init__ method creates a new GObject instance.

        - position attribute stores the X and Y position in the screen.

        - sprite pygame Sprite keeps an optional sprite to be displayed for
        the game object.

        - width attribute stores the graphical object width.

        - length attribute stores the graphical object length.
        """
        super().__init__(kwargs.get("a_name", None))
        self._position = kwargs.get("a_position", pygame.Vector2())
        self.sprite = kwargs.get("a_sprite", None)
        if self.sprite:
            self.width = self.sprite.width
            self.height = self.sprite.height
        else:
            self.width = kwargs.get("a_width", None)
            self.height = kwargs.get("a_height", None)

    @property
    def position(self):
        """position property returns the actual position in the screen.
        """
        return self._position

    @position.setter
    def position(self, a_position):
        """position setter property sets a new value for the position in the
        screen.
        """
        self._position = a_position

    def get_sprite(self):
        """get_sprite method returns the sprite instance to be added to the
        handler sprite group.
        """
        return self.sprite
