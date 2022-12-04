import pygame

from settings import *
from tile import Tile
from hero import Hero, Aim




class Level:
    def __init__(self, screen):

        self.display_surface = pygame.display.get_surface()
        # sprite group setup

        self.visible_sprites = Camera()

        self.all_sprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.tiles = pygame.sprite.Group()

        self.create_map()
        self.screen = screen


    def run(self):
        self.visible_sprites.update()

        self.visible_sprites.custom_draw(self.hero)


        # self.all_sprites.update()
        # self.all_sprites.draw(self.screen)


    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    tile = Tile((x + 100, y + 100), [self.all_sprites])
                    self.tiles.add(tile)
                    self.visible_sprites.add(tile)
                elif col == 'p':
                    self.aim = Aim(0, 0)
                    self.hero = Hero(3, 3, 0, self.visible_sprites, self.bullets, self.tiles, x + 100, y + 100, self.aim)

                    # self.all_sprites.add(self.hero)
                    self.visible_sprites.add(self.aim)
                    self.visible_sprites.add(self.hero)



class Camera(pygame.sprite.Group):
    def __init__(self):

        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()


    def custom_draw(self, player):

        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        for sprite in self.sprites():
            if type(sprite) == Aim:
                offset_position = sprite.rect.topleft - self.offset
                self.display_surface.blit(sprite.image, (offset_position.x + player.help_x, offset_position.y + player.help_y))
            else:
                offset_position = sprite.rect.topleft - self.offset
                self.display_surface.blit(sprite.image, offset_position)