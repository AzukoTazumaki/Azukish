from os import path

# ———————————IMAGES—FOLDER———————————
IMG_DIR = path.join(path.dirname(__file__), 'images')
METEORS_BIG_DIR = path.join(IMG_DIR, 'enemies', 'meteors', 'meteor_big')
METEORS_SMALL_DIR = path.join(IMG_DIR, 'enemies', 'meteors', 'meteor_small')

# ———————————IMAGES———————————
PLAYER_IMG = path.join(IMG_DIR, 'player.png')
BACKGROUND_IMG = path.join(IMG_DIR, 'background.png')
MAIN_STARS_IMG = path.join(IMG_DIR, 'stars_1.png')
ADDITIONAL_STARS = path.join(IMG_DIR, 'stars_2.png')
UFO_IMG = path.join(IMG_DIR, 'enemy_ufo.png')
PLANETS_IMG = [path.join(IMG_DIR, 'planets', f'planet0{i}.png') for i in range(10)]
ENEMIES_NAIRAN_IMG = [path.join(IMG_DIR, 'enemies', 'nairan', f'enemy0{i}.png') for i in range(8)]
METEORS_BIG_IMG = [path.join(METEORS_BIG_DIR, f'meteor_big_0{i}.png') for i in range(8)]
METEORS_SMALL_IMG = [path.join(METEORS_SMALL_DIR, f'meteor_small_0{i}.png') for i in range(4)]


# ———————————DEFAULT—SETTINGS———————————
RUN = False
DESKTOP_SIZES = 600, 900
FPS = 60
CAPTION = 'AZUKISH'
LAST_SHOOT_TIME = 0

# ———————————PLANET—SETTINGS———————————
PLANET_SPEED = 1
PLANET_SIZES = (
    (800, 800), (1000, 1000),
    (1200, 1200), (1400, 1400)
)

# ———————————PLAYER—SETTINGS———————————
PLAYER_SPEED = 10
PLAYER_SIZE = 100, 100

# ———————————ENEMIES—SETTINGS———————————
ENEMIES_SPEEDS_Y = (
    2.5, 2.6, 2.7,
    3.5, 3.6, 3.7,
    4.5, 4.6, 4.7,
    5.5, 5.6, 5.7,
)
ENEMIES_SPEEDS_X = (1, -1, 2, -2)
ENEMIES_SIZES = (
    (100, 100), (120, 120),
    (140, 140), (160, 160)
)
AMOUNT_OF_ENEMIES = 5

# ———————————UFO—SETTINGS———————————
UFO_SIZE = 100, 100

# ———————————METEOR—SETTINGS———————————
METEOR_SMALL_SIZES = (
    (40, 40), (50, 50), (60, 60)
)
METEOR_BIG_SIZES = (
    (80, 80), (90, 90), (100, 100)
)

# ———————————BULLET—SETTINGS———————————
BULLET_SPEED = 10
BULLET_SIZE = (4, 30)
BULLET_COOLDOWN = 100
AMOUNT_OF_BULLETS = 100

YELLOW = 255, 255, 0
BLUE = 0, 0, 255
RED = 255, 0, 0
GREEN = 0, 255, 0
VIOLET = 0, 255, 255
