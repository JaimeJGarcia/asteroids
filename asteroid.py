import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen,
                           "white",
                           self.position,
                           self.radius,
                           2)

    def update(self, dt):
        self.position += self.velocity * dt


    def split(self):
        self.kill()
        
        # small asteroid
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        opposite_angle = random_angle * -1

        vector_1 = self.velocity.rotate(random_angle)
        vector_2 = self.velocity.rotate(opposite_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # initialize new asteroid objects
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity = vector_1 * 1.2
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2.velocity = vector_2 * 1.2
