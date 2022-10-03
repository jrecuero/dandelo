"""player.py module implements all classes related with the game player.
"""

import os
import pygame
from pygame.locals import *
from engine import icolors
from engine import idefaults
from engine import bobject
from engine import isprite
from engine import gevent
from engine import support
from engine import itimer
from . import config


class PlayerSprite(isprite.ISprite):
    """PlayerSprite class implements the players sprite to be displayed in the
    screen inside the board.
    """

    def __init__(self, **kwargs):
        """__init__ method creates a new PlayerSprite instance.
        """
        super().__init__(**kwargs)
        self.animations = {"idle": [], "attack": []}
        for l_animation in self.animations.keys():
            v_animation_path = os.path.join("game/graphics/player", l_animation)
            self.animations[l_animation] = support.import_images_from_path(v_animation_path)
        self.animation_index = 0.0
        self.animation_action = "idle"
        self.image = self.animations[self.animation_action][int(self.animation_index)]
        self.rect = self.image.get_rect()
        self.rect.topleft = self.position


    def update(self, a_fps):
        """update method is called by the sprite group.
        """
        v_number_images = len(self.animations[self.animation_action])
        v_animation_per_second = 2
        self.animation_index += v_number_images * v_animation_per_second / a_fps
        if self.animation_index >= v_number_images:
            self.animation_index = 0.0
        self.image = self.animations[self.animation_action][int(self.animation_index)]
        


class Player(bobject.BObject):
    """Player class implements the main player in the board.
    """

    def __init__(self, **kwargs):
        """__init__ method initializes a Player instance.
        """
        super().__init__(**kwargs)
        # self.sprite = PlayerSprite(a_position=self.board_to_screen(self.board_position),
        self.sprite = PlayerSprite(a_position=self.position,
            a_width=idefaults.DEFAULT_WIDTH,
            a_length=idefaults.DEFAULT_LENGTH,
            a_foreground_color=icolors.RED,
            a_key_color=idefaults.DEFAULT_SPRITE_COLOR)
        self.previous_position = None

    def set_position(self, a_position):
        """set_position method sets the player instance in a new board
        position.
        """
        # self.previous_position = self.board_position.copy()
        self.set_board_position(a_position)

    def handle_keyboard_event(self, a_event):
        """handle_keyboard_event method moves the player with the given
        keyboard inputs.
        """
        def stop_attack_animation(**kwargs):
            self.sprite.animation_action = "idle"

        self.previous_position = self.board_position.copy()
        v_result = a_event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT, K_SPACE, K_RETURN]
        if a_event.key == K_UP:
            self.board_position.y -= 1
            self.sprite.animation_action = "idle"
        if a_event.key == K_DOWN:
            self.board_position.y += 1
            self.sprite.animation_action = "idle"
        if a_event.key == K_LEFT:
            self.sprite.animation_action = "idle"
            self.board_position.x -= 1
        if a_event.key == K_RIGHT:
            self.sprite.animation_action = "idle"
            self.board_position.x += 1
        if a_event.key == K_SPACE:
            self.sprite.animation_action = "attack"
            v_timer = itimer.Timer("attack", 500, stop_attack_animation)
            v_timer.activate()
            self.notifier(gevent.GEvent("action/parent/timer:create/now", {"object": self, "timer": v_timer}))
        if a_event.key == K_RETURN:
            v_position = self.board_to_screen(self.board_position)
            self.notifier(gevent.GEvent("action/top/scene:this", {"object": self, "scene":config.SCENE_POPUP, "position": v_position}))
        if self.out_of_bounds and self.out_of_bounds(self.board_position):
            self.set_position(self.previous_position)
        # self.sprite.rect.topleft = self.board_to_screen(self.board_position)
        self.sprite.rect.topleft = self.position
        return v_result
