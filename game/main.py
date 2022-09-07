"""main.py module is the game main module.
"""

import sys
import pygame
from pygame.locals import *
from engine import icolors
from engine import idefaults
from engine import board
from engine import ihandler
from engine import handler
from engine import scene
from engine import menu
from engine import idefaults
from engine import engine
from engine import gevent
from game import config
from game import player
from game import popup


class BoardScene(scene.Scene):
    """BoardScene class contains all functionality to create the board
    scene.
    """

    def __init__(self, **kwargs):
        """__init__ method creates a new BoardScene instance.
        """
        super().__init__(a_name=config.SCENE_BOARD, **kwargs)

    #def handle_end_scene(self, a_object):
    #    """handle_end_scene method handles the end of the scene.
    #    """
    #    def _inner_(**kwargs):            
    #        kwargs = {"object": a_object}
    #        return "action/scene/end", kwargs
    #    return _inner_

    @ihandler.callback
    def handle_end_scene(self, **kwargs):
        """handle_end_scene method handles the end of the scene.
        """
        return gevent.GEvent("action/scene/end", kwargs)

    def end_scene(self, **kwargs):
        """end_scene method ends the scene.
        """
        return "action/scene/end", kwargs


class PopUpMenuScene(scene.Scene):
    """PopUpMenuScene class contains all functionality to create the popup
    menu scene.
    """

    def __init__(self, **kwargs):
        """__init__ method creates a new PopUpMenuScene instance.
        """
        super().__init__(a_name=config.SCENE_POPUP)
        self.position = None

    def open(self, **kwargs):
        """open method is called when a scene is activated the first
        time and it contains any functionality required to start the
        scene.
        """
        self.position = kwargs.get("position", self.position)
        self.objects[0].set_position(self.position)
    
    def end_scene(self):
        """end_scene method ends the scene.
        """
        print(self, " end the scene")


def handle_scene_this(a_event):
    """handler_scene_this function handles action scene:this.
    """
    v_handler = a_event.handler
    if v_handler is None:
        return False
    print(a_event)
    v_scene = v_handler.get_scene_by_name(config.SCENE_POPUP)
    if v_scene is None:
        return False        
    v_handler.activate_this_scene(v_scene, **a_event.data)
    return True

def handle_scene_end(a_event):
    """handler_scene_end function handles action scene:end.
    """
    v_handler = a_event.handler
    if v_handler is None:
        return False
    print("menu selected ", a_event.data["selected"])
    v_handler.end_active_and_reactivate_next()
    return True

def create_board_scene(a_game_handler):
    """create_board_scene function creates the game board scene.
    """
    v_game_board = board.Board(10, 10, idefaults.DEFAULT_WIDTH, idefaults.DEFAULT_LENGTH)
    v_game_board.create_default_board(8)
    v_game_player = player.Player(a_position=pygame.Vector2(), a_board_to_screen=v_game_board.board_to_screen)
    v_game_player.out_of_bounds = v_game_board.out_of_bounds
    v_board_scene = BoardScene()
    v_board_scene.add_object(v_game_board)
    v_board_scene.add_object(v_game_player)
    v_board_scene.keyboard_control_object = v_game_player
    #v_board_scene.keyboard_release_callback = a_game_handler.release_player()
    v_board_scene.keyboard_release_callback = v_board_scene.handle_end_scene
    #v_board_scene.add_action("scene/end", v_board_scene.end_scene)
    a_game_handler.add_scene(v_board_scene)
    a_game_handler.activate_this_scene(v_board_scene)
    a_game_handler.add_action("scene:this", handle_scene_this)

def create_menu_scene(a_game_handler):
    """create_menu_scene function creates the game menu scene.
    """
    #v_game_menu = menu.PopUpMenu((300, 10), ["open", "world", "battle", "end"])
    v_game_popup_menu = popup.PopUp()
    v_menu_scene = PopUpMenuScene()
    v_menu_scene.add_object(v_game_popup_menu)
    v_menu_scene.keyboard_control_object = v_game_popup_menu
    a_game_handler.add_scene(v_menu_scene)
    a_game_handler.add_action("scene:end", handle_scene_end)


def main():
    """main function is the main game function.
    """
    #pygame.init()
    v_engine = engine.Engine("dandelo", config.FPS)
    v_engine.init()
    create_board_scene(v_engine.handler)
    create_menu_scene(v_engine.handler)
    v_engine.run()
    sys.exit()


if __name__ == "__main__":
    main()
