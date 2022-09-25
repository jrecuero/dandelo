"""iobject.py module contains the interface with common functionality for
any object created in the game.
"""

import uuid


class IObject:
    """IObject class contains all common attributes and functionality for any
    object created in the game.
    """

    def __init__(self, a_name=None):
        """__init__ method creates an IObject instance.

        - uuid attribute stores the object unique identifier.

        - name attribute stores the optional object name.

        - notifier attribute keeps the callback to be used to notify events to
        the proper parent.

        - opened attribute keeps the status if the object has been already
        activated in a scene.
        """
        self.uid = str(uuid.uuid1())
        self.name = a_name if a_name else self.uid
        self.notifier = None
        self.opened = False

    def open(self, a_handler):
        """open method is a virtual call done by the handler the first time
        the object is being activated in the scene.
        """
        self.opened = True
    
    def close(self, a_handler):
        """close method is a virtual call done by the handler when the scene
        where object is places is deactivated.
        """
        self.opened = False