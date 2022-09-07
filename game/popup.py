"""popup.py module contains the object that contains the popup menu sprite.
"""

import pygame
from pygame.locals import *
from engine import gobject
from engine import menu
from engine import gevent


class PopUp(gobject.GObject):
    """PopUp class contains the object that contains the popup menu sprite.
    """

    def __init__(self, a_position=pygame.Vector2()):
        """__init__ method creates a new PopUp instance.
        """
        super().__init__()
        self.position = a_position
        self.sprite = menu.PopUpMenu(self.position, ["open", "world", "battle", "end"])

    def set_position(self, a_position):
        """set_position method sets a new position for the object.
        """
        self.position = a_position
        self.sprite.set_position(a_position)

    def handle_keyboard_event(self, a_event):
        """handle_keyboard_event method moves the player with the given
        keyboard inputs.
        """
        v_selected = self.sprite.handle_keyboard_event(a_event)
        if v_selected is not None:
            self.notifier(gevent.GEvent("action/top/scene:end", {"object": self, "selected": v_selected}))
        return True
