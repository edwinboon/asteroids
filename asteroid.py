import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Split into two smaller asteroids
        random_angle = random.uniform(20, 50)
        rotation_1 = self.velocity.rotate(random_angle)
        rotation_2 = self.velocity.rotate(-random_angle)

        radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, radius)
        asteroid1.velocity = rotation_1 * 1.2

        asteroid2 = Asteroid(self.position.x, self.position.y, radius)
        asteroid2.velocity = rotation_2 * 1.2
