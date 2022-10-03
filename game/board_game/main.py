"""main.py module is the game main module.
"""

import sys
# import pygame
from game.board_game import config
from game.board_game import gameplay
from engine import engine


def main():
    """main function is the main game function.
    """
    # pygame.init()
    v_engine = engine.Engine("dandelo", config.FPS)
    v_engine.init(config.WIDTH, config.LENGTH)
    gameplay.create_board_scene(v_engine.handler)
    gameplay.create_menu_scene(v_engine.handler)
    v_engine.run()
    sys.exit()


if __name__ == "__main__":
    main()
