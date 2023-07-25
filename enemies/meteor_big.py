from pygame import Surface
from enemies.enemy import Enemy
from settings import METEOR_BIG_SIZES, VIOLET
from random import choice


class MeteorBig(Enemy):
    def __init__(self):
        super().__init__()
        self.size = choice(METEOR_BIG_SIZES)
        self.image = Surface(self.size)
        self.image.fill(VIOLET)
        self.rect.width = self.size[0]
        self.rect.height = self.size[1]

    def update(self):
        super().update()
        self.rect.x += self.speed_x
        self.speed_x = -self.speed_x \
            if self.rect.left < 0 or self.rect.right > self.screen_rect.width else self.speed_x
