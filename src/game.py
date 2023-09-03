import pygame
from sys import exit
from classes.Hammer import Hammer

from constants.GameConfig import MoleGame, ScreenSize
from constants.AssetPath import *

from classes.Mole import Mole
from classes.Text import Text


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Whack a Mole")
        pygame.mouse.set_visible(False)

        self.screen = pygame.display.set_mode((ScreenSize.WIDTH, ScreenSize.HEIGHT))

        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(FontPath.KNIFER, 48)

        self.top_bg = pygame.image.load(ImagePath.TOP_BACKGROUND)
        self.mid_1_bg = pygame.image.load(ImagePath.MID_1_BACKGROUND)
        self.mid_2_bg = pygame.image.load(ImagePath.MID_2_BACKGROUND)
        self.bot_bg = pygame.image.load(ImagePath.BOT_BACKGROUND)

        self.hit_text = Text("hit: 0", self.font, (160, 720))
        self.miss_text = Text("miss: 0", self.font, (260, 720))

        self.hit = 0
        self.miss = 0

        self.moles = []

        for i in range(0, 9):
            self.moles.append(
                Mole(
                    (
                        MoleGame.POSITIONS[i][0],
                        MoleGame.POSITIONS[i][1],
                    )
                )
            )

        self.hammer = Hammer()

    def draw(self):
        self.screen.fill((0, 0, 0))

        self.screen.blit(self.top_bg, (0, 0))

        for i in range(0, 3):
            self.moles[i].update(self.screen)

        self.screen.blit(self.mid_2_bg, (0, 0))
        for i in range(3, 6):
            self.moles[i].update(self.screen)

        self.screen.blit(self.mid_1_bg, (0, 0))

        for i in range(6, 9):
            self.moles[i].update(self.screen)

        self.screen.blit(self.bot_bg, (0, 0))

        self.hit_text.update(self.screen)
        self.miss_text.update(self.screen)

        self.hammer.update(self.screen)

        pygame.display.update()

    def update(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.draw()

            # make hammer follow mouse

            self.clock.tick(60)


game = Game()

game.update()
