from pygame import FULLSCREEN
from pygame.display import set_mode
from settings import HEIGHT, WIDTH


class Screen:
    def __init__(self):
        self.screen = set_mode((WIDTH, HEIGHT), FULLSCREEN)

    def set_mode_screen(self):
        return self.screen
