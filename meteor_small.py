from pygame import Surface
from enemy import Enemy
from settings import METEOR_SMALL_SIZES, BLUE
from random import choice


class MeteorSmall(Enemy):
    def __init__(self):
        super().__init__()
        self.image = Surface(choice(METEOR_SMALL_SIZES))
        self.image.fill(BLUE)

    def update(self):
        super().update()
        self.rect.x += self.speed_x
        self.speed_x = -self.speed_x \
            if self.rect.left < 0 or self.rect.right > self.screen_rect.width else self.speed_x
