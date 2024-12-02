# this allows us to use code from
# the open-source pygame library
# throughout this file

import pygame
import sys
from shot import *
from constants import *
from player import Player
from asteroidfield import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
dt = 0


def main():
    
    print("""Starting asteroids!
Screen width: 1280
Screen height: 720""")

    group_shots = pygame.sprite.Group()
    group_asteroids = pygame.sprite.Group()
    group_updatable = pygame.sprite.Group()
    group_drawable = pygame.sprite.Group()
    Player.containers = (group_updatable, group_drawable)
    Asteroid.containers = (group_asteroids, group_updatable, group_drawable)
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    AsteroidField.containers = (group_updatable,)
    asteroid_field = AsteroidField()
    Shot.containers = (group_shots, group_updatable, group_drawable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = clock.tick(60) / 1000    

       
       # Update all objects
        for updatable in group_updatable:
            updatable.update(dt)        
        
       
       #    Check collisions

        for asteroid in group_asteroids:
            if player.collides_with(asteroid):
               print("Game over!")
               sys.exit()


       #    Bullet Collision Check
        
        for shot in group_shots:
            for asteroid in group_asteroids:
                if shot.collides_with(asteroid):
                    shot.kill()
                    asteroid.split()



       #    Draw Everything
        screen.fill((0, 0, 0)) 
        for drawing in group_drawable:
            drawing.draw(screen)
        pygame.display.flip()

        

if __name__ == "__main__":
    main()
