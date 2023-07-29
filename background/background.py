from pygame import image, Surface
from pygame.transform import scale
from settings import BACKGROUND_IMG, MAIN_STARS_IMG, ADDITIONAL_STARS


class Background:
    def __init__(self, screen: Surface):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.size = self.screen.get_size()
        self.background_images = [
            scale(image.load(BACKGROUND_IMG).convert_alpha(), self.size),
            scale(image.load(MAIN_STARS_IMG).convert_alpha(), self.size),
            scale(image.load(ADDITIONAL_STARS).convert_alpha(), self.size)
        ]
        self.iterations = [0, 0, 0]

    def load_background(self):
        for i in range(3):
            self.screen.blit(self.background_images[i], (0, self.iterations[i]))
            self.screen.blit(self.background_images[i], (0, - self.screen_rect.height + self.iterations[i]))
            if self.iterations[i] == self.screen_rect.height:
                self.screen.blit(self.background_images[i], (0, self.iterations[i]))
                self.iterations[i] = 0
            self.iterations[i] += (i + 1)


