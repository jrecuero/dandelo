"""board_scene.py module contains the game board scene.
"""

import pygame
from engine import board
from engine import scene
from engine import idefaults
from . import config
from . import player


class BoardScene(scene.Scene):
    """BoardScene class contains all functionality to create the board
    scene.

    - board attribute contains a Board instance where player and other game
    objects will be placed.

    - player attribute contains a Player instance with the player game object.
    """

    def __init__(self, **kwargs):
        """__init__ method creates a new BoardScene instance.
        """
        super().__init__(a_name=config.SCENE_BOARD, **kwargs)
        self.board = board.Board(10, 10, idefaults.DEFAULT_WIDTH, idefaults.DEFAULT_LENGTH)
        self.board.create_default_board(8)
        self.player = player.Player(a_position=pygame.Vector2(), a_board_to_screen=self.board.board_to_screen)
        self.player.out_of_bounds = self.board.out_of_bounds
        self.add_object(self.board)
        self.add_object(self.player)
        self.keyboard_control_object = self.player
