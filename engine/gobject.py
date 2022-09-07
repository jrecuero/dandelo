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

        """
        super().__init__(kwargs.get("a_name", None), kwargs.get("a_sprite", None))
        self.position = kwargs.get("a_position", pygame.Vector2())
