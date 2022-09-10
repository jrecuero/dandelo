"""player.py module implements all classes related with the game player.
"""

from engine import icolors
import pygame
from pygame.locals import *
from engine import idefaults
from engine import bobject
from engine import isprite
from engine import gevent
from . import config


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
        #self.sprite = PlayerSprite(a_position=self.board_to_screen(self.board_position),
        self.sprite = PlayerSprite(a_position=self.position,
            a_width=idefaults.DEFAULT_WIDTH,
            a_length=idefaults.DEFAULT_LENGTH,
            a_foreground_color=icolors.RED,
            a_key_color=idefaults.DEFAULT_SPRITE_COLOR)

    def set_position(self, a_position):
        """set_position method sets the player instance in a new board
        position.
        """
        #self.previous_position = self.board_position.copy()
        self.set_board_position(a_position)

    def handle_keyboard_event(self, a_event):
        """handle_keyboard_event method moves the player with the given
        keyboard inputs.
        """
        self.previous_position = self.board_position.copy()
        v_result = a_event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT, K_RETURN]
        if a_event.key == K_UP:
            self.board_position.y -= 1
        if a_event.key == K_DOWN:
            self.board_position.y += 1
        if a_event.key == K_LEFT:
            self.board_position.x -= 1
        if a_event.key == K_RIGHT:
            self.board_position.x += 1
        if a_event.key == K_RETURN:
            v_position = self.board_to_screen(self.board_position)
            self.notifier(gevent.GEvent("action/top/scene:this", {"object": self, "scene":config.SCENE_POPUP, "position": v_position}))
        if self.out_of_bounds and self.out_of_bounds(self.board_position):
            self.set_position(self.previous_position)
        #self.sprite.rect.topleft = self.board_to_screen(self.board_position)
        self.sprite.rect.topleft = self.position
        return v_result
