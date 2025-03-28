import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from game import LEVELS_MTX
from game.Box import Box
from game.CONSTANTS import WHITE, PLAYER, FLOOR, WALL, BOX, SHIP, MUSIC, WIN_WIDTH
from game.EndGame import EndGame
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
        self.player_level = LEVELS_MTX.LEVEL_REF
        self.player = ""
        self.prev_element = ""
        self.ship_wall = []
        self.current_level = 1

    def run(self):
        self.copy_level_to_level_ref()
        self.set_game_mtx(self.player_level)
        pygame.mixer_music.load(MUSIC)
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(.15)

        while True:
            for entity in self.entity_list:
                self.window.blit(source=entity.surf, dest=entity.rect)

            for event in pygame.event.get():
                pressed_key = pygame.key.get_pressed()

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if pressed_key[pygame.K_ESCAPE]:
                        pygame.quit()
                        sys.exit()

                    if pressed_key[pygame.K_r]:
                        self.set_game_mtx(self.level_mtx)
                        self.copy_level_to_level_ref()

                    # get player position in all directions
                    player_pos = self.player.rect
                    x = int(self.player.rect.left / 64)
                    y = int(self.player.rect.top / 64)

                    if pressed_key[pygame.K_UP]:
                        if player_pos.top > 64:
                            self.verify_valid_move(x, y, x, y - 1)

                    if pressed_key[pygame.K_DOWN]:
                        if player_pos.top < 640:
                            self.verify_valid_move(x, y, x, y + 1)

                    if pressed_key[pygame.K_RIGHT]:
                        if player_pos.left < 640 - 128:
                            self.verify_valid_move(x, y, x + 1, y)

                    if pressed_key[pygame.K_LEFT]:
                        if player_pos.left > 64:
                            self.verify_valid_move(x, y, x - 1, y)

            self.level_text(24, "RU: 4596063", WHITE, (24, 24))
            self.level_text(18, f'Level {self.current_level}', WHITE, (24, 5))

            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        # text_font: Font = pygame.font.Font(FONT_MENU, size=text_size)
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

    def set_game_mtx(self, mtx):
        self.verify_is_solved()
        level_mtx = mtx
        self.entity_list = []

        for y, row in enumerate(level_mtx):
            for x, tile in enumerate(row):
                if tile is not 's':
                    f = Floor('regular', FLOOR[0][0], position=(x * 64, y * 64))
                    self.entity_list.append(f)

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

                        case 'wibr':
                            t = WALL[8]
                        case 'wibl':
                            t = WALL[9]

                        case 'witr':
                            t = WALL[10]

                        case 'witl':
                            t = WALL[11]

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
                            t = BOX[0][2]
                    box = Box('BOX', t, position=(x * 64, y * 64))
                    self.entity_list.append(box)

                if tile.startswith('s'):
                    t = SHIP[int(tile.split("_")[1])]
                    w = Wall('ship', t, position=(x * 64, y * 64))
                    self.ship_wall.append(w)
                    self.entity_list.append(w)

                if tile == 'p1':
                    p = Player(PLAYER[0], (0, 0), 'Player')
                    self.player = p
                    self.entity_list.append(self.player)
                    p.rect.left = x * 64
                    p.rect.top = y * 64

    def verify_valid_move(self, from_x=0, from_y=0, to_x=0, to_y=0):
        player_pos = self.player_level[from_y][from_x]
        desire_pos = self.player_level[to_y][to_x]

        if desire_pos == "" or desire_pos == "bm" or desire_pos == "bp":

            if desire_pos is "bp":
                self.player_level[to_y][to_x] = player_pos
                self.prev_element = desire_pos
                self.player_level[from_y][from_x] = ""
            elif desire_pos is "bm":
                t_pos = self.player_level[to_y - 1][to_x]
                r_pos = self.player_level[to_y][to_x + 1]
                b_pos = self.player_level[to_y + 1][to_x]
                l_pos = self.player_level[to_y][to_x - 1]

                if not t_pos.startswith('w') and not b_pos.startswith('w') and not t_pos.startswith(
                        's') and not b_pos.startswith('s') and t_pos != 'bm' and not b_pos == 'bm':
                    if from_y < to_y:
                        self.player_level[to_y][to_x] = player_pos
                        self.player_level[to_y + 1][to_x] = desire_pos if b_pos != "bp" else 'bot'
                        self.player_level[from_y][from_x] = ""
                    if from_y > to_y:
                        self.player_level[to_y][to_x] = player_pos
                        self.player_level[to_y - 1][to_x] = desire_pos if t_pos != "bp" else 'bot'
                        self.player_level[from_y][from_x] = ""

                if not r_pos.startswith('w') and not l_pos.startswith('w') and not r_pos.startswith(
                        's') and not l_pos.startswith('s') and not r_pos == 'bm' and not l_pos == 'bm':
                    if from_x < to_x:
                        self.player_level[to_y][to_x] = player_pos
                        self.player_level[to_y][to_x + 1] = desire_pos if r_pos != "bp" else 'bot'
                        self.player_level[from_y][from_x] = ""

                    if from_x > to_x:
                        self.player_level[to_y][to_x] = player_pos
                        self.player_level[to_y][to_x - 1] = desire_pos if l_pos != "bp" else 'bot'
                        self.player_level[from_y][from_x] = ""


            else:
                self.player_level[to_y][to_x] = player_pos
                self.player_level[from_y][from_x] = self.prev_element
                self.prev_element = ""

            self.set_game_mtx(self.player_level)

        else:
            print('can not move')

    def copy_level_to_level_ref(self):
        for y, row in enumerate(self.level_mtx):
            for x, tile in enumerate(row):
                self.player_level[y][x] = tile

    def verify_is_solved(self):
        target_position = []
        boxes_position = []

        for y, row in enumerate(self.level_mtx):
            for x, tile in enumerate(row):
                if tile == 'bp':
                    target_position.append([y, x])
                    boxes_position.append(False)

        for y, row in enumerate(self.player_level):
            for x, tile in enumerate(row):
                if tile == "bot":
                    if target_position.__contains__([y, x]):
                        index = target_position.index([y, x])
                        boxes_position[index] = True

        if all(boxes_position):
            self.current_level += 1
            if self.current_level <= 3:
                match self.current_level:
                    case 2:
                        self.level_mtx = LEVELS_MTX.LEVEL_2
                    case 3:
                        self.level_mtx = LEVELS_MTX.LEVEL_3
                self.copy_level_to_level_ref()
                self.set_game_mtx(self.level_mtx)
            else:
                win = EndGame(self.window)
                win.run()
