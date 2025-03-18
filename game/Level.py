import pygame
from pygame import Surface, Rect
from pygame.font import Font

from game.CONSTANTS import FONT_MENU, WHITE, MENU_BG_0, WIN_HEIGHT, WIN_WIDTH


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode

    def run(self):
        while True:
            self.level_text(14, f'Level name{self.name}', WHITE, (10, 5))

            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.Font(FONT_MENU, size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
