"""bobject.py module contains all common functionality to objects contained
in a game board.
"""

import pygame
from . import iobject


class BObject(iobject.IObject):
    """BObject class contains all common attributes and functionality to any
    object contained in a game board.
    """

    def __init__(self, **kwargs):
        """___init__ method creates a new BObject instance.

        - position attribute stores the X and Y position in the board.

        - board_to_screen function translate a board position to a graphical
        position. It is only required to be used if the board object contains
        an sprite.
        """
        super().__init__(kwargs.get("a_name", None), kwargs.get("a_sprite", None))
        self.position = kwargs.get("a_position", pygame.Vector2())
        self.board_to_screen = kwargs.get("a_board_to_screen", None)
