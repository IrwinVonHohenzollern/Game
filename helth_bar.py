import pygame
from settings import *

pygame.init()


class Bar(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image =
        self.rect = self.image.get_rect()
        self.sprites = []
        for i in range(16):
            self.sprites.append(pygame.image.load(f'sprites/healthbar/Health bar{i}.png').convert_alpha())


    def draw(self, x, y, screen):
        screen.blit(self.image, (x, y))
