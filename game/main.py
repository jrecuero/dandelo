"""main.py module is the game main module.
"""

import sys
import pygame
from engine import engine
from game import config
from game import gameplay

def main():
    """main function is the main game function.
    """
    #pygame.init()
    v_engine = engine.Engine("dandelo", config.FPS)
    v_engine.init()
    gameplay.create_board_scene(v_engine.handler)
    gameplay.create_menu_scene(v_engine.handler)
    v_engine.run()
    sys.exit()


if __name__ == "__main__":
    main()
