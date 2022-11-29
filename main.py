import random

import pygame
import sys
import math

WIDTH = 800
HEIGHT = 800
FPS = 60

pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((255, 255, 255))


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
        self.distance_x = pricel.x - hero.rect.x
        self.distance_y = pricel.y - hero.rect.y

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
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.speedx = speedx
        self.speedy = speedy
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10

    def update(self):
        btn = pygame.key.get_pressed()
        if btn[pygame.K_a] and self.rect.x > 0: self.rect.x -= self.speedx
        if btn[pygame.K_d] and self.rect.x < WIDTH - 30: self.rect.x += self.speedx
        if btn[pygame.K_w] and self.rect.y > 0: self.rect.y -= self.speedy
        if btn[pygame.K_s] and self.rect.y < HEIGHT - 40: self.rect.y += self.speedy

    def shoot(self):
        bullet = Projectile(10, self.rect.x + 20 // 2, self.rect.y + 40 // 2)
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


hero = Hero(3, 3)

enemies = []

pricel = Pricel()

all_sprites = pygame.sprite.Group()
all_sprites.add(hero)

bullets = pygame.sprite.Group()

mobs = pygame.sprite.Group()


while True:
    clock.tick(FPS)

    keys = pygame.key.get_pressed()

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


    screen.fill((255, 255, 255))
    pricel.draw()

    all_sprites.draw(screen)

    pygame.display.flip()


# KidsCanCode - Game Development with Pygame video series
# Shmup game - part 3
# Video link: https://www.youtube.com/watch?v=33g62PpFwsE
# Collisions and bullets
# import pygame
# import random
#
# WIDTH = 480
# HEIGHT = 600
# FPS = 60
#
# # define colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# YELLOW = (255, 255, 0)
#
# # initialize pygame and create window
# pygame.init()
# pygame.mixer.init()
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Shmup!")
# clock = pygame.time.Clock()
#
# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.Surface((50, 40))
#         self.image.fill(GREEN)
#         self.rect = self.image.get_rect()
#         self.rect.centerx = WIDTH / 2
#         self.rect.bottom = HEIGHT - 10
#         self.speedx = 0
#
#     def update(self):
#         self.speedx = 0
#         keystate = pygame.key.get_pressed()
#         if keystate[pygame.K_LEFT]:
#             self.speedx = -8
#         if keystate[pygame.K_RIGHT]:
#             self.speedx = 8
#         self.rect.x += self.speedx
#         if self.rect.right > WIDTH:
#             self.rect.right = WIDTH
#         if self.rect.left < 0:
#             self.rect.left = 0
#
#     def shoot(self):
#         bullet = Bullet(self.rect.centerx, self.rect.top)
#         all_sprites.add(bullet)
#         bullets.add(bullet)
#
# class Mob(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.Surface((30, 40))
#         self.image.fill(RED)
#         self.rect = self.image.get_rect()
#         self.rect.x = random.randrange(WIDTH - self.rect.width)
#         self.rect.y = random.randrange(-100, -40)
#         self.speedy = random.randrange(1, 8)
#         self.speedx = random.randrange(-3, 3)
#
#     def update(self):
#         self.rect.x += self.speedx
#         self.rect.y += self.speedy
#         if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
#             self.rect.x = random.randrange(WIDTH - self.rect.width)
#             self.rect.y = random.randrange(-100, -40)
#             self.speedy = random.randrange(1, 8)
#
# class Bullet(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.Surface((10, 20))
#         self.image.fill(YELLOW)
#         self.rect = self.image.get_rect()
#         self.rect.bottom = y
#         self.rect.centerx = x
#         self.speedy = -10
#
#     def update(self):
#         self.rect.y += self.speedy
#         # kill if it moves off the top of the screen
#         if self.rect.bottom < 0:
#             self.kill()
#
# all_sprites = pygame.sprite.Group()
# mobs = pygame.sprite.Group()
# bullets = pygame.sprite.Group()
# player = Player()
# all_sprites.add(player)
# for i in range(8):
#     m = Mob()
#     all_sprites.add(m)
#     mobs.add(m)
#
# # Game loop
# running = True
# while running:
#     # keep loop running at the right speed
#     clock.tick(FPS)
#     # Process input (events)
#     for event in pygame.event.get():
#         # check for closing window
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_SPACE:
#                 player.shoot()
#
#     # Update
#     all_sprites.update()
#
#     # check to see if a bullet hit a mob
#     hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
#     for hit in hits:
#         print(hits)
#         # m = Mob()
#         # all_sprites.add(m)
#         # mobs.add(m)
#
#     # check to see if a mob hit the player
#     hits = pygame.sprite.spritecollide(player, mobs, False)
#     if hits:
#         running = False
#
#     # Draw / render
#     screen.fill(BLACK)
#     all_sprites.draw(screen)
#     # *after* drawing everything, flip the display
#     pygame.display.flip()
#
# pygame.quit()