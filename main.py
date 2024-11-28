# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
dt = 0


def main():
    
    print("""Starting asteroids!
Screen width: 1280
Screen height: 720""")


    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000    
        player.update(dt)    
        screen.fill((0, 0, 0))
        player.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
