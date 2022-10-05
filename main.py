__author__ = "segdevv"


import random
import pygame


# Settings
FPS = 60
RESOLUTION = (1280, 720)
BACKGROUND_COLOR = (135, 206, 235)
FOREGROUDN_COLOR = (212, 241, 249)
RAIN_DROP_WIDTH = 5
RAIN_DROP_HEIGHT = 17
RAIN_DROP_COUNT = 135
RAIN_DROP_MIN_SPEED = 4
RAIN_DROP_MAX_SPPED = 16


class RainDrop:
    def __init__(self, start_x, start_y, width, height, speed):
        self._x = start_x
        self._y = start_y
        self._width = width
        self._height = height
        self._speed = speed

    def get_y(self):
        return self._y

    def get_rect(self):
        return pygame.Rect(self._x, self._y, self._width, self._height)

    def drop(self):
        self._y += self._speed

    def redrop(self, x, y, speed):
        self._x = x
        self._y = y
        self._speed = speed


def die():
    pygame.quit()
    exit()


def main():
    pygame.display.init()
    pygame.display.set_caption("RAINdrp")

    screen = pygame.display.set_mode(RESOLUTION)
    clock = pygame.time.Clock()

    rain_drops = [
        RainDrop(
            random.randint(0, RESOLUTION[0]),
            random.randint(0, RESOLUTION[1]),
            RAIN_DROP_WIDTH,
            RAIN_DROP_HEIGHT,
            random.randint(RAIN_DROP_MIN_SPEED, RAIN_DROP_MAX_SPPED),
        )
        for _ in range(RAIN_DROP_COUNT)
    ]

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                die()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    die()

        # Update
        screen.fill(BACKGROUND_COLOR)

        for rain_drop in rain_drops:
            rain_drop.drop()
            if rain_drop.get_y() > RESOLUTION[1]:
                rain_drop.redrop(
                    random.randint(0, RESOLUTION[0]),
                    random.randint(0, RESOLUTION[1]),
                    random.randint(RAIN_DROP_MIN_SPEED, RAIN_DROP_MAX_SPPED),
                )

        # Draw
        for rain_drop in rain_drops:
            pygame.draw.rect(screen, FOREGROUDN_COLOR, rain_drop.get_rect())

        pygame.display.flip()


if __name__ == "__main__":
    main()
