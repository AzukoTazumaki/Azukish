from pygame import Surface, mask, image as img
from pygame.transform import scale

from enemies.enemy import Enemy
from settings import METEOR_SMALL_SIZES, METEORS_SMALL_IMG
from random import choice


class MeteorSmall(Enemy):
    def __init__(self, screen: Surface):
        super().__init__(screen)
        self.size = choice(METEOR_SMALL_SIZES)
        self.image_orig = scale(img.load(choice(METEORS_SMALL_IMG)).convert_alpha(), self.size)
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
