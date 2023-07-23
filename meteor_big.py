from pygame import Surface, transform, display
from enemy import Enemy
from settings import METEOR_BIG_SIZES, VIOLET
from random import choice, randint


class MeteorBig(Enemy):
    def __init__(self):
        super().__init__()
        self.image = Surface(choice(METEOR_BIG_SIZES))
        self.image.fill(VIOLET)

    def update(self):
        super().update()
        self.rect.x += self.speed_x
        self.speed_x = -self.speed_x \
            if self.rect.left < 0 or self.rect.right > self.screen_rect.width else self.speed_x
