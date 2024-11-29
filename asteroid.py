from circleshape import *
from constants import PLAYER_RADIUS
import pygame

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        self.radius = radius
        super().__init__(x, y, self.radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width =2)

    def update(self, dt):
       self.position +=  self.velocity * dt
