import pygame
import random

from constants.AssetPath import AudioPath


class AudioManager:
    pygame.mixer.init()

    hitSound = pygame.mixer.Sound(AudioPath.HIT)

    def playHitSound():
        AudioManager.hitSound.play()
