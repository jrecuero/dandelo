"""iobject.py module contains the interface with common functionality for
any object created in the game.
"""

import uuid


class IObject:
    """IObject class contains all common attributes and functionality for any
    object created in the game.
    """

    def __init__(self, a_name=None, a_sprite=None):
        """__init__ method creates an IObject instance.

        - uuid attribute stores the object unique identifier.

        - name attribute stores the optional object name.

        - sprite pygame Sprite keeps an optional sprite to be displayed for
        the game object.
        """
        self.uid = str(uuid.uuid1())
        self.name = a_name if a_name else self.uid
        self.sprite = a_sprite

    def get_sprite(self):
        """get_sprite method returns the sprite instance to be added to the
        handler sprite group.
        """
        return self.sprite
