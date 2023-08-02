from pygame import Surface, mask, image as img
from pygame.time import get_ticks
from pygame.transform import scale, rotate
from enemies.enemy import Enemy
from settings import METEOR_SIZES, METEORS_IMG
from random import choice


class Meteor(Enemy):
    def __init__(self, screen: Surface):
        super().__init__(screen)
        self.size = choice(METEOR_SIZES)
        self.image_orig = scale(img.load(METEORS_IMG).convert_alpha(), self.size)
        self.image = self.image_orig.copy()
        self.mask = self.set_mask()
        self.start_position()

    def set_mask(self):
        return mask.from_surface(self.image)

    def rotate(self):
        now = get_ticks()
        if now - self.last_update > 40:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = rotate(self.image_orig, self.rot)
            new_mask = self.set_mask()
            self.image = new_image
            self.mask = new_mask
            old_center = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        super().update()
        self.rotate()
        self.rect.x += self.speed_x
        self.speed_x = -self.speed_x \
            if self.rect.left < 0 or self.rect.right > self.screen_rect.width else self.speed_x
