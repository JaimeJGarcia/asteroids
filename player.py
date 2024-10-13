import pygame
from circleshape import *
from constants import *
from shot import Shot

class Player(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.shoot_timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), width = 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        
        # check for movement
        keys = pygame.key.get_pressed()

        # move left
        if keys[pygame.K_a]:
            self.rotate(dt * -1)

        # move right
        if keys[pygame.K_d]:
            self.rotate(dt)

        # move forwards
        if keys[pygame.K_w]:
            self.move(dt)

        # move backwards:
        if keys[pygame.K_s]:
            self.move(dt * -1)

        if keys[pygame.K_SPACE]:
            self.shoot()

        # reduce shoot cooldown
        if self.shoot_timer > 0:
            self.shoot_timer -= dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shoot_timer > 0:
            return
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
