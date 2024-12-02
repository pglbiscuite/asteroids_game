import pygame
from shot import *
from circleshape import *
from constants import PLAYER_RADIUS
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED
from constants import PLAYER_SHOOT_SPEED
from constants import PLAYER_SHOOT_COOLDOWN

class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.player_timer = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), width = 2)

    # in the player class
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.player_timer = max(self.player_timer - dt, 0)

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            new_shot = self.shoot()


    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt


    def shoot(self):
        if self.player_timer > 0:
            return None
        new_shot = Shot(self.position.x, self.position.y)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        new_shot.velocity = forward * PLAYER_SHOOT_SPEED
        self.player_timer = PLAYER_SHOOT_COOLDOWN
        return new_shot
