from pygame.display import set_mode


class Screen:
    def __init__(self, sizes: tuple):
        self.screen = set_mode(sizes)

    def set_mode_screen(self):
        return self.screen
