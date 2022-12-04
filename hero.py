import pygame
from settings import *
import spritesheet
from projectile import Projectile

BLACK = (0, 0, 0)
pygame.init()

class Hero(pygame.sprite.Sprite):
    def __init__(self, speedx, speedy, facing, all_sprites, bullets, tiles, x, y, aim):
        pygame.sprite.Sprite.__init__(self)
        self.speedx = speedx
        self.speedy = speedy
        self.update_time = pygame.time.get_ticks()
        self.frame_index = 0
        self.animation_list = []
        self.animation_list.append(idle_list)
        self.animation_list.append(walk_list)
        self.action = 0  # 0-idle, 1-walking
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.last_coords = self.rect
        self.facing = 0  # 0 -right, 1-left
        self.shoot_time = pygame.time.get_ticks()
        self.all_sprites = all_sprites
        self.bullets = bullets
        self.tiles = tiles
        self.rect.centerx = x
        self.rect.bottom = y
        self.aim = aim
        self.help_x = 0
        self.help_y = 0

    def update(self):
        animation_cooldown = 100
        if self.facing:
            self.image = pygame.transform.flip(self.animation_list[self.action][self.frame_index], True, False)
            self.image.set_colorkey(BLACK)
        else:
            self.image = self.animation_list[self.action][self.frame_index]
        self.action = 0
        if pygame.time.get_ticks() - self.update_time >= animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
            if self.frame_index >= len(self.animation_list[self.action]):
                self.frame_index = 0

        btn = pygame.key.get_pressed()

        # if pygame.sprite.spritecollide(hero, self.level.visible_sprites, False):
        #     pygame.sprite.spritecollide(hero, self.level.visible_sprites, False)



        if btn[pygame.K_a]:
            self.rect.x -= self.speedx
            self.action = 1
            self.facing = 0
            self.help_x -= self.speedx
            if pygame.sprite.spritecollide(self, self.tiles, False):
                self.rect.x += self.speedx
                self.help_x += self.speedx
        if btn[pygame.K_d]:
            self.rect.x += self.speedx
            self.action = 1
            self.facing = 1
            self.help_x += self.speedx
            if pygame.sprite.spritecollide(self, self.tiles, False):
                self.rect.x -= self.speedx
                self.help_x -= self.speedx
        if btn[pygame.K_w]:
            self.rect.y -= self.speedy
            self.action = 1
            self.help_y -= self.speedy
            if pygame.sprite.spritecollide(self, self.tiles, False):
                self.rect.y += self.speedy
                self.help_y += self.speedy
        if btn[pygame.K_s]:
            self.rect.y += self.speedy
            self.action = 1
            self.help_y += self.speedy
            if pygame.sprite.spritecollide(self, self.tiles, False):
                self.rect.y -= self.speedy
                self.help_y -= self.speedy
        if pygame.time.get_ticks() - self.shoot_time >= 250:
            self.shoot_time = pygame.time.get_ticks()
            if pygame.mouse.get_pressed()[0]:
                self.shoot(self.all_sprites, self.bullets)

    def shoot(self, group_of_sprite, bullets_sprite):
        bullet = Projectile(10, self.rect.x, self.rect.y, self.aim.rect.x + self.help_x + 20, self.aim.rect.y + self.help_y + 20)
        group_of_sprite.add(bullet)
        bullets_sprite.add(bullet)


class Aim(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sprites/target_20.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (512 * 0.08, 512 * 0.08))
        self.image.set_colorkey(BLACK)
        self.x, self.y = x, y

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0] - 20 - 188
        self.rect.y = pos[1] - 20 + 9


screen = pygame.display.set_mode((WIDTH, HEIGHT))
sprite_sheet_idle = pygame.image.load('sprites/idle.png').convert_alpha()
sprite_sheet_walk = pygame.image.load('sprites/walk.png').convert_alpha()
show_idle = spritesheet.Spritesheet(sprite_sheet_idle)
show_walk = spritesheet.Spritesheet(sprite_sheet_walk)
idle_list = spritesheet.get_animation(show_idle, 128, 128, BLACK, 6, 0.2)
walk_list = spritesheet.get_animation(show_walk, 128, 128, BLACK, 6, 0.2)
bullets = pygame.sprite.Group()