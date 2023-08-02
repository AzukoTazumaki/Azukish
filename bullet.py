from pygame import Surface, mask, image as img
from pygame.sprite import Sprite
from pygame.time import get_ticks
from pygame.transform import scale
from settings import BULLET_SPEED, BULLET_SIZE, BULLETS_IMG, BULLET_WAIT_NEXT_FRAME


class Bullet(Sprite):
    def __init__(self, screen: Surface, x: int, y: int):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.speed = BULLET_SPEED
        self.frames = [scale(img.load(i).convert_alpha(), BULLET_SIZE) for i in BULLETS_IMG]
        self.index = 0
        self.image = self.frames[self.index]
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.mask = mask.from_surface(self.image)
        self.last_time = get_ticks()
        self.wait_next_frame = BULLET_WAIT_NEXT_FRAME

    def animation(self):
        self.index += 1
        if self.index >= len(self.frames):
            self.index = 0
        self.image = self.frames[self.index]

    def update(self):
        now = get_ticks()
        if now - self.last_time >= self.wait_next_frame:
            self.last_time = now
            self.animation()
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()

