"""scene.py module handles any scene added to the game.
"""

import ihandler


class Scene(ihandler.IHandler):
    """Scene class handles any scene in the game.
    """

    def __init__(self):
        """__init__ method initializes an Scene instance.
        """
        super().__init__()
