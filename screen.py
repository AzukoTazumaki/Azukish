from pygame import display


class Screen:
    def __init__(self, sizes: tuple):
        self.screen = display.set_mode(sizes)

    def set_mode_screen(self):
        return self.screen
