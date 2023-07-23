import pygame
from game import Game
from settings import CAPTION, IMG_DIR

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption(CAPTION)
    game = Game(IMG_DIR)
    game.run()
    pygame.quit()
