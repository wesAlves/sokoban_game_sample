import pygame


class Box:
    def __init__(self, type, asset_name, position=(0, 0)):
        self.type = type
        self.asset_name = asset_name
        self.surf = pygame.image.load(self.asset_name).convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
