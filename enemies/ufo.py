from enemies.enemy import Enemy
from pygame import image as img, transform, mask
from settings import UFO_SIZE, UFO_IMG


class UFO(Enemy):
    def __init__(self, screen):
        super().__init__(screen)
        self.image = img.load(UFO_IMG).convert_alpha()
        self.rect.width = UFO_SIZE[0]
        self.rect.height = UFO_SIZE[1]
        self.image = transform.scale(self.image, UFO_SIZE)
        self.mask = mask.from_surface(self.image)
