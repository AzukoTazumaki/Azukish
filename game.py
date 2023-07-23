from os import path
from pygame import display, time, event as events, QUIT, image, transform, KEYDOWN, K_SPACE
from pygame.sprite import Group
from settings import FPS, RUN
from screen import Screen
from player import Player
from create_enemy import CreateEnemy


class Game:
    screen = Screen().set_mode_screen()
    enemies = CreateEnemy().start_enemies()
    player = Player(enemies)

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
        background_original = image.load(path.join(self.image_direction, 'background.jpg')).convert()
        background_smooth = transform.scale(background_original, (self.screen_rect.width, self.screen_rect.height))
        return background_smooth

    def run(self):
        loaded_graphic = self.load_graphic()
        self.load_player().update()
        while not self.run_game:
            self.clock.tick(FPS)
            for event in events.get():
                if event.type == QUIT:
                    self.run_game = True
            self.screen.blit(loaded_graphic, loaded_graphic.get_rect())
            loaded_enemies = self.load_enemies()
            loaded_enemies.update()
            self.all_sprites.draw(self.screen)
            display.flip()
