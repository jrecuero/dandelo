"""bobject.py module contains all common functionality to objects contained
in a game board.
"""

import pygame
from . import gobject


class BObject(gobject.GObject):
    """BObject class contains all common attributes and functionality to any
    object contained in a game board.
    """

    def __init__(self, **kwargs):
        """___init__ method creates a new BObject instance.

        - position attribute stores the X and Y position in the board.

        - board_to_screen function translates a board position to a graphical
        position. It is only required to be used if the board object contains
        an sprite.

        - out_of_bounds function checks if a board object is inside or outside
        the board.
        """
        super().__init__(**kwargs)
        self.board_position = kwargs.get("a_board_position", pygame.Vector2())
        self.board_to_screen = kwargs.get("a_board_to_screen", None)
        self.out_of_bounds = kwargs.get("a_out_of_bounds", None)

    @property
    def position(self):
        """position property returns the actual position in the screen.
        """
        if self.board_to_screen:
            self._position = self.board_to_screen(self.board_position)
        return super().position

    @position.setter
    def position(self, a_position):
        """position setter property sets a new value for the position in the
        screen.
        """
        assert("BObject does not allow position.setter")

    def set_board_position(self, a_position):
        """set_board_position method sets the player instance in a new board
        position.
        """
        self.board_position = a_position
        _ = self.position
