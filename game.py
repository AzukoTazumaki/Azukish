from pygame import display, time, event, QUIT
from pygame.sprite import Group
from settings import FPS, RUN
from player import Player
from enemies.create_enemy import CreateEnemy
from background.background import Background


class Game:
    def __init__(self, image_direction, screen):
        self.clock = time.Clock()
        self.run_game = RUN
        self.all_sprites = Group()
        self.screen = screen
        self.enemies = CreateEnemy(self.screen).start_enemies()
        self.screen_rect = self.screen.get_rect()
        self.player = Player(self.enemies, self.screen)
        self.background = Background(self.screen)
        self.image_direction = image_direction

    def load_enemies(self) -> Group:
        for enemy in self.enemies:
            self.all_sprites.add(enemy)
        return self.all_sprites

    def load_player(self) -> Group:
        self.all_sprites.add(self.player)
        return self.all_sprites

    def run(self):
        self.load_player().update()
        while not self.run_game:
            self.clock.tick(FPS)
            self.background.load_background()
            loaded_enemies = self.load_enemies()
            loaded_enemies.update()
            self.all_sprites.draw(self.screen)
            for e in event.get():
                if e.type == QUIT:
                    self.run_game = True
            display.update()
