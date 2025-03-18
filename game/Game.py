import pygame

from game.CONSTANTS import WIN_WIDTH, WIN_HEIGHT
from game.Level import Level


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            level = Level(self.window, 'level_1', "New Game")
            level.run()

            pygame.quit()
            quit()
