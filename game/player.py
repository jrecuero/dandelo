"""player.py module implements all classes related with the game player.
"""

from engine import icolors
import pygame
from pygame.locals import *
from engine import idefaults
from engine import bobject
from engine import isprite


class PlayerSprite(isprite.ISprite):
    """PlayerSprite class implements the players sprite to be displayed in the
    screen inside the board.
    """

    def __init__(self, **kwargs):
        """__init__ method creates a new PlayerSprite instance.
        """
        super().__init__(**kwargs)

    def draw_sprite(self, a_screen):
        """draw method draws the player sprite in the surface.
        """
        center = (self.width / 2, self.length / 2)
        ratio = (self.width / 2) - 2
        pygame.draw.circle(a_screen, self.foreground_color, center, ratio)


class Player(bobject.BObject):
    """Player class implements the main player in the board.
    """

    def __init__(self, **kwargs):
        """__init__ method initializes a Player instance.
        """
        super().__init__(**kwargs)
        self.sprite = PlayerSprite(a_position=self.board_to_screen(self.position),
            a_width=idefaults.DEFAULT_WIDTH,
            a_length=idefaults.DEFAULT_LENGTH,
            a_foreground_color=icolors.RED,
            a_key_color=idefaults.DEFAULT_SPRITE_COLOR)

    def set_position(self, a_position):
        """set_position method sets the player instance in a new board
        position.
        """
        self.previous_position = self.position
        self.position = a_position

    def handle_keyboard_event(self, a_event, a_release_callback=None):
        """handle_keyboard_event method moves the player with the given
        keyboard inputs.
        """
        self.previous_position = self.position
        if a_event.key == K_UP:
            self.position.y -= 1
        if a_event.key == K_DOWN:
            self.position.y += 1
        if a_event.key == K_LEFT:
            self.position.x -= 1
        if a_event.key == K_RIGHT:
            self.position.x += 1
        if a_event.key == K_RETURN and a_release_callback:
            a_release_callback("popup")
        if self.out_of_bounds and self.out_of_bounds(self.position):
            self.set_position(*self.old_position)
        self.sprite.rect.topleft = self.board_to_screen(self.position)
