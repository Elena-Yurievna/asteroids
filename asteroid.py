import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        vertices = self.get_irregular_vertices(num_vertices=8)
        pygame.draw.polygon(screen, "red", vertices, 2)
    
    def get_irregular_vertices(self, num_vertices=8):
        vertices = []
        angle_step = 360 / num_vertices
        for i in range(num_vertices):
            angle = i * angle_step
            offset = random.uniform(0.8, 1.2)
            vertex = self.position + pygame.Vector2(0, 1).rotate(angle) * self.radius * offset
            vertices.append((int(vertex.x), int(vertex.y)))
        return vertices

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # randomize the angle of the split
        random_angle = random.uniform(20, 50)

        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2