import pygame
import random

from constants.AssetPath import ImagePath
from constants.GameConfig import ScreenSize


class Mole:
    def __init__(self, position: tuple):
        self.body = pygame.image.load(ImagePath.MOLE_BODY)

        self.position = (
            position[0] - self.body.get_size()[0] / 2,
            position[1] - self.body.get_size()[1] / 2,
        )

        # fill random color
        self.body.fill(
            (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
            ),
            special_flags=pygame.BLEND_RGB_MULT,
        )

        self.show = False

    def update(self, screen: pygame.Surface):
        screen.blit(self.body, self.position)

    def show(self):
        self.show = True

    def hide(self):
        self.show = False
