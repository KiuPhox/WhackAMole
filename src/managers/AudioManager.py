import pygame

from constants.AssetPath import AudioPath


class AudioManager:
    pygame.mixer.init()

    hitSound = pygame.mixer.Sound(AudioPath.HIT)
    bgMusic = pygame.mixer.Sound(AudioPath.BG_MUSIC)
    bgMusic.play(-1)

    def playHitSound():
        AudioManager.hitSound.play()
