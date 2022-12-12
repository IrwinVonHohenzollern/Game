import pygame
import spritesheet

BLACK = (0, 0, 0)

sprite_sheet_idle = pygame.image.load('sprites/idle.png').convert_alpha()
sprite_sheet_idle = pygame.transform.scale(sprite_sheet_idle, (768, 128))
show_idle = spritesheet.Spritesheet(sprite_sheet_idle)
idle_list = spritesheet.get_animation(show_idle, 128, 128, BLACK, 6, 1)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.facing = 0
        self.animation_list = []
        self.animation_list.append(idle_list)
        self.action = 0  # 0-idle
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.image = self.animation_list[0][0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):
        animation_cooldown = 100
        if not self.facing:
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
