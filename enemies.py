import pygame
import spritesheet
import math

BLACK = (0, 0, 0)

sprite_sheet_idle = pygame.image.load('sprites/idle.png').convert_alpha()
sprite_sheet_idle = pygame.transform.scale(sprite_sheet_idle, (768, 128))
show_idle = spritesheet.Spritesheet(sprite_sheet_idle)
idle_list = spritesheet.get_animation(show_idle, 128, 128, (255, 0, 0), 6, 1)

sprite_sheet_walk = pygame.image.load('sprites/walk.png').convert_alpha()
sprite_sheet_walk = pygame.transform.scale(sprite_sheet_walk, (768, 128))
show_walk = spritesheet.Spritesheet(sprite_sheet_walk)
walk_list = spritesheet.get_animation(show_walk, 128, 128, (255, 0, 0), 6, 1)

sprite_sheet_die = pygame.image.load('sprites/die.png').convert_alpha()
sprite_sheet_die = pygame.transform.scale(sprite_sheet_die, (511, 88))
show_die = spritesheet.Spritesheet(sprite_sheet_die)
die_list = spritesheet.get_animation(show_die, 73, 88, (255, 255, 255), 7, 1)



class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, enemies, enemy_lst):
        pygame.sprite.Sprite.__init__(self)
        self.facing = 0
        self.animation_list = []
        self.animation_list.append(idle_list)
        self.animation_list.append(walk_list)
        self.animation_list.append(die_list)

        self.action = 2  # 0-idle 1-walk 2-death
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.image = self.animation_list[2][0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.vel = 2
        self.float_x = x
        self.float_y = y
        self.hp = 100
        self.enemies = enemies
        self.enemy_lst = enemy_lst
        self.enemies.add(self)
        self.enemy_lst.append(self)
        self.live = True

    def updater(self, direction_x, direction_y):
        animation_cooldown = 100
        if self.facing:
            self.image = pygame.transform.flip(self.animation_list[self.action][self.frame_index], True, False)
            # self.image.set_colorkey(BLACK)
            self.image.set_colorkey((255, 255, 255))
        else:
            self.image = self.animation_list[self.action][self.frame_index]
            self.image.set_colorkey((255, 255, 255))
        if pygame.time.get_ticks() - self.update_time >= animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
            if self.frame_index >= len(self.animation_list[self.action]):
                self.frame_index = 0
                # if self.action == 2:
                #     self.kill()

        if self.live:
            x_diff = direction_x - self.rect.x
            y_diff = direction_y - self.rect.y

            self.angle = math.atan2(y_diff, x_diff)
            self.change_x = math.cos(self.angle) * self.vel
            self.change_y = math.sin(self.angle) * self.vel

            self.float_y += self.change_y
            self.float_x += self.change_x

            self.rect.x = int(self.float_x)
            self.rect.y = int(self.float_y)
            if direction_x > self.rect.x:
                self.facing = True
            else:
                self.facing = False
        # if self.hp <= 0:
        #     self.live = False
        #     print(1)
        #     self.action = 2
        #     self.frame_index = 0
