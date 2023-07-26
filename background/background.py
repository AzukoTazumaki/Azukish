from pygame import image, time, Surface
from settings import IMG_DIR, FPS
from os import path
from random import randint

iteration = 0


class Background:

    def __init__(self, screen: Surface):
        self.image_direction = IMG_DIR
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.background = image.load(path.join(self.image_direction, 'background.png')).convert_alpha()
        self.main_stars = image.load(path.join(self.image_direction, 'stars_1.png')).convert_alpha()
        self.additional_stars = image.load(path.join(self.image_direction, 'stars_2.png')).convert_alpha()
        self.images = [
            self.background,
            self.main_stars,
            self.additional_stars
        ]
        self.iterations = [0, 0, 0]
        self.clock = time.Clock()

    def load_background(self):
        for i in range(3):
            self.screen.blit(self.images[i], (0, self.iterations[i]))
            self.screen.blit(self.images[i], (0, - self.screen_rect.height + self.iterations[i]))
            if self.iterations[i] == self.screen_rect.height:
                self.screen.blit(self.images[i], (0, - self.screen_rect.height + self.iterations[i]))
                self.iterations[i] = 0
            self.iterations[i] += (i + 1)


