"""engine.py module contains all the engine framework functionality.
"""

import pygame
from pygame.locals import *
from . import icolors
from . import handler


class Engine:
    """Engine class contains all the engine framework.
    """

    def __init__(self, a_name, a_fps):
        """___init__ method creates a new Engine instance.

        - name attribute stores the engine name, used as a screen caption.

        - fps attribute stores the frame per second to be used in the clock.

        - handler attribute stores the GameHandler instance.

        - clock attribute stores the pygame clock used to keep frame per
        second constant.

        - screen attribute stores the pygame Surface used to display any 
        sprite.

        - is_running attribute stores the flag showing if the engine has to
        keep running.
        """
        self.name = a_name
        self.fps = a_fps
        self.handler = None
        self.clock = None
        self.screen = None
        self.is_running = False

    def init(self):
        """init method initializes the engine.
        """
        pygame.init()
        self.clock = pygame.time.Clock()
        self.handler = handler.GameHandler()
        pygame.display.set_caption(self.name)
        self.screen = pygame.display.set_mode((640, 480))

    def run(self):
        """run method runs the engine.
        """
        self.is_running = True
        while self.is_running:
            self.screen.fill(icolors.WHITE)
            self.handler.draw(self.screen)
            pygame.display.update()
            for l_event in pygame.event.get():
                if l_event.type == QUIT:
                    self.is_running = False
                if l_event.type == KEYDOWN:
                    self.handler.handle_keyboard_event(l_event)
            self.handler.update()
            self.handler.handle_all_events()
            self.clock.tick(self.fps)
        pygame.quit()        