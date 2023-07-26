from pygame import Surface, image, transform
from pygame.sprite import Sprite

from settings import PLANETS_IMG, PLANET_SPEED, PLANET_SIZES
from random import randint, choice


class Planet(Sprite):
    def __init__(self, screen: Surface):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.planets_img = PLANETS_IMG
        self.all_planets = [image.load(planet).convert_alpha() for planet in self.planets_img]
        self.image = transform.scale(choice(self.all_planets), choice(PLANET_SIZES))
        self.image.set_alpha(50)
        self.rect = self.image.get_rect()
        self.speed = PLANET_SPEED
        self.start_position()

    def start_position(self):
        self.rect.x = randint(0, self.screen_rect.width)
        self.rect.bottom = self.screen_rect.height - self.rect.height

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > self.screen_rect.height:
            self.image = transform.scale(choice(self.all_planets), choice(PLANET_SIZES))
            self.image.set_alpha(50)
            self.start_position()
