from pygame import transform, Surface
from pygame.sprite import Sprite
from pygame import image as img
from random import choice, randint
from settings import ENEMIES_SIZES, ENEMIES_SPEEDS_X, ENEMIES_SPEEDS_Y, IMG_DIR, RED
from screen import Screen
from os import path


class Enemy(Sprite):
    screen = Screen().set_mode_screen()
    # image = img.load(path.join(IMG_DIR, 'enemy_ufo.png')).convert_alpha()

    def __init__(self):
        super().__init__()
        self.screen_rect = self.screen.get_rect()
        # self.image = transform.scale(self.image, choice(ENEMIES_SIZES))
        self.size = choice(ENEMIES_SIZES)
        self.image = Surface(self.size)
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.speed_y = choice(ENEMIES_SPEEDS_Y)
        self.speed_x = choice(ENEMIES_SPEEDS_X)
        self.start_position()

    def start_position(self):
        self.rect.x = randint(0, self.screen_rect.width - self.rect.width)
        self.rect.bottom = randint(-self.rect.height * 2, 0)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > self.screen_rect.height:
            self.start_position()

