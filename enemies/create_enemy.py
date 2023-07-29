from pygame import Surface
from pygame.sprite import Group
from enemies.enemy import Enemy
from enemies.meteor import Meteor
from enemies.ufo import UFO
from random import choice
from settings import AMOUNT_OF_ENEMIES


class CreateEnemy:
    def __init__(self, screen: Surface):
        self.enemies = Group()
        self.screen = screen
        self.all_enemies = [Enemy, UFO, Meteor]

    def start_enemies(self):
        for _ in range(AMOUNT_OF_ENEMIES):
            enemy = choice(self.all_enemies)(self.screen)
            self.enemies.add(enemy)
        return self.enemies

    def create_one_enemy(self):
        enemy = choice(self.all_enemies)(self.screen)
        self.enemies.add(enemy)
        return self.enemies
