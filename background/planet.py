from screen import Screen
from settings import IMG_DIR
from os import path


class Planet:
    screen = Screen().set_mode_screen()

    def __init__(self):
        self.screen_rect = self.screen.get_rect()

