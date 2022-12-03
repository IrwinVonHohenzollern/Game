import pygame
from settings import *
from tile import Tile
from hero import Hero, Aim

class Level:
    def __init__(self, screen):

        self.display_surface = pygame.display.get_surface()
        # sprite group setup
        self.all_sprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.tiles = pygame.sprite.Group()

        self.create_map()
        self.screen = screen

    def run(self):
        self.all_sprites.draw(self.screen)

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    tile = Tile((x + 100, y + 100), [self.all_sprites])
                    self.tiles.add(tile)
                elif col == 'p':
                    hero = Hero(3, 3, 0, self.all_sprites, self.bullets, self.tiles, x + 100, y + 100)
                    aim = Aim()
        self.all_sprites.add(hero)
        self.all_sprites.add(aim)
