import pygame
from pygame import Surface, Rect
from pygame.font import Font

from game.CONSTANTS import WIN_WIDTH, MENU_BG_0, FONT_MENU, GREEN, BLUE, WIN_HEIGHT, \
    MENU_OPTION, GREEN_YELLOW, PALE_BLUE, WHITE, TRANSPARENT_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.transform.scale(pygame.image.load(MENU_BG_0).convert_alpha(), (WIN_WIDTH, WIN_HEIGHT))
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0

        while True:
            self.window.blit(source=self.surf, dest=self.rect)

            self.menu_text(32, "STELLAR REPAIR", BLUE, ((WIN_WIDTH / 2), 128))
            self.menu_text(24, "Sokoban odyssey", GREEN, ((WIN_WIDTH / 2), 168))
            
            
            self.menu_text(24, "Instruções:", TRANSPARENT_WHITE, ((WIN_WIDTH / 2), 224), 'x')
            self.menu_text(24, "Pressione R para resetar o Level", TRANSPARENT_WHITE, ((WIN_WIDTH / 2), 248), 'x')
            self.menu_text(24, "Pressione ESC para sair do jogo", TRANSPARENT_WHITE, ((WIN_WIDTH / 2), 264), 'x')
            
            self.menu_text(24, "Desenvolvido por: ", TRANSPARENT_WHITE, ((WIN_WIDTH / 2), 320), "x")
            self.menu_text(32, "RU: 4596063", WHITE, ((WIN_WIDTH / 2), 360), "x")

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], GREEN_YELLOW, ((WIN_WIDTH / 2), 396 + i * 32))
                else:
                    self.menu_text(20, MENU_OPTION[i], PALE_BLUE, ((WIN_WIDTH / 2), 396 + i * 32))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                            print('menu option')
                        else:
                            menu_option = 0
                            print('menu option')

                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1

                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, font=None):
        if font:
            text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        else:
            text_font: Font = pygame.font.Font(FONT_MENU, size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
