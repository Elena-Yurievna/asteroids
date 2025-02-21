import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    score = 0  # player's score
    font = pygame.font.SysFont("Arial", 30)

    # load the background image
    background = pygame.image.load("images/space.png").convert()

    # create sprite groups for the game objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    updatable.add(player)
    drawable.add(player)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid in asteroids:  # check for collisions with asteroids
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

            for shot in shots: # check for collisions with shots
                if asteroid.collides_with(shot):
                    shot.kill()
                    score += 100 # increase the score
                    asteroid.split()
                if score > 2000:
                    print("You win!")
                    sys.exit()

        screen.blit(background, (0, 0)) # draw the background
        
        for obj in drawable:
            obj.draw(screen)
        
        # draw the score
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()