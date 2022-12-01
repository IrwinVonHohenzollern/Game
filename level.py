import pygame
from settings import *

class Level:
    def __init__(self):

        self.display_surface = pygame.display.get_surface()
        # sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

    def run(self):
        # update
        pass

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            print(row)