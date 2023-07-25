from os import path

IMG_DIR = image_direction = path.join(path.dirname(__file__), 'images')

WIDTH = 1920
HEIGHT = 1080
FPS = 60
CAPTION = 'AZUKO'

PLAYER_SPEED = 10
PLAYER_SIZE = 100, 100

ENEMIES_SPEEDS_Y = (2, 3)
ENEMIES_SPEEDS_X = (1, -1, 2, -2)
ENEMIES_SIZES = (
    (30, 30), (40, 40),
    (50, 50), (60, 60),
    (70, 70), (80, 80),
    (90, 90), (100, 100)
)

UFO_IMG = 'enemy_ufo.png'
UFO_SIZE = 100, 100

AMOUNT_OF_ENEMIES = 7

METEOR_SMALL_SIZES = (
    (30, 30), (40, 40),
    (50, 50), (60, 60)
)
METEOR_BIG_SIZES = (
    (70, 70), (80, 80),
    (90, 90), (100, 100)
)

BULLET_SPEED = 10
BULLET_SIZE = (10, 30)
BULLET_COOLDOWN = 100
AMOUNT_OF_BULLETS = 10

LAST_SHOOT_TIME = 0

RUN = False

YELLOW = 255, 255, 0
BLUE = 0, 0, 255
RED = 255, 0, 0
GREEN = 0, 255, 0
VIOLET = 0, 255, 255
