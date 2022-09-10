"""popup_scene.py module contains the PopUp Menu scene.
"""

from engine import scene
from . import config
from . import popup

class PopUpMenuScene(scene.Scene):
    """PopUpMenuScene class contains all functionality to create the popup
    menu scene.
    
    - position attribute contains screen X and Y coordinates where scene should
    be displayed.

    - popup_menu attribute contains the PopUpMenu instance with the popup menu
    to be displayed in the scenario.
    """

    def __init__(self, **kwargs):
        """__init__ method creates a new PopUpMenuScene instance.
        """
        super().__init__(a_name=config.SCENE_POPUP)
        self.position = None
        self.popup_menu = popup.PopUp()
        self.add_object(self.popup_menu)
        self.keyboard_control_object = self.popup_menu

    def open(self, **kwargs):
        """open method is called when a scene is activated the first
        time and it contains any functionality required to start the
        scene.
        """
        self.position = kwargs.get("position", self.position)
        self.popup_menu.set_position(self.position)
    
    def end_scene(self):
        """end_scene method ends the scene.
        """
        print(self, " end the scene")

