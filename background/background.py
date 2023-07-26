from pygame import image, time
from settings import IMG_DIR, FPS
from os import path


class Background:
    def __init__(self, screen, iteration=0):
        self.image_direction = IMG_DIR
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.background = image.load(path.join(self.image_direction, 'background.png')).convert()
        self.stars_1 = image.load(path.join(self.image_direction, 'stars_1.png')).convert_alpha()
        self.stars_2 = image.load(path.join(self.image_direction, 'stars_2.png')).convert_alpha()
        self.background_rect = self.background.get_rect()
        self.stars_1_rect = self.stars_1.get_rect()
        self.stars_2_rect = self.stars_2.get_rect()
        self.iteration = iteration
        self.clock = time.Clock()

    def blit_background(self):
        for i in range(round(self.screen_rect.height / self.background_rect.height)):
            self.screen.blit(self.background, (0, self.background_rect.height * i))

    def blit_stars(self):
        for i in range(round(self.screen_rect.height / self.stars_1_rect.height)):
            self.screen.blit(self.stars_1, (0, self.stars_1_rect.height * i))
            self.screen.blit(self.stars_2, (0, self.stars_2_rect.height * i))


