import pygame
from pygame import Surface, Rect
from pygame.font import Font

from game.CONSTANTS import WIN_WIDTH, MENU_BG_0, FONT_MENU, GREEN, BLUE, WIN_HEIGHT, \
    MENU_OPTION, GREEN_YELLOW, PALE_BLUE, WHITE, TRANSPARENT_WHITE


class EndGame:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.transform.scale(pygame.image.load(MENU_BG_0).convert_alpha(), (WIN_WIDTH, WIN_HEIGHT))
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        while True:
            self.window.blit(source=self.surf, dest=self.rect)

            self.menu_text(32, "STELLAR REPAIR", BLUE, ((WIN_WIDTH / 2), 128))
            self.menu_text(24, "Sokoban odyssey", GREEN, ((WIN_WIDTH / 2), 168))
            
            
            self.menu_text(24, "PARABENS!!!", TRANSPARENT_WHITE, ((WIN_WIDTH / 2), 224), 'x')
            self.menu_text(24, "Você completou todos os nívies", TRANSPARENT_WHITE, ((WIN_WIDTH / 2), 248), 'x')
            
            self.menu_text(24, "Desenvolvido por: ", TRANSPARENT_WHITE, ((WIN_WIDTH / 2), 320), "x")
            self.menu_text(24, "Wesley Alberto Alves Benvindo", WHITE, ((WIN_WIDTH / 2), 340), "x")
            self.menu_text(24, "RU: 4596063", WHITE, ((WIN_WIDTH / 2), 360), "x")


            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

              

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, font=None):
        if font:
            text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        else:
            text_font: Font = pygame.font.Font(FONT_MENU, size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
