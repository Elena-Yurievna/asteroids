import pygame
from constants import *
from circleshape import CircleShape


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", self.position, self.radius, 2)

    def update(self, dt):
        if self.position.x < 0 or self.position.x > SCREEN_WIDTH:
            self.kill()
        if self.position.y < 0 or self.position.y > SCREEN_HEIGHT:
            self.kill()
        self.position += self.velocity * dt
