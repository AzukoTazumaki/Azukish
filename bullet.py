from pygame import Surface, mask
from pygame.sprite import Sprite
from settings import BULLET_SPEED, BULLET_SIZE, YELLOW


class Bullet(Sprite):
    def __init__(self, screen: Surface, x: int, y: int):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.speed = BULLET_SPEED
        self.image = Surface(BULLET_SIZE)
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.mask = mask.from_surface(self.image)

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < self.rect.height - self.rect.height:
            self.kill()
