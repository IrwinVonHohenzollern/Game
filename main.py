import random

import pygame
import sys
import math

import spritesheet
from pygame import mixer

WIDTH = 800
HEIGHT = 800
FPS = 60

BLACK = (0, 0, 0)

pygame.init()

pygame.mixer.init()
mixer.init()
mixer.music.load('music/stranger-things-124008.mp3')
mixer.music.set_volume(0.2)
mixer.music.play(-1)

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((50, 50, 50))
pygame.display.set_caption('Spritesheets')

pygame.mouse.set_visible(False)

sprite_sheet_idle = pygame.image.load('sprites/idle.png').convert_alpha()
sprite_sheet_walk = pygame.image.load('sprites/walk.png').convert_alpha()
show_idle = spritesheet.Spritesheet(sprite_sheet_idle)
show_walk = spritesheet.Spritesheet(sprite_sheet_walk)



# TEST

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


class Projectile(pygame.sprite.Sprite):
    def __init__(self, vel, x, y, direction_x, direction_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5, 5))
        self.image.fill((255, 0, 0))
        self.vel = vel
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.float_x = x
        self.float_y = y

        x_diff = direction_x - x
        y_diff = direction_y - y
        angle = math.atan2(y_diff, x_diff)

        self.change_x = math.cos(angle) * vel
        self.change_y = math.sin(angle) * vel

        # distance_x = a.x - hero.x  Управляемая стрельба
        # distance_y = a.y - hero.y
        # angle = math.atan2(distance_y, distance_x)
        # bullet.x += bullet.vel * math.cos(angle)
        # bullet.y += bullet.vel * math.sin(angle)

    def update(self):

        self.float_y += self.change_y
        self.float_x += self.change_x

        self.rect.x = int(self.float_x)
        self.rect.y = int(self.float_y)

        if self.rect.x < 0 or self.rect.x > WIDTH or self.rect.y < 0 or self.rect.y > HEIGHT:
            self.kill()


class Hero(pygame.sprite.Sprite):
    def __init__(self, speedx, speedy, facing):
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
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.facing = 0  # 0 -right, 1-left

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

        if btn[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= self.speedx
            self.action = 1
            self.facing = 0
        if btn[pygame.K_d] and self.rect.x < WIDTH - 30:
            self.rect.x += self.speedx
            self.action = 1
            self.facing = 1
        if btn[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= self.speedy
            self.action = 1
        if btn[pygame.K_s] and self.rect.y < HEIGHT - 40:
            self.rect.y += self.speedy
            self.action = 1

    def shoot(self):
        pos = pygame.mouse.get_pos()
        mouse_x = pos[0]
        mouse_y = pos[1]
        bullet = Projectile(10, self.rect.x, self.rect.y, mouse_x, mouse_y)
        all_sprites.add(bullet)
        bullets.add(bullet)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(20, WIDTH - 20)
        self.rect.bottom = random.randint(20, HEIGHT - 20)


def get_animation(list_of_sheet, width, height, destroy_bg, num_of_sprite):
    animation_list = []
    step_counter = 0
    for animation in range(1, num_of_sprite + 1):  # количество спрайтов в листе
        animation_list.append(list_of_sheet.get_image(step_counter, width, height, 1, destroy_bg))
        step_counter += 1
    return animation_list


idle_list = get_animation(show_idle, 128, 128, BLACK, 6)
walk_list = get_animation(show_walk, 128, 128, BLACK, 6)
hero = Hero(3, 3, 0)


enemies = []

aim = Aim()

all_sprites = pygame.sprite.Group()
all_sprites.add(hero)
all_sprites.add(aim)

my_sprites = []
my_sprites.append(hero)
bullets = pygame.sprite.Group()

mobs = pygame.sprite.Group()


while True:
    clock.tick(FPS)
    screen.fill((50, 50, 50))
    keys = pygame.key.get_pressed()


    # TEST


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            hero.shoot()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_j:
            enemy = Enemy()
            all_sprites.add(enemy)
            mobs.add(enemy)

    all_sprites.update()
    pygame.sprite.groupcollide(mobs, bullets, True, True)
    all_sprites.draw(screen)

    pygame.display.flip()


