import pygame as pg
import random
import ctypes


WIDTH, HEIGHT = tuple(map(lambda x: ctypes.windll.user32.GetSystemMetrics(x) // 3, (0, 1)))
FPS = 60

if __name__ == '__main__':
    pg.init()
    pg.display.set_caption('Running Ninja')
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()
    game_is_running = True

    all_sprites = pg.sprite.Group()
    while game_is_running:
        clock.tick(FPS)
        # Inputs
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_is_running = False

        # Updates
        all_sprites.update()
        # Draw and render
        screen.fill((0, 255, 255))
        all_sprites.draw(screen)
        # After everything - it changes the demonstrated image
        pg.display.flip()

pg.quit()
