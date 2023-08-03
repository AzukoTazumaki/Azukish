# DRAFT CLASS

from pygame.sprite import Sprite, Group
from settings import EXPLOSIONS
from pygame import image as img
from pygame.transform import scale


class Explosion(Sprite):
    def __init__(self):
        super().__init__()
        self.frames = [scale(img.load(i), (150, 150)).convert_alpha() for i in EXPLOSIONS]
        self.index = 0
        self.image = self.frames[self.index]
        self.rect = self.image.get_rect()
        self.animation_count = 0
        self.animation_frames = 3
        self.animation = False

    def update(self):
        image_index = self.animation_count // self.animation_frames
        self.animation_count += 1
        if image_index < len(self.frames):
            self.image = self.frames[image_index]
        else:
            self.kill()

