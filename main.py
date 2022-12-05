import random

import pygame
import sys
from pygame import mixer
from settings import *
from level import Level
# from camera import *



BLACK = (0, 0, 0)
# TEST
class Game:
    def __init__(self):


        pygame.init()

        pygame.mixer.init()
        mixer.init()
        mixer.music.load('music/stranger-things-124008.mp3')
        mixer.music.set_volume(0.2)
        mixer.music.play(-1)

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.screen.fill((50, 50, 50))
        pygame.display.set_caption('Spritesheets')

        bg_img = pygame.image.load('sprites/bg.png').convert_alpha()
        self.bg = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))

        pygame.mouse.set_visible(True)



        self.level = Level(self.screen)

        # self.camera = Camera(self.level.hero)
        # follow = Follow(self.camera, self.level.hero)
        # self.camera.setmethod(follow)

    def run(self):
        i = 0
        while True:
            self.clock.tick(FPS)
            self.screen.fill((50, 50, 50))

            # TEST

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_j:
                    enemy = Enemy()
                    # mobs.add(enemy)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    sys.exit()

            self.screen.blit(self.bg, (0, i))
            self.screen.blit(self.bg, (0, HEIGHT + i))
            if i == -HEIGHT:
                self.screen.blit(self.bg, (0, HEIGHT+i))
                i = 0
            i -= 1
            self.level.run()

            # self.camera.scroll()
            # pygame.sprite.groupcollide(mobs, bullets, True, True)

            # self.all_sprites.draw(self.screen)

            pygame.display.flip()



class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(20, WIDTH - 20)
        self.rect.bottom = random.randint(20, HEIGHT - 20)

if __name__ == '__main__':
    game = Game()
    game.run()