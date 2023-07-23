from pygame.sprite import Sprite, Group, groupcollide, spritecollide
from pygame import key, K_LEFT, K_RIGHT, K_SPACE, time, image as img, transform
from settings import PLAYER_SPEED, PLAYER_SIZE, BULLET_COOLDOWN, LAST_SHOOT_TIME, IMG_DIR
from bullet import Bullet
from create_enemy import CreateEnemy
from screen import Screen
from os import path


class Player(Sprite):
    screen = Screen().set_mode_screen()
    image = img.load(path.join(IMG_DIR, 'player.png')).convert_alpha()
    transform.scale(image, PLAYER_SIZE)

    def __init__(self, enemies: Group):
        super().__init__()
        self.screen_rect = self.screen.get_rect()
        self.enemies = enemies
        self.speed = PLAYER_SPEED
        self.rect = self.image.get_rect()
        self.cooldown = BULLET_COOLDOWN
        self.last_shoot_time = LAST_SHOOT_TIME
        self.bullets_group = Group()
        self.start_position()

    def start_position(self):
        self.rect.centerx = self.screen_rect.width / 2
        self.rect.bottom = self.screen_rect.height - 20

    def update(self):
        keys = key.get_pressed()
        ticks = time.get_ticks()
        if keys[K_LEFT]:
            self.rect.x -= self.speed
        elif keys[K_RIGHT]:
            self.rect.x += self.speed
        self.check_sides()
        if keys[K_SPACE] and (self.last_shoot_time + self.cooldown) < ticks and len(self.bullets_group) <= 3:
            self.shoot()
            self.last_shoot_time = ticks
        self.draw_bullets()
        self.check_collides()

    def draw_bullets(self):
        self.bullets_group.update()
        self.bullets_group.draw(self.screen)

    def check_collides(self):
        if groupcollide(self.bullets_group, self.enemies, True, True):
            self.enemies.add(CreateEnemy().create_one_enemy())
        if spritecollide(self, self.enemies, True):
            self.kill()
            del self

    def check_sides(self):
        self.rect.left = max(0, self.rect.left)
        self.rect.right = min(self.screen_rect.width, self.rect.right)

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.centery - self.rect.height)
        self.bullets_group.add(bullet)
