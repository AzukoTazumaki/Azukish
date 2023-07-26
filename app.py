import pygame
from game import Game
from screen import Screen
from settings import CAPTION, IMG_DIR, DESKTOP_SIZES

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption(CAPTION)
    game = Game(IMG_DIR, Screen(DESKTOP_SIZES).set_mode_screen())
    game.run()
    pygame.quit()
