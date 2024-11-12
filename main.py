import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from circleshape import CircleShape
from shot import Shot


def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shot = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shot, updatable, drawable)

    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()
    dt = 0

    while True:
        # to make the quit button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        # initiate groups
        for entity in updatable:
            entity.update(dt)

        for entity in asteroids:
            if player.is_colliding(entity):
                sys.exit("Game over!")

        for entity in drawable:
            entity.draw(screen)

        # update content on the display screen
        pygame.display.flip()
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
