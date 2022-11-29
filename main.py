import pygame, sys, math

WIDTH = 800
HEIGHT = 800
FPS = 60

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((255, 255, 255))


class Pricel():

    def draw(self):
        self.x, self.y = pygame.mouse.get_pos()
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, 10, 10))


class Projectile(object):
    def __init__(self, vel, x, y):
        self.x = x
        self.y = y
        self.vel = vel
        distance_x = a.x - hero.x
        distance_y = a.y - hero.y
        angle = math.atan2(distance_y, distance_x)
        self.speed_x = math.cos(angle) * self.vel
        self.speed_y = math.sin(angle) * self.vel


    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, 10, 10))


class Hero:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, 30, 40))


bullets = []
hero = Hero(WIDTH // 2, HEIGHT - 50)

a = Pricel()


def draw():
    screen.fill((255, 255, 255))
    hero.draw()

    for bullet in bullets:
        bullet.draw()

    a.draw()


    pygame.display.flip()

    pygame.display.update()

    clock.tick(FPS)


while True:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:
                if len(bullets) < 5:
                    bullets.append(
                        Projectile(10, hero.x + 20 // 2, hero.y + 40 // 2))

    for bullet in bullets:
        if bullet.y < 0 or bullet.y < 0 or bullet.x > WIDTH or bullet.y > HEIGHT:
            bullets.pop(bullets.index(bullet))
        else:
            # distance_x = a.x - hero.x  Управляемая стрельба
            # distance_y = a.y - hero.y
            # angle = math.atan2(distance_y, distance_x)
            # bullet.x += bullet.vel * math.cos(angle)
            # bullet.y += bullet.vel * math.sin(angle)
            bullet.x += bullet.speed_x
            bullet.y += bullet.speed_y

    if keys[pygame.K_a] and hero.x > 0: hero.x -= 3
    if keys[pygame.K_d] and hero.x < WIDTH - 30: hero.x += 3
    if keys[pygame.K_w] and hero.y > 0: hero.y -= 3
    if keys[pygame.K_s] and hero.y < HEIGHT - 40: hero.y += 3

    draw()


