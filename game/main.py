"""main.py module is the game main module.
"""

import sys
import pygame
from pygame.locals import *
import board
import colors
import config
import player
import handler
import scene
import menu

def create_board_scene(game_handler):
    """create_board_scene function creates the game board scene.
    """
    game_board = board.Board(10, 10, config.CELL_WIDTH, config.CELL_LENGTH)
    game_board.create_default_board(8)
    game_player = player.Player(0, 0, game_board.board_to_screen)
    game_player.out_of_bounds = game_board.out_of_bounds
    board_scene = scene.Scene()
    board_scene.add_object(game_board)
    board_scene.add_object(game_player)
    board_scene.keyboard_control_object = game_player
    board_scene.keyboard_release_callback = game_handler.release_player()
    game_handler.add_scene(board_scene)
    game_handler.activate_scene(board_scene)

def create_menu_scene(game_handler):
    """create_menu_scene function creates the game menu scene.
    """
    game_menu = menu.PopUpMenu((300, 10), ["open", "world", "battle", "end"])
    menu_scene = scene.Scene()
    menu_scene.add_object(game_menu)
    menu_scene.keyboard_control_object = game_menu
    menu_scene.keyboard_release_callback = game_handler.release_menu()


def create_game():
    """create_scenario function creates the game scenario.
    """
    game_handler = handler.GameHandler()
    return game_handler


def main():
    """main function is the main game function.
    """
    pygame.init()
    frame_per_second = pygame.time.Clock()
    pygame.display.set_caption("dandelo")
    screen = pygame.display.set_mode((640, 480))
    running = True
    game_handler = create_game()
    create_board_scene(game_handler)
    create_menu_scene(game_handler)
    while running:
        screen.fill(colors.WHITE)
        game_handler.draw(screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                game_handler.handle_keyboard_event(event)
        game_handler.update()
        frame_per_second.tick(config.FPS)
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
