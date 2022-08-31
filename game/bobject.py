"""bobject.py module contains all common functionality to objects contained
in a game board.
"""

import pygame
import iobject


class BObject(iobject.IObject):
    """BObject class contains all common attributes and functionality to any
    object contained in a game board.
    """

    def __init__(self, **kwargs):
        """___init__ method creates a new BObject instance.

        - position attribute stores the X and Y position in the board.
        """
        super().__init__(kwargs.get("the_name", None), kwargs.get("the_sprite", None))
        self.position = kwargs.get("the_position", pygame.Vector2())