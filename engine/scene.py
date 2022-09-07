"""scene.py module handles any scene added to the game.
"""

from . import ihandler


class Scene(ihandler.IHandler):
    """Scene class handles any scene in the game.
    """

    def __init__(self, **kwargs):
        """__init__ method initializes an Scene instance.
        
        - name attribute stores the name of the scene.
        """
        super().__init__(a_type="scene")
        self.name = kwargs.get("a_name", "")

    def open(self, **kwargs):
        """open method is called when a scene is activated the first
        time and it contains any functionality required to start the
        scene.
        """
        pass
    
    def close(self):
        """close method is called when a scene is deactivated and it
        contains any functionality required to end the scene.
        """
        pass
