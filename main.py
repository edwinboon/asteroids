import pygame

from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    clock = pygame.time.Clock()
    dt = 0

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatables.update(dt)

        screen.fill("black")

        for obj in drawables:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000  # Convert milliseconds to seconds


if __name__ == "__main__":
    main()
