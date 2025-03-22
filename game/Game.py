import pygame

from game.CONSTANTS import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION, MUSIC
from game.Level import Level
from game.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        pygame.mixer_music.load(MUSIC)
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(.15)
        
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0]]:
                level = Level(self.window, 'level_1', menu_return)
                level.run()

            if menu_return == MENU_OPTION[1]:
                pygame.quit()
                quit()
