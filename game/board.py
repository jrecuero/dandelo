"""board.py module implements all classes related with game and graphic board.
"""

import random
import pygame
import colors
import config
import isprite


class Board:
    """Board class implements the board where the player will move and act.
    """

    def __init__(self, a_x_origin, a_y_origin, a_cell_width, a_cell_length):
        """__init__method initializes a Board instance.

        - x_origin attribute stores the graphical X position where board
        should be displayed.

        -y_origin attribute stores the graphical Y position where board
        should be displayed.

        - cell_width attribute stores the width for any graphical cell in the
        board.

        - cell_length attribute stores the length for any graphical cell in the
        board.

        - cells list stores all board cells.

        - sprite_group pygame Group contains sprites for all cells in the
        board.

        - size attribute contains the size for any square regular board (same
        width and length).
        """
        self.x_origin = a_x_origin
        self.y_origin = a_y_origin
        self.cell_width = a_cell_width
        self.cell_length = a_cell_length
        self.cells = []
        self.sprite_group = pygame.sprite.Group()
        self.size = None

    def get_sprite(self):
        """get_sprite method returns the sprite instance to be added to the
        handler sprite group.
        """
        return self.sprite_group

    def board_to_screen(self, a_position):
        """board_to_screen method translates some board coordinates to screen
        coordinates.
        """
        return (a_position.x * self.cell_width + self.x_origin, a_position.y * self.cell_length + self.y_origin)

    def screen_to_board(self, a_position):
        """screen_to_board method translates some screen coordinates to board
        coordinates.
        """
        return ((a_position.x - self.x_origin) / self.width, (a_position.y - self.y_origin) / self.length)

    def in_bounds(self, a_position):
        """in_bounds method checks if the given board coordinates are inside
        the board.
        """
        return (0 <= a_position.x < self.size) and (0 <= a_position.y < self.size)

    def out_of_bounds(self, a_position):
        """out_of_bounds method checks if the given board coordinates are
        outside the board.
        """
        #return (a_x < 0) or (a_x >= self.size) or (a_y < 0) or (a_y >= self.size)
        return not(self.in_bounds(a_position))

    def create_default_board(self, a_number_of_cells=8):
        """create_default_board method creates a default square board with the
        given ratio.
        """
        self.size = a_number_of_cells
        for row in range(a_number_of_cells):
            for column in range(a_number_of_cells):
                cell_spec = {
                        "x": row,
                        "y": column,
                        "color": colors.BLUE,
                        # "color": random.choice([colors.BLACK, colors.RED, colors.GREEN, colors.BLUE, colors.WHITE]),
                        "gx": self.x_origin + self.cell_width * row,
                        "gy": self.y_origin + self.cell_length * column,
                        "width": self.cell_width,
                        "length": self.cell_length,
                        "border": 0,
                        }
                cell = BCell(cell_spec)
                self.cells.append(cell)
                self.sprite_group.add(cell.gcell)

    def draw(self, a_screen):
        """draw method draws all board cells in the surface.
        """
        #for cell in self.cells:
        #    cell.draw(a_screen)
        self.sprite_group.draw(a_screen)


class BCell:
    """BCell class implements the cells that will be in a board.
    """

    def __init__(self, a_specs):
        """__init__ method initializes a BCell instance.
        """
        self.x = a_specs.get("x", 0)
        self.y = a_specs.get("y", 0)
        self.color = a_specs.get("color", colors.BLACK)
        self.gx = a_specs.get("gx", 0)
        self.gy = a_specs.get("gy", 0)
        self.gwidth = a_specs.get("width", config.CELL_WIDTH)
        self.glength = a_specs.get("length", config.CELL_LENGTH)
        self.gborder = a_specs.get("border", 1)
        self.gcell = GCell(a_foreground_color=self.color,
            a_position=pygame.Vector2(self.gx, self.gy),
            a_width=self.gwidth,
            a_length=self.glength,
            a_border=self.gborder)


class GCell(isprite.ISprite):
    """GCell class implements the cells that will be displayed in a graphical
    board.
    """

    def __init__(self, **kwargs):
        """__init__ method initializes a GCell instance.

        - x attribute stores the graphical X position where cell sprite should
        be displayed.

        - y attribute stores the graphical Y position where cell sprite should
        be displayed.

        - width attribute stores the cell sprite width.

        - length attribute stores the cell sprite length.

        - color attribute stores the pygame Color to be used to display the
        cell sprite.

        - border attribute stores if the cell sprite board (0 means it is
        filled with the color).

        - image pygame Surface instance is a derived attribute where the
        pygame Surface used to display the cell sprite is stored.

        - rect pygame Rectangle instance is a derived attribute where the
        surface rectangle used to display the cell sprite is stored.
        """
        super().__init__(**kwargs)

    def draw_sprite(self, a_screen):
        """draw method draws the cell board in the surface.
        """
        rect = (0, 0, self.width, self.length)
        pygame.draw.rect(a_screen, self.foreground_color, rect, self.border)
        if self.border == 0:
            pygame.draw.rect(a_screen, self.background_color, rect, 1)
