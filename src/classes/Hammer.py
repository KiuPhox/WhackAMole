import pygame
import random

from constants.AssetPath import ImagePath
from constants.GameConfig import ScreenSize


class Hammer:
    def __init__(self):
        self.image = pygame.image.load(ImagePath.HAMMER)
        self.image = pygame.transform.rotate(self.image, 45)

    def update(self, screen: pygame.Surface):
        mouse_pos = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed()[0]:
            screen.blit(
                pygame.transform.rotate(self.image, 45),
                (
                    mouse_pos[0] - self.image.get_size()[0] / 2,
                    mouse_pos[1] - self.image.get_size()[1] / 2,
                ),
            )
        else:
            screen.blit(
                self.image,
                (
                    mouse_pos[0] - self.image.get_size()[0] / 2,
                    mouse_pos[1] - self.image.get_size()[1] / 2,
                ),
            )
