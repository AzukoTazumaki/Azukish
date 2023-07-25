from os import path
from pygame import display, time, event as events, QUIT, image
from pygame.sprite import Group
from settings import FPS, RUN
from screen import Screen
from player import Player
from enemies.create_enemy import CreateEnemy
from background.background import Background


class Game:
    screen = Screen().set_mode_screen()
    enemies = CreateEnemy().start_enemies()
    player = Player(enemies)
    background = Background()

    def __init__(self, image_direction):
        self.clock = time.Clock()
        self.run_game = RUN
        self.all_sprites = Group()
        self.screen_rect = self.screen.get_rect()
        self.image_direction = image_direction

    def load_enemies(self) -> Group:
        for enemy in self.enemies:
            self.all_sprites.add(enemy)
        return self.all_sprites

    def load_player(self) -> Group:
        self.all_sprites.add(self.player)
        return self.all_sprites

    def load_graphic(self):
        background = image.load(path.join(self.image_direction, 'background.png')).convert()
        return background

    def run(self):
        self.load_player().update()
        while not self.run_game:
            self.clock.tick(FPS)
            self.background.blit_background()
            self.background.blit_stars()
            loaded_enemies = self.load_enemies()
            loaded_enemies.update()
            self.all_sprites.draw(self.screen)
            for event in events.get():
                if event.type == QUIT:
                    self.run_game = True
            display.update()
