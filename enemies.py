import pygame
import spritesheet
import math
from settings import WIDTH, HEIGHT

BLACK = (0, 0, 0)
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, enemies, enemy_lst):
        pygame.sprite.Sprite.__init__(self)
        self.facing = 0
        self.animation_list = []
        self.action = 0  # 0-idle 1-walk 2-death
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.vel = 2
        self.float_x = x
        self.float_y = y
        self.hp = 100
        self.enemies = enemies
        self.enemy_lst = enemy_lst
        self.enemies.add(self)
        self.enemy_lst.append(self)
        self.live = True
        self.animation_cooldown = 100

    def updater(self, direction_x, direction_y):

        if self.facing:
            self.image = pygame.transform.flip(self.animation_list[self.action][self.frame_index], True, False)
            self.image.set_colorkey(BLACK)
        else:
            self.image = self.animation_list[self.action][self.frame_index]
            self.image.set_colorkey((255, 255, 255))
        if pygame.time.get_ticks() - self.update_time >= self.animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
            if self.frame_index >= len(self.animation_list[self.action]):
                self.frame_index = 0
                # if self.action == 2:
                #     self.kill()

        # Moving
        # if self.live:
        #     x_diff = direction_x - self.rect.x
        #     y_diff = direction_y - self.rect.y
        #
        #     self.angle = math.atan2(y_diff, x_diff)
        #     self.change_x = math.cos(self.angle) * self.vel
        #     self.change_y = math.sin(self.angle) * self.vel
        #
        #     self.float_y += self.change_y
        #     self.float_x += self.change_x
        #
        #     self.rect.x = int(self.float_x)
        #     self.rect.y = int(self.float_y)
        #     if direction_x > self.rect.x:
        #         self.facing = True
        #     else:
        #         self.facing = False

        # if self.hp <= 0:
        #     self.live = False
        #     print(1)
        #     self.action = 2
        #     self.frame_index = 0

idle_list = []

class Golem(Enemy):

    def __init__(self, x, y, enemies, enemy_lst):
        super().__init__(x, y, enemies, enemy_lst)
        self.animation_list = golem_lst
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.animation_cooldown = 150

    def updater(self, direction_x, direction_y):
        super().updater(direction_x, direction_y)



# for i in range(1, 32):
#     if i < 10:
#         img = pygame.image.load(f'sprites/Idle_demon/Idle_000{i}.png').convert_alpha()
#     else:
#         img = pygame.image.load(f'sprites/Idle_demon/Idle_00{i}.png').convert_alpha()
#     img.fill((255, 255, 255))
#     # img = pygame.transform.scale(img, (300, 200))
#     idle_list.append(img)
sprite_sheet_idle1 = pygame.image.load('sprites/gladiator.png').convert_alpha()
show_idle1 = spritesheet.Spritesheet(sprite_sheet_idle1)
idle_1_list = spritesheet.get_animation(show_idle1, 32, 32, BLACK, 7, 4, 2)

# Sprites for golem
sprite_sheet_idle = pygame.image.load('sprites/golem.png').convert_alpha()
show_idle = spritesheet.Spritesheet(sprite_sheet_idle)
idle_list = spritesheet.get_animation(show_idle, 100, 111, BLACK, 4, 3, 0)
walk_list = spritesheet.get_animation(show_idle, 100, 111, BLACK, 8, 3, 1)


golem_lst = []
golem_lst.append(idle_list)
golem_lst.append(walk_list)


