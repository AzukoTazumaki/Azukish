from pygame import display, FULLSCREEN


class Screen:
    def __init__(self, sizes: tuple):
        self.screen = display.set_mode(sizes, FULLSCREEN, display=0)

    def set_mode_screen(self):
        return self.screen
