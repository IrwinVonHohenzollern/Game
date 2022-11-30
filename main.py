import random

import pygame
import sys
import math

import spritesheet

WIDTH = 800
HEIGHT = 800
FPS = 60

BLACK = (0, 0, 0)

pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((50, 50, 50))
pygame.display.set_caption('Spritesheets')

sprite_sheet_idle = pygame.image.load('sprites/idle.png').convert_alpha()
sprite_sheet_walk = pygame.image.load('sprites/walk.png').convert_alpha()
show_idle = spritesheet.Spritesheet(sprite_sheet_idle)
show_walk = spritesheet.Spritesheet(sprite_sheet_walk)

class Pricel():

    def draw(self):
        self.x, self.y = pygame.mouse.get_pos()
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, 10, 10))


class Projectile(pygame.sprite.Sprite):
    def __init__(self, vel, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5, 5))
        self.image.fill((255, 0, 0))
        self.vel = vel
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.distance_x = pricel.x - hero.rect.x + (30 // 2)
        self.distance_y = pricel.y - hero.rect.y + (40 // 2)

        # distance_x = a.x - hero.x  Управляемая стрельба
        # distance_y = a.y - hero.y
        # angle = math.atan2(distance_y, distance_x)
        # bullet.x += bullet.vel * math.cos(angle)
        # bullet.y += bullet.vel * math.sin(angle)

    def update(self):

        angle = math.atan2(self.distance_y, self.distance_x)
        self.rect.x += math.cos(angle) * self.vel
        self.rect.y += math.sin(angle) * self.vel
        if self.rect.x < 0 or self.rect.x > WIDTH or self.rect.y < 0 or self.rect.y > HEIGHT:
            self.kill()


class Hero(pygame.sprite.Sprite):
    def __init__(self, speedx, speedy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.rect = self.image.get_rect()
        self.speedx = speedx
        self.speedy = speedy
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.update_time = pygame.time.get_ticks()
        self.frame_index = 0
        self.animation_list = []
        self.last_coords = self.rect
        self.action = 0  # 0-idle, 1-walking

    def update(self):
        animation_cooldown = 100
        if pygame.time.get_ticks() - self.update_time >= animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
            if self.frame_index >= len(self.animation_list[self.action]):
                self.frame_index = 0
        btn = pygame.key.get_pressed()
        if btn[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= self.speedx
        if btn[pygame.K_d] and self.rect.x < WIDTH - 30:
            self.rect.x += self.speedx
        if btn[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= self.speedy
        if btn[pygame.K_s] and self.rect.y < HEIGHT - 40:
            self.rect.y += self.speedy
        # if self.last_coords == self.rect:
        #     self.animation_list = idle_list

    def shoot(self):
        bullet = Projectile(10, self.rect.x + 20 // 2, self.rect.y + 40 // 2)
        all_sprites.add(bullet)
        bullets.add(bullet)

    def draw(self):
        screen.blit(self.animation_list[self.action][self.frame_index], (self.rect.x, self.rect.y))


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
hero = Hero(3, 3)
hero.animation_list.append(idle_list)
hero.animation_list.append(walk_list)

enemies = []

pricel = Pricel()

all_sprites = pygame.sprite.Group()
# all_sprites.add(hero)

bullets = pygame.sprite.Group()

mobs = pygame.sprite.Group()


while True:
    clock.tick(FPS)
    screen.fill((50, 50, 50))
    keys = pygame.key.get_pressed()

    # update animation
    # current_time = pygame.time.get_ticks()
    # if current_time - last_update >= animation_cooldown:
    #     frame += 1
    #     last_update = current_time
    #     if frame >= len(idle_list):
    #         frame = 0
    #
    # if counter_hero_animation == 0:
    #     screen.blit(idle_list[frame], (0, 0))
    # elif counter_hero_animation == 1:
    #     screen.blit(walk_list[frame], (0, 0))


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

    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)

    pricel.draw()
    hero.update()
    hero.draw()

    all_sprites.draw(screen)

    pygame.display.flip()


