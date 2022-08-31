"""board.py module implements all classes related with game and graphic board.
"""

import random
import pygame
import colors
import config


class Board:
    """Board class implements the board where the player will move and act.
    """

    def __init__(self, the_x_origin, the_y_origin, the_cell_width, the_cell_length):
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
        self.x_origin = the_x_origin
        self.y_origin = the_y_origin
        self.cell_width = the_cell_width
        self.cell_length = the_cell_length
        self.cells = []
        self.sprite_group = pygame.sprite.Group()
        self.size = None

    def get_sprite(self):
        """get_sprite method returns the sprite instance to be added to the
        handler sprite group.
        """
        return self.sprite_group

    def board_to_screen(self, the_x, the_y):
        """board_to_screen method translates some board coordinates to screen
        coordinates.
        """
        return (the_x * self.cell_width + self.x_origin, the_y * self.cell_length + self.y_origin)

    def screen_to_board(self, the_x, the_y):
        """screen_to_board method translates some screen coordinates to board
        coordinates.
        """
        return ((the_x - self.x_origin) / self.width, (the_y - self.y_origin) / self.length)

    def in_bounds(self, the_x, the_y):
        """in_bounds method checks if the given board coordinates are inside
        the board.
        """
        return (0 <= the_x < self.size) and (0 <= the_y < self.size)

    def out_of_bounds(self, the_x, the_y):
        """out_of_bounds method checks if the given board coordinates are
        outside the board.
        """
        #return (the_x < 0) or (the_x >= self.size) or (the_y < 0) or (the_y >= self.size)
        return not(self.in_bounds(the_x, the_y))

    def create_default_board(self, the_number_of_cells=8):
        """create_default_board method creates a default square board with the
        given ratio.
        """
        self.size = the_number_of_cells
        for row in range(the_number_of_cells):
            for column in range(the_number_of_cells):
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

    def draw(self, the_screen):
        """draw method draws all board cells in the surface.
        """
        #for cell in self.cells:
        #    cell.draw(the_screen)
        self.sprite_group.draw(the_screen)


class BCell:
    """BCell class implements the cells that will be in a board.
    """

    def __init__(self, the_specs):
        """__init__ method initializes a BCell instance.
        """
        self.x = the_specs.get("x", 0)
        self.y = the_specs.get("y", 0)
        self.color = the_specs.get("color", colors.BLACK)
        self.gx = the_specs.get("gx", 0)
        self.gy = the_specs.get("gy", 0)
        self.gwidth = the_specs.get("width", config.CELL_WIDTH)
        self.glength = the_specs.get("length", config.CELL_LENGTH)
        self.gborder = the_specs.get("border", 1)
        self.gcell = GCell(self.color, self.gx, self.gy, self.gwidth, self.glength, self.gborder)


    def draw(self, the_screen):
        """draw method draws the graphical cell in the surface.
        """
        self.gcell.draw(the_screen)


class GCell(pygame.sprite.Sprite):
    """GCell class implements the cells that will be displayed in a graphical
    board.
    """

    def __init__(self, the_color, the_x, the_y, the_width, the_length, the_border=1):
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
        super().__init__()
        self.x = the_x
        self.y = the_y
        self.width = the_width
        self.length = the_length
        self.color = the_color
        self.border = the_border
        self.image = pygame.Surface((self.width, self.length))
        self.draw(self.image)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

    def draw(self, the_screen):
        """draw method draws the cell board in the surface.
        """
        #rect = (self.x, self.y, self.width, self.length)
        rect = (0, 0, self.width, self.length)
        pygame.draw.rect(the_screen, self.color, rect, self.border)
        if self.border == 0:
            pygame.draw.rect(the_screen, colors.BLACK, rect, 1)
