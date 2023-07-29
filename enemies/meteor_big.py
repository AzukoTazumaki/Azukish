from pygame import Surface, mask, image as img
from pygame.time import get_ticks
from pygame.transform import scale, rotate

from enemies.enemy import Enemy
from settings import METEOR_BIG_SIZES, METEORS_BIG_IMG
from random import choice, randrange


class MeteorBig(Enemy):
    def __init__(self, screen: Surface):
        super().__init__(screen)
        self.size = choice(METEOR_BIG_SIZES)
        self.image_orig = scale(img.load(choice(METEORS_BIG_IMG)).convert_alpha(), self.size)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.mask = mask.from_surface(self.image)
        self.start_position()

    def update(self):
        super().update()
        self.rotate()
        self.rect.x += self.speed_x
        self.speed_x = -self.speed_x \
            if self.rect.left < 0 or self.rect.right > self.screen_rect.width else self.speed_x
