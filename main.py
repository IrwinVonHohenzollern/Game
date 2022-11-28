import pygame, sys

WIDTH = 800
HEIGHT = 800
FPS = 60

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((255, 255, 255))


class Pricel(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 10))

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


class projectile(object):
    def __init__(self, vel, x, y):
        self.x = x
        self.y = y
        self.vel = vel

    def draw(self, win):
        pygame.draw.rect(screen, (0, 0, 0))


class Hero:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, 30, 40))


bullets = []
hero = Hero(WIDTH // 2, HEIGHT - 50)


def draw():
    hero.draw()

    pygame.display.flip()
    pygame.display.update()


while True:
    keys = pygame.key.get_pressed()
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    for bullet in bullets:
        if bullet.y < 0:
            bullets.pop(bullets.index(bullet))
        else:
            bullet.x += bullet.vel

    if keys[pygame.K_a] and hero.x > 0: hero.x -= 3
    if keys[pygame.K_d] and hero.x < WIDTH - 30: hero.x += 3
    if keys[pygame.K_w] and hero.y > 0: hero.y -= 3
    if keys[pygame.K_s] and hero.y < HEIGHT - 40: hero.y += 3


    hero.draw()

    pygame.display.update()

    clock.tick(FPS)

