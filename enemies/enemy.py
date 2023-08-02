from pygame import Surface, image as img, Rect, draw, mask
from pygame.time import get_ticks
from pygame.transform import scale, rotate
from pygame.sprite import Sprite
from random import choice, randint, randrange
from settings import ENEMIES_SIZES, ENEMIES_SPEEDS_X, ENEMIES_SPEEDS_Y, ENEMIES_NAIRAN_IMG, ENEMIES_NAIRAN_DESTRUCTION, ENEMY_WAIT_NEXT_FRAME


class Enemy(Sprite):
    def __init__(self, screen: Surface):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.size = choice(ENEMIES_SIZES)
        self.width = self.size[0]
        self.height = self.size[1]
        self.index = 0
        self.nairan_destruction_frames = [
            rotate(scale(img.load(i), (self.width * 1.2, self.height * 1.2)), 180)
            for i in ENEMIES_NAIRAN_DESTRUCTION
        ]
        self.animation = False
        self.image = rotate(scale(img.load(choice(ENEMIES_NAIRAN_IMG)), (self.width * 1.2, self.height * 1.2)), 180)
        self.rect = self.image.get_rect()
        self.mask = mask.from_surface(self.image)
        self.speed_x = choice(ENEMIES_SPEEDS_X)
        self.speed_y = choice(ENEMIES_SPEEDS_Y)
        self.start_position()
        self.last_update = get_ticks()
        self.rot = 0
        self.rot_speed = randrange(-8, 8)
        self.last_time = get_ticks()
        self.wait_next_frame = ENEMY_WAIT_NEXT_FRAME

    def start_position(self):
        self.rect.x = randint(self.screen_rect.left, self.screen_rect.width - self.rect.width)
        self.rect.bottom = randint(- self.rect.height * 2, - self.rect.height)

    def start_animation(self):
        self.animation = True

    def update(self):
        if self.animation:
            now = get_ticks()
            if now - self.last_time >= self.wait_next_frame:
                self.last_time = now
                self.index += 1
                if self.index > len(self.nairan_destruction_frames):
                    self.kill()
                self.image = self.nairan_destruction_frames[self.index]
        self.rect.y += self.speed_y
        if self.rect.top > self.screen_rect.height:
            self.start_position()
