import pygame
from random import randint

from ..game import Game
from ..entity import Entity

class Tile(Entity):

    def __init__(self, name):
        super().__init__(name)
        pass

class MemoryMania(Game):
    tile_margin = 10
    tile_size = 50

    def __init__(self):
        info = pygame.display.Info()
        self.tiles = [Tile("Tile_" + i, pygame.Rect(info.current_w, info.current_h)) for i in range(0, 9)]            

    # loop
    def run(self):
        # seq of lit tile nums
        sequence = []

        while not self.is_game_over:
            next_tile_num = randint(0, 8)
            next_tile = self.tiles[next_tile_num]

    @classmethod
    def __generate_tile_pos(cls, center_pos):
        return [
            (center_pos.x - cls.tile_size - cls.tile_margin, center_pos.y - cls.tile_size - cls.tile_margin),
            (center_pos.x, center_pos.y - cls.tile_size - cls.tile_margin),
            (center_pos.x + cls.tile_size + cls.tile_margin, center_pos.y - cls.tile_size - cls.tile_margin),
            (center_pos.x - cls.tile_size - cls.tile_margin, center_pos.y),
            center_pos,
            (center_pos.x + cls.tile_size + cls.tile_margin, center_pos.y),
            (center_pos.x - cls.tile_size - cls.tile_margin, center_pos.y + cls.tile_size + cls.tile_margin),
            (center_pos.x, center_pos.y + cls.tile_size + cls.tile_margin),
            (center_pos.x + cls.tile_size + cls.tile_margin, center_pos.y + cls.tile_size + cls.tile_margin)
        ]