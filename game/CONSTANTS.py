import os
from typing import Callable, Any, LiteralString

import pygame

from game.helpers.hex_to_rgb import hex_to_rgb

# ASSETS BASE PATH
ASSETS: Callable[[Any], LiteralString | str] = lambda x: os.path.join("./assets", x)

# COLOR CONTANTS
BLUE = hex_to_rgb("#55ACEE")
PALE_BLUE = hex_to_rgb("#505ca7ff")
GREEN = hex_to_rgb("#A4C639")
GREEN_YELLOW = hex_to_rgb("#eafb52ff")
PALE_GREEN_YELLOW = hex_to_rgb("#eafb52ff")
PRIMARY_COLOR = hex_to_rgb("#55ACEE")
WHITE = hex_to_rgb("#FFFFFFFF")

# ENTITY_SPEED
ENTITY_SPEED = {
    "Player": 1
}

# FONT
FONT_MENU = ASSETS('fonts/sky.ttf')

# MENU CONSTANTS
MENU_BG_0 = ASSETS("menu_bg_0.png")
MENU_BG_1 = ASSETS("menu_bg_1.png")

MENU_OPTION = ('New game', 'Random game', 'Leaderboard', 'Exit')

# PLAYER
PLAYER_KEY_UP = {'Player': pygame.K_UP, 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player': pygame.K_DOWN, 'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player': pygame.K_LEFT, 'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player': pygame.K_RIGHT, 'Player2': pygame.K_d}
PLAYER_KEY_SHOT = {'Player': pygame.K_RCTRL, 'Player2': pygame.K_LCTRL}

# TILES
BOX = (
    (ASSETS('floors/box_1_obj.png'),
     ASSETS('floors/box_1_place.png'),
     ASSETS('floors/box_1_on_target.png'),
     ),)
FLOOR = (
    (
        ASSETS('floors/floor_0_1.png'),
        ASSETS('floors/floor_1_2.png'),
        ASSETS('floors/floor_1_2.png'),
        ASSETS('floors/floor_1_3.png'),
    ),
)
PLAYER = (ASSETS('player/idle_player.png'),)
WALL = (
    ASSETS('floors/w_h_t.png'),  # 0
    ASSETS('floors/w_h_b.png'),  # 1
    ASSETS('floors/w_v_l.png'),  # 2
    ASSETS('floors/w_v_r.png'),  # 3
    ASSETS('floors/w_t_l.png'),  # 4
    ASSETS('floors/w_t_r.png'),  # 5
    ASSETS('floors/w_b_l.png'),  # 6
    ASSETS('floors/w_b_r.png'),  # 7
    ASSETS('floors/w_i_b_r.png'),  # 8
    ASSETS('floors/w_i_b_l.png'),  # 9
    ASSETS('floors/w_i_t_r.png'),  # 10
    ASSETS('floors/w_i_t_l.png')  # 11

)

SHIP = (
    ASSETS('floors/ship_1.png'),
    ASSETS('floors/ship_2.png'),
    ASSETS('floors/ship_3.png'),
    ASSETS('floors/ship_4.png'),
    ASSETS('floors/ship_5.png'),
)

# WINDOW CONSTANTS:
WIN_WIDTH = 576
WIN_HEIGHT = 576
