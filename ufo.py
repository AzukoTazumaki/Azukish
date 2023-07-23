from os import path
from enemy import Enemy
from pygame import image as img, transform, Surface
from settings import IMG_DIR, UFO_SIZE, UFO_IMG


class UFO(Enemy):
    def __init__(self):
        super().__init__()
        self.image = img.load(path.join(IMG_DIR, UFO_IMG)).convert_alpha()
        self.rect.width = UFO_SIZE[0]
        self.rect.height = UFO_SIZE[1]
        self.image = transform.scale(self.image, UFO_SIZE)
