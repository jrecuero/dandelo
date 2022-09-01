"""dice.py module implements a game dices functionality.
"""

import pygame
import random


class Dice(pygame.sprite.Sprite):
    """Dice class implements a game dice.
    """

    def __init__(self, a_sides=20):
        """___init__ method initializes a Dice instance.

        - sides attribute stores the dice number of sides.
        """
        super().__init__()

        self.sides = a_sides

    def roll(self):
        """roll method rolls a dice.
        """
        return random.randint(0, self.sides)
