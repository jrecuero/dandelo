"""gameplay.py modules contains the main gameplay.
"""

from . import config
from . import board_scene
from . import popup_scene


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
    v_board_scene = board_scene.BoardScene()
    a_game_handler.add_scene(v_board_scene)
    a_game_handler.activate_this_scene(v_board_scene)
    a_game_handler.add_action("scene:this", handle_scene_this)


def create_menu_scene(a_game_handler):
    """create_menu_scene function creates the game menu scene.
    """
    v_menu_scene = popup_scene.PopUpMenuScene()
    a_game_handler.add_scene(v_menu_scene)
    a_game_handler.add_action("scene:end", handle_scene_end)
