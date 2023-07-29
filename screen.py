from pygame.locals import SCALED
from pygame.display import set_mode


class Screen:
    def __init__(self, sizes: tuple):
        self.flags = SCALED
        self.screen = set_mode(sizes, self.flags, vsync=1)

    def set_mode_screen(self):
        return self.screen
