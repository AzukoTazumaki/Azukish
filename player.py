from pygame.sprite import Sprite, Group, groupcollide, spritecollide, collide_mask
from pygame import key, K_LEFT, K_RIGHT, K_SPACE, time, image as img, transform, Surface, draw, mask
from settings import PLAYER_SPEED, PLAYER_SIZE, PLAYER_IMG, BULLET_COOLDOWN, LAST_SHOOT_TIME, AMOUNT_OF_BULLETS
from bullet import Bullet
from enemies.create_enemy import CreateEnemy


class Player(Sprite):
    def __init__(self, enemies: Group, screen: Surface):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.enemies = enemies
        self.image = transform.scale(img.load(PLAYER_IMG).convert_alpha(), PLAYER_SIZE)
        self.rect = self.image.get_rect()
        self.mask = mask.from_surface(self.image)
        self.speed = PLAYER_SPEED
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
        if keys[K_SPACE] and (self.last_shoot_time + self.cooldown) < ticks and len(self.bullets_group) < AMOUNT_OF_BULLETS:
            self.shoot()
            self.last_shoot_time = ticks
        self.draw_bullets()
        self.check_collides()

    def draw_bullets(self):
        self.bullets_group.update()
        self.bullets_group.draw(self.screen)

    def check_collides(self):
        if groupcollide(self.bullets_group, self.enemies, True, True, collide_mask):
            self.enemies.add(CreateEnemy(self.screen).create_one_enemy())
        if spritecollide(self, self.enemies, True, collide_mask):
            self.kill()

    def check_sides(self):
        self.rect.left = max(-self.rect.width / 2, self.rect.left)
        self.rect.right = min(self.screen_rect.width + self.rect.width / 2, self.rect.right)

    def shoot(self):
        bullet = Bullet(self.screen, self.rect.centerx, self.rect.centery - self.rect.height / 2)
        self.bullets_group.add(bullet)
