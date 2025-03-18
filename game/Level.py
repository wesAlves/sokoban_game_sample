import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from game.CONSTANTS import FONT_MENU, WHITE, PLAYER
from game.Player import Player


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list = []

        self.player = Player(PLAYER[0], (32, 32), 'Player')
        self.entity_list.append(self.player)

    def run(self):
        while True:
            self.level_text(14, f'Level name{self.name}', WHITE, (10, 5))

            for entity in self.entity_list:
                self.window.blit(source=entity.surf, dest=entity.rect)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.KEYDOWN:
                        self.player.move()

            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.Font(FONT_MENU, size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
