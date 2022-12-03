import pygame
from settings import *
import spritesheet
from projectile import Projectile

BLACK = (0, 0, 0)
pygame.init()

class Hero(pygame.sprite.Sprite):
    def __init__(self, speedx, speedy, facing, all_sprites, bullets, tiles, x, y):
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



        if btn[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= self.speedx
            self.action = 1
            self.facing = 0
            if pygame.sprite.spritecollide(self, self.tiles, False):
                self.rect.x += self.speedx
        if btn[pygame.K_d] and self.rect.x < WIDTH - 30:
            self.rect.x += self.speedx
            self.action = 1
            self.facing = 1
            if pygame.sprite.spritecollide(self, self.tiles, False):
                self.rect.x -= self.speedx
        if btn[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= self.speedy
            self.action = 1
            if pygame.sprite.spritecollide(self, self.tiles, False):
                self.rect.y += self.speedy
        if btn[pygame.K_s] and self.rect.y < HEIGHT - 40:
            self.rect.y += self.speedy
            self.action = 1
            if pygame.sprite.spritecollide(self, self.tiles, False):
                self.rect.y -= self.speedy
        if pygame.time.get_ticks() - self.shoot_time >= 250:
            self.shoot_time = pygame.time.get_ticks()
            if pygame.mouse.get_pressed()[0]:
                self.shoot(self.all_sprites, self.bullets)

    def shoot(self, group_of_sprite, bullets_sprite):
        pos = pygame.mouse.get_pos()
        mouse_x = pos[0]
        mouse_y = pos[1]
        bullet = Projectile(10, self.rect.x, self.rect.y, mouse_x, mouse_y)
        group_of_sprite.add(bullet)
        bullets_sprite.add(bullet)


class Aim(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sprites/target_20.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (512 * 0.08, 512 * 0.08))
        self.image.set_colorkey(BLACK)


    def update(self):
        self.rect.x = pygame.mouse.get_pos()[0] - 20
        self.rect.y = pygame.mouse.get_pos()[1] - 20


screen = pygame.display.set_mode((WIDTH, HEIGHT))
sprite_sheet_idle = pygame.image.load('sprites/idle.png').convert_alpha()
sprite_sheet_walk = pygame.image.load('sprites/walk.png').convert_alpha()
show_idle = spritesheet.Spritesheet(sprite_sheet_idle)
show_walk = spritesheet.Spritesheet(sprite_sheet_walk)
idle_list = spritesheet.get_animation(show_idle, 128, 128, BLACK, 6, 1)
walk_list = spritesheet.get_animation(show_walk, 128, 128, BLACK, 6, 1)
bullets = pygame.sprite.Group()