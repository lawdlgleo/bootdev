import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    game_loop(screen)


def game_loop(screen):
    ### Create game loop

    while True:
        ## Log the state

        log_state()

        ## Starting point for game events

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return

        ## Draw to screen

        screen.fill("black")

        ## Flip the screen

        pygame.display.flip()


if __name__ == "__main__":
    main()
