"""iobject.py module contains the interface with common functionality for
any object created in the game.
"""

import uuid


class IObject:
    """IObject class contains all common attributes and functionality for any
    object created in the game.
    """

    def __init__(self, the_name=None, the_sprite=None):
        """__init__ method creates an IObject instance.

        - uuid attribute stores the object unique identifier.

        - name attribute stores the optional object name.

        - sprite pygame Sprite keeps an optional sprite to be displayed for
        the game object.
        """
        self.uid = str(uuid.uuid1())
        self.name = the_name if the_name else self.uuid
        self.sprite = the_sprite