import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # initialize game start
    pygame.init()
    # initialize display object
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Initialize FPS game object
    game_clock = pygame.time.Clock()
    # delta time
    dt = 0

    # create groups
    updatable = pygame.sprite.Group() # all updatable objects
    drawable = pygame.sprite.Group() # all drawable objects
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # add classes to containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # initialize objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    field = AsteroidField()

    # Game loop
    while True:
        # interupt event from game loop to exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # fill the game screen
        screen.fill("black")
        # draw player
        for sprite in drawable:
            sprite.draw(screen)

        # update movement
        for game_object in updatable:
            game_object.update(dt)
        
        # check for collisions
        for rock in asteroids:
            # player collision
            if player.collides(rock):
                print("Game over!")
                sys.exit()
           # shot collision
            for bullet in shots:
                if rock.collides(bullet):
                    bullet.kill()
                    rock.kill()
 
        # re-draw game screen
        pygame.display.flip()
        # get delta time and limit fps
        dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()
