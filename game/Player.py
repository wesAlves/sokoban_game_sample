import pygame

from game.CONSTANTS import WIN_HEIGHT, WIN_WIDTH


class Player:
    def __init__(self, asset_name: str, position: tuple = (0, 0), name: str = ""):
        self.speed = 0
        self.name = name
        self.asset_name = asset_name
        self.last_dmg = None
        self.surf = pygame.image.load(self.asset_name).convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])

    def move(self, level_mtx=None):
        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN] and self.rect.top > 1:
            current_pos = (self.rect.left, self.rect.top)
            self.rect.centery = self.rect.centery + 64

        if key[pygame.K_UP] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery = self.rect.centery - 64

        if key[pygame.K_LEFT] and self.rect.left > 1:
            self.rect.centerx = self.rect.centerx - 64

        if key[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.centerx = self.rect.centerx + 64
