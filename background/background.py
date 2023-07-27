from pygame import image, time, Surface
from settings import BACKGROUND_IMG, MAIN_STARS_IMG, ADDITIONAL_STARS


class Background:
    def __init__(self, screen: Surface):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.background_images = [
            image.load(BACKGROUND_IMG).convert_alpha(),
            image.load(MAIN_STARS_IMG).convert_alpha(),
            image.load(ADDITIONAL_STARS).convert_alpha()
        ]
        self.iterations = [0, 0, 0]
        self.clock = time.Clock()

    def load_background(self):
        for i in range(3):
            self.screen.blit(self.background_images[i], (0, self.iterations[i]))
            self.screen.blit(self.background_images[i], (0, - self.screen_rect.height + self.iterations[i]))
            if self.iterations[i] == self.screen_rect.height:
                self.screen.blit(self.background_images[i], (0, - self.screen_rect.height + self.iterations[i]))
                self.iterations[i] = 0
            self.iterations[i] += (i + 1)


