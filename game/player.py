"""player.py module implements all classes related with the game player.
"""

import colors
import config
import pygame
from pygame.locals import *


class Player(pygame.sprite.Sprite):
    """Player class implements the main player in the board.
    """

    def __init__(self, the_x, the_y, the_board_to_screen):
        """__init__ method initializes a Player instance.

        - x attribute stores the board X position for the player.

        - y attribute stores the board Y position for the player

        - old_position tuple stores the board X and Y position for the player
        after a move action.

        - board_to_screen function is called to translate board positions to
        graphical positions where sprites will be displayed.

        - out_of_bounds function is called to check if the player is inside
        or outside the board.
        
        - image pygame Surface instance is a derived attribute where the
        pygame Surface used to display the player sprite is stored.

        - rect pygame Rectangle instance is a derived attribute where the
        surface rectangle used to display the player sprite is stored.
        """
        super().__init__()
        self.x = the_x
        self.y = the_y
        self.old_position = (None, None)
        self.board_to_screen = the_board_to_screen
        self.out_of_bounds = None
        self.image = pygame.Surface((config.CELL_LENGTH, config.CELL_LENGTH))
        self.image.set_colorkey(colors.BLACK)
        self.draw(self.image)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.board_to_screen(self.x, self.y)

    def get_sprite(self):
        """get_sprite method returns the sprite instance to be added to the
        handler sprite group.
        """
        return self

    def set_position(self, the_x, the_y):
        """set_position method sets the player instance in a new board
        position.
        """
        self.old_position = (self.x, self.y)
        self.x = the_x
        self.y = the_y

    def draw(self, the_screen):
        """draw method draws the player in the surface.
        """
        #center = (self.x + config.CELL_WIDTH / 2, self.y + config.CELL_LENGTH / 2)
        center = (config.CELL_WIDTH / 2, config.CELL_LENGTH / 2)
        ratio = (config.CELL_WIDTH / 2) - 2
        pygame.draw.circle(the_screen, colors.RED, center, ratio)

    def handle_keyboard_event(self, the_event, the_release_callback=None):
        """handle_keyboard_event method moves the player with the given
        keyboard inputs.
        """
        self.old_position = (self.x, self.y)
        if the_event.key == K_UP:
            self.y -= 1
        if the_event.key == K_DOWN:
            self.y += 1
        if the_event.key == K_LEFT:
            self.x -= 1
        if the_event.key == K_RIGHT:
            self.x += 1
        if the_event.key == K_RETURN and the_release_callback:
            the_release_callback("popup")
        if self.out_of_bounds and self.out_of_bounds(self.x, self.y):
            self.set_position(*self.old_position)
        self.rect.topleft = self.board_to_screen(self.x, self.y)
