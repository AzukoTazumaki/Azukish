from pygame.sprite import Group
from enemy import Enemy
from screen import Screen
from meteor_small import MeteorSmall
from meteor_big import MeteorBig
from ufo import UFO
from random import choice
from settings import AMOUNT_OF_ENEMIES


class CreateEnemy:
    screen = Screen().set_mode_screen()
    all_enemies = [Enemy, MeteorSmall, MeteorBig, UFO]

    def __init__(self):
        self.enemies = Group()

    def start_enemies(self):
        for _ in range(AMOUNT_OF_ENEMIES):
            enemy = choice(self.all_enemies)()
            self.enemies.add(enemy)
        return self.enemies

    def create_one_enemy(self):
        enemy = choice(self.all_enemies)()
        self.enemies.add(enemy)
        return self.enemies
