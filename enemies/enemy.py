from pygame import Surface, image as img, Rect, draw, mask
from pygame.transform import scale, rotate
from pygame.sprite import Sprite
from random import choice, randint
from settings import ENEMIES_SIZES, ENEMIES_SPEEDS_X, ENEMIES_SPEEDS_Y, ENEMIES_NAIRAN_IMG


class Enemy(Sprite):
    def __init__(self, screen: Surface):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.size = choice(ENEMIES_SIZES)
        self.width = self.size[0]
        self.height = self.size[1]
        self.image = scale(img.load(choice(ENEMIES_NAIRAN_IMG)), (self.width * 1.2, self.height * 1.2))
        self.rect = self.image.get_rect()
        self.mask = mask.from_surface(self.image)
        self.speed_x = choice(ENEMIES_SPEEDS_X)
        self.speed_y = choice(ENEMIES_SPEEDS_Y)
        self.start_position()

    def start_position(self):
        self.rect.x = randint(self.screen_rect.left, self.screen_rect.width - self.rect.width)
        self.rect.y = randint(- self.rect.height * 2, - self.rect.height)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > self.screen_rect.height:
            self.start_position()
