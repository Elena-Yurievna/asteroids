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
        
        # check if there are too many asteroids
        asteroid_group = Asteroid.containers[0]
        current_count = len(asteroid_group)
        if current_count >= ASTEROID_MAX_COUNT:
            return

        # randomize the angle of the split
        random_angle = random.uniform(20, 50)

        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroids_to_spawn = 2
        if current_count == 99:
            asteroids_to_spawn = 1

        if asteroids_to_spawn == 2:
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = new_velocity1 * 1.2

            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = new_velocity2 * 1.2
        elif asteroids_to_spawn == 1:
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = new_velocity1 * 1.2