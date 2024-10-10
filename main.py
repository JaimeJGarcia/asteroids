import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Initialize FPS game object
    game_clock = pygame.time.Clock()
    # delta time
    dt = 0


    # Game loop
    while True:
        # interupt event from game loop to exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # fill the game screen
        screen.fill("black")
        # re-draw game screen
        pygame.display.flip()
        # get delta time and limit fps
        dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()
