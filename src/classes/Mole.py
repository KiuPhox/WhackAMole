import pygame
import random

from classes.Time import Time
from constants.AssetPath import ImagePath


class Mole:
    def __init__(self, position: tuple):
        self.body = pygame.image.load(ImagePath.MOLE_BODY)

        self.initialPosition = (
            position[0] - self.body.get_size()[0] / 2,
            position[1] - self.body.get_size()[1] / 2,
        )

        self.actualPosition = self.initialPosition
        self.renderPosition = self.initialPosition
        self.rect = pygame.Rect(self.initialPosition, self.body.get_size())

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
        self.timer = random.random() * 3 + 2

    def update(self, screen: pygame.Surface):
        # lerp render position to actual position
        self.renderPosition = (
            self.renderPosition[0]
            + (self.actualPosition[0] - self.renderPosition[0]) * Time.deltaTime * 10,
            self.renderPosition[1]
            + (self.actualPosition[1] - self.renderPosition[1]) * Time.deltaTime * 10,
        )

        screen.blit(self.body, self.renderPosition)

        # pygame.draw.rect(screen, (255, 0, 0), self.rect, 1)

        self.timer -= Time.deltaTime

        if self.timer < 0:
            if self.isHide:
                self.show()
            else:
                self.hide()

    def show(self):
        self.isHide = False
        self.timer = 2
        self.actualPosition = self.initialPosition

    def hide(self):
        self.isHide = True
        self.timer = random.random() * 3 + 2
        self.actualPosition = (self.initialPosition[0], self.initialPosition[1] + 52)
