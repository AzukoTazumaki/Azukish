from os import path

# ———————————IMAGES—FOLDER———————————
IMG_DIR = path.join(path.dirname(__file__), 'images')
ENEMIES_DIR = path.join(IMG_DIR, 'enemies')
METEORS_DIR = path.join(ENEMIES_DIR, 'meteors')
UFO_DIR = path.join(ENEMIES_DIR, 'ufo')

# ———————————IMAGES———————————
PLAYER_IMG = path.join(IMG_DIR, 'player', 'player.png')
BULLETS_IMG = [path.join(IMG_DIR, 'player', 'bullet', f'bullet0{i}.png') for i in range(3)]
BACKGROUND_IMG = path.join(IMG_DIR, 'background', 'background.png')
MAIN_STARS_IMG = path.join(IMG_DIR, 'background', 'stars_1.png')
ADDITIONAL_STARS = path.join(IMG_DIR, 'background', 'stars_2.png')
UFO_IMG = path.join(UFO_DIR, 'ufo.png')
PLANETS_IMG = [path.join(IMG_DIR, 'planets', f'planet0{i}.png') for i in range(10)]
METEORS_IMG = path.join(METEORS_DIR, f'meteor.png')

# ———————————EXPLOSION———————————
EXPLOSIONS = [path.join(IMG_DIR, 'explosions', f'Explosion_{i}.png') for i in range(1, 10)]
EXPLOSION_SIZE = 150, 150

# ———————————ENEMIES—NAIRAN———————————
ENEMIES_NAIRAN_IMG = [path.join(IMG_DIR, 'enemies', 'nairan', f'enemy0{i}.png') for i in range(8)]

# ———————————DEFAULT—SETTINGS———————————
RUN = False
DESKTOP_SIZES = 1280, 720
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
    5.5, 5.6, 5.7
)
ENEMIES_SPEEDS_X = (1, -1, 2, -2)
ENEMIES_SIZES = (
    (100, 100), (120, 120),
    (140, 140), (160, 160)
)
AMOUNT_OF_ENEMIES = 8

# ———————————UFO—SETTINGS———————————
UFO_SIZE = 60, 60

# ———————————METEOR—SETTINGS———————————
METEOR_SIZES = (
    (100, 100), (120, 120), (140, 140)
)

# ———————————BULLET—SETTINGS———————————
BULLET_SPEED = 5
BULLET_SIZE = (70, 70)
BULLET_COOLDOWN = 100
AMOUNT_OF_BULLETS = 100
BULLET_WAIT_NEXT_FRAME = 100


YELLOW = 255, 255, 0
BLUE = 0, 0, 255
RED = 255, 0, 0
GREEN = 0, 255, 0
VIOLET = 0, 255, 255
