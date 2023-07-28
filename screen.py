from pygame.display import set_mode


class Screen:
    def __init__(self, sizes: tuple):
        self.screen = set_mode(sizes, vsync=11)

    def set_mode_screen(self):
        return self.screen
