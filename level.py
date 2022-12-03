import pygame
from settings import *
from tile import Tile

class Level:
    def __init__(self, screen):

        self.display_surface = pygame.display.get_surface()
        # sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

        self.create_map()
        self.screen = screen

    def run(self):
        self.visible_sprites.draw(self.screen)

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP1):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x + 100, y + 100), [self.visible_sprites])