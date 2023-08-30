import pygame
from sys import exit

from constants.GameConfig import ScreenSize
from constants.AssetPath import ImagePath

pygame.init()
screen = pygame.display.set_mode((ScreenSize.WIDTH, ScreenSize.HEIGHT))
pygame.display.set_caption("Whack a Mole")
clock = pygame.time.Clock()

bg_surface = pygame.image.load(ImagePath.BACKGROUND)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(bg_surface, (0, 0))

    pygame.display.update()

    clock.tick(60)
