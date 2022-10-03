"""title_scene.py module contains all functionality for the main title scene.
"""

import pygame
from engine import icolors
from engine import scene
from engine import gobject


class Title(pygame.sprite.Sprite):
    """Title class implements the title sprite.
    """

    def __init__(self):
        """__init__ method creates a new Title instance.
        """
        super().__init__()
        self.font_size = 48
        self.font = pygame.font.SysFont("arial", self.font_size)
        self.image = pygame.Surface((640, 480))
        self.image.fill(icolors.WHITE)
        title_image = self.font.render("Dandelo", True, icolors.BLUE)
        self.image.blit(title_image, (300, 240))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)


class TitleScene(scene.Scene):
    """TitleScene class contains all functionality for the title scene.
    """

    def __init__(self):
        """__init__ method creates a new TitleScene instance.
        """
        super().__init__()
        self.title = gobject.GObject(a_sprite=Title())
        self.add_object(self.title)
