"""menu.py module implements most of generics menus used in the game.
"""

import pygame
from pygame.locals import *
import colors


class PopUpMenu(pygame.sprite.Sprite):
    """PopUpMenu class implements a generic pop up menus with multiple
    options.
    """

    def __init__(self, the_position, the_options):
        """__init__ methods initializes a PopUpMenu instance with the given
        options (list).

        - position attribute stores the position in the display where the pop
        up menu has to be placed.

        - options list contains a list with all strings to be displayed in the
        pop up menu.

        - selected attribute marks the index of the options being selected at
        any time.

        - font_size attribute stores the size of the pygame font to be used.

        - font attribute stores the pygame font being used.

        - padding attribute stores the padding between any string displayed for
        every option.

        - width attribute stores the width for the popup menu.

        - length attribute stores the length for the popup menu

        - image pygame Surface instance is a derived attribute where the
        pygame Surface used to display the popup menu is stored.

        - rect pygame Rectangle instance is a derived attribute where the
        surface rectangle used to display the popup menu is stored.
        """
        super().__init__()
        self.position = the_position
        self.options = the_options
        self.selected = 0
        self.font_size = 24
        self.font = pygame.font.SysFont("arial", self.font_size)
        max_width = max(map(lambda x: self.font.size(x)[0], self.options))
        self.padding = 4
        self.width = max_width + 8 * self.padding
        self.length = self.font_size + 2 * self.padding
        self.image = pygame.Surface((self.width, self.length * len(self.options)))
        self.draw()
        self.rect = self.image.get_rect()        
        self.rect.topleft = the_position

    def get_sprite(self):
        """get_sprite method returns the sprite instance to be added to the
        handler sprite group.
        """
        return self

    def draw(self):
        """draw methods displays the menu in the surface.
        """
        self.image.fill(colors.WHITE)
        background_color = colors.WHITE
        foreground_color = colors.BLUE
        y = 0
        for index, option in enumerate(self.options):
            if index == self.selected:
                background_color = colors.BLUE
                foreground_color = colors.WHITE
            else:
                background_color = colors.WHITE
                foreground_color = colors.BLUE
            pygame.draw.rect(self.image, background_color, (0, y, self.width, self.length))
            pygame.draw.rect(self.image, colors.BLACK, (0, y, self.width, self.length), 1)
            option_image = self.font.render(option, True, foreground_color)
            self.image.blit(option_image, (self.padding, y + self.padding))
            y += self.length

    def handle_keyboard_event(self, the_event, the_release_callback=None):
        """handle_keyboard_event method moves the player with the given
        keyboard inputs.
        """
        if the_event.key == K_UP:
            if self.selected != 0:
                self.selected -= 1
        if the_event.key == K_DOWN:
            if self.selected < len(self.options) - 1:
                self.selected += 1
        if the_event.key == K_RETURN and the_release_callback:
            print("option {} was selected".format(self.options[self.selected]))
            the_release_callback("player")
        self.draw()

    def update(self):
        """update method is called by the sprite Group.
        """
        # This is the mouse click implementation.
        #if self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        #    print("option {} was selected".format(self.options[self.selected]))
        pass
    