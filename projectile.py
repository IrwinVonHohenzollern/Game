import pygame
import math
from settings import *


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

        # if self.rect.x < 0 or self.rect.x > WIDTH or self.rect.y < 0 or self.rect.y > HEIGHT:
        #     self.kill()