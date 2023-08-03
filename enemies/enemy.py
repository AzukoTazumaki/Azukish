from pygame import Surface, image as img, Rect, draw, mask
from pygame.time import get_ticks
from pygame.transform import scale, rotate
from pygame.sprite import Sprite
from random import choice, randint, randrange
from settings import ENEMIES_SIZES, ENEMIES_SPEEDS_X, ENEMIES_SPEEDS_Y, ENEMIES_NAIRAN_IMG, EXPLOSIONS, EXPLOSION_SIZE


class Enemy(Sprite):
    def __init__(self, screen: Surface):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.size = choice(ENEMIES_SIZES)
        self.width = self.size[0]
        self.height = self.size[1]
        self.image_orig = rotate(scale(img.load(choice(ENEMIES_NAIRAN_IMG)), (self.width * 1.2, self.height * 1.2)), 180)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.mask = mask.from_surface(self.image)
        self.speed_x = choice(ENEMIES_SPEEDS_X)
        self.speed_y = choice(ENEMIES_SPEEDS_Y)
        self.start_position()
        self.last_update = get_ticks()
        self.rot = 0
        self.rot_speed = randrange(-8, 8)
        self.animation_count = 0
        self.animation_frames = 2
        self.animation = False
        self.frames = [scale(img.load(i), EXPLOSION_SIZE).convert_alpha() for i in EXPLOSIONS]

    def start_animation(self):
        self.animation = True

    def start_position(self):
        self.rect.x = randint(self.screen_rect.left, self.screen_rect.width - self.rect.width)
        self.rect.bottom = randint(- self.rect.height * 2, - self.rect.height)

    def update(self):
        if self.animation:
            image_index = self.animation_count // self.animation_frames
            self.animation_count += 1
            if image_index < len(self.frames):
                self.image = self.frames[image_index]
            else:
                self.kill()
        self.rect.y += self.speed_y
        if self.rect.top > self.screen_rect.height:
            self.start_position()
