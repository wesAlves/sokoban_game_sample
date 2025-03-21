import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from game import LEVELS_MTX
from game.Box import Box
from game.CONSTANTS import FONT_MENU, WHITE, PLAYER, FLOOR, WALL, BOX
from game.Floor import Floor
from game.Player import Player
from game.Wall import Wall


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list = []
        self.level_mtx = LEVELS_MTX.LEVEL_1
        self.player = ""
        # self.player = Player(PLAYER[0], (0, 0), 'Player')
        # self.entity_list.append(self.player)
        # self.base_floor_tile = Floor('base')
        # self.f = Floor('regular', FLOOR[0][0], position=(64, 64))
        # self.entity_list.append(self.f)

    def run(self):
        self.set_game_mtx()

        while True:
            self.level_text(14, f'Level name{self.name}', WHITE, (10, 5))

            for entity in self.entity_list:
                self.window.blit(source=entity.surf, dest=entity.rect)
            # 

            for event in pygame.event.get():
                pressed_key = pygame.key.get_pressed()

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if pressed_key[pygame.K_ESCAPE]:
                        pygame.quit()
                        sys.exit()
                    # self.player.move(self.level_mtx)

                    if pressed_key[pygame.K_r]:
                        print('reseting the game')
                        self.level_mtx = LEVELS_MTX.LEVEL_1
                        self.set_game_mtx()

                    if pressed_key[pygame.K_UP]:
                        self.player.move()

            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.Font(FONT_MENU, size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
    
    def set_game_mtx(self):
        for y, row in enumerate(self.level_mtx):
            for x, tile in enumerate(row):
                f = Floor('regular', FLOOR[0][0], position=(x * 64, y * 64))
                self.entity_list.append(f)

                if tile == 'p1':
                    p = Player(PLAYER[0], (0, 0), 'Player')
                    self.player = p
                    self.entity_list.append(self.player)
                    print('positioning player')
                    p.rect.left = x * 64
                    p.rect.top = y * 64

                if tile.startswith('w'):
                    t = WALL[0]
                    match tile:
                        case 'wtl':
                            t = WALL[4]
                        case 'wtr':
                            t = WALL[5]

                        case 'wbl':
                            t = WALL[6]
                        case 'wbr':
                            t = WALL[7]

                        case 'whb':
                            t = WALL[1]
                        case 'wht':
                            t = WALL[0]

                        case 'wvr':
                            t = WALL[3]
                        case 'wvl':
                            t = WALL[2]

                    w = Wall('regular', t, position=(x * 64, y * 64))

                    self.entity_list.append(w)

                if tile.startswith('b'):
                    t = BOX[0][0]
                    match tile:
                        case 'bm':
                            t = BOX[0][0]
                        case 'bp':
                            t = BOX[0][1]
                        case 'bot':
                            t = BOX[0][1]
                    box = Box('BOX', t, position=(x * 64, y * 64))
                    self.entity_list.append(box)
