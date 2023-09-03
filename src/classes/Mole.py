import pygame
import random

from classes.Time import Time
from constants.AssetPath import ImagePath
from constants.GameConfig import ScreenSize


class Mole:
    def __init__(self, position: tuple):
        self.body = pygame.image.load(ImagePath.MOLE_BODY)

        self.initialPosition = (
            position[0] - self.body.get_size()[0] / 2,
            position[1] - self.body.get_size()[1] / 2,
        )

        self.renderPosition = self.initialPosition

        self.body.fill(
            (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
            ),
            special_flags=pygame.BLEND_RGB_MULT,
        )

        self.isHide = True
        self.hide()

        self.timer = 0
        self.timer = random.random() * 3 + 1

    def update(self, screen: pygame.Surface):
        screen.blit(self.body, self.renderPosition)

        self.timer -= Time.deltaTime

        if self.timer < 0:
            if self.isHide:
                self.show()
            else:
                self.hide()

    def show(self):
        self.isHide = False
        self.timer = 2
        self.renderPosition = self.initialPosition

    def hide(self):
        self.isHide = True
        self.timer = random.random() * 2 + 1
        self.renderPosition = (self.initialPosition[0], self.initialPosition[1] + 52)
