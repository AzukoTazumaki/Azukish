from pygame import Surface, mask
from enemies.enemy import Enemy
from settings import METEOR_SMALL_SIZES, BLUE
from random import choice


class MeteorSmall(Enemy):
    def __init__(self, screen):
        super().__init__(screen)
        self.size = choice(METEOR_SMALL_SIZES)
        self.image = Surface(self.size)
        self.image.fill(BLUE)
        self.rect.width = self.size[0]
        self.rect.height = self.size[1]
        self.mask = mask.from_surface(self.image)

    def update(self):
        super().update()
        self.rect.x += self.speed_x
        self.speed_x = -self.speed_x \
            if self.rect.left < 0 or self.rect.right > self.screen_rect.width else self.speed_x
