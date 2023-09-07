import pygame


from constants.AssetPath import ImagePath
from managers.AudioManager import AudioManager
from managers.MoleManager import MoleManager

from utils.Time import Time


class Hammer:
    def __init__(self):
        self.image = pygame.image.load(ImagePath.HAMMER)
        self.image = pygame.transform.rotate(self.image, 45)
        self.angle = 0
        self.renderAngle = 0
        self.click = False
        self.rect = pygame.Rect((0, 0), (60, 50))

    def update(self, screen: pygame.Surface):
        mousePosition = pygame.mouse.get_pos()

        position = (
            mousePosition[0] - self.image.get_size()[0] / 2,
            mousePosition[1] - self.image.get_size()[1] / 2,
        )

        self.rect.x = position[0] + 50
        self.rect.y = position[1] + 140

        self.renderAngle = (
            self.renderAngle + (self.angle - self.renderAngle) * Time.deltaTime * 24
        )

        screen.blit(pygame.transform.rotate(self.image, self.renderAngle), position)

        # pygame.draw.rect(screen, (255, 0, 0), self.rect, 1)

    def onMousePressed(self):
        self.angle = 45

        if self.click:
            return

        self.click = True
        for mole in MoleManager.moles:
            if mole.rect.colliderect(self.rect) and not mole.isHide:
                AudioManager.playHitSound()
                mole.hit()

    def onMouseReleased(self):
        self.angle = 0
        self.click = False
