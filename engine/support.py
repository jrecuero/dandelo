"""support.py module contains all support methods.
"""

import os
import pygame

def import_images_from_path(a_path):
    """import_images_from_path function import all image files from aa given
    path.
    """
    v_image_list = list()
    for _, _, l_image_files in os.walk(a_path):
        for l_image in l_image_files:
            v_image_path = os.path.join(a_path, l_image)
            v_image = pygame.image.load(v_image_path).convert_alpha()
            v_image_list.append(v_image)
    return v_image_list
