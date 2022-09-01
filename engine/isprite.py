"""isprite.py module contains all common functionality for any object in the
game that contains an sprite.
"""

import uuid
import pygame
from . import idefaults


class ISprite(pygame.sprite.Sprite):
    """ISprite class contains all common attributes and functionality for any
    object in the game that contains an sprite.
    """

    def __init__(self, **kwargs):
        """__init__ method creates a new Isprite instance.

        - position attribute stores the graphical X and Y position where the
        sprite will be displayed.

        - previous_position attribute stores the graphical X and Y position
        where the sprite was previously displayed.

        - out_of_bounds function is called to check if the player is inside
        or outside the board.

        - width attribute stores the cell sprite width.

        - length attribute stores the cell sprite length.

        - border attribute stores if the cell sprite board (0 means it is
        filled with the color).

        - foreground_color attribute stores the pygame Color to be used to
        display the sprite.

        - background_color attribute stores the pygame Color to be used to
        display the sprite background.

        - key_color attribute stores the pygame Color to be used as keycolor
        for transparencies.

        - image pygame Surface instance is a derived attribute where the
        pygame Surface used to display the player sprite is stored.

        - rect pygame Rectangle instance is a derived attribute where the
        surface rectangle used to display the player sprite is stored.

        """
        super().__init__()
        self.position = kwargs.get("a_position", pygame.Vector2())
        self.previous_position = self.position
        self.width = kwargs.get("a_width", idefaults.DEFAULT_WIDTH)
        self.length = kwargs.get("a_length", idefaults.DEFAULT_LENGTH)
        self.border = kwargs.get("a_border", idefaults.DEFAULT_SPRITE_BORDER)
        self.foreground_color = kwargs.get("a_foreground_color", idefaults.DEFAULT_SPRITE_COLOR)
        self.background_color = kwargs.get("a_background_color", idefaults.DEFAULT_SPRITE_COLOR)
        self.key_color = kwargs.get("a_key_color", None)
        self.out_of_bounds = kwargs.get("a_out_of_bounds", None)
        self.image = pygame.Surface((self.width, self.length))
        if self.key_color:
            self.image.set_colorkey(self.key_color)
        self.draw_sprite(self.image)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.position

    def draw_sprite(self, a_screen):
        """draw_sprite method is a virtual method to be overwritten in
        any derived class with the actual sprite drawing information.
        """
        pass

    def get_sprite(self):
        """get_sprite method returns the sprite instance to be added to the
        handler sprite group.
        """
        return self
