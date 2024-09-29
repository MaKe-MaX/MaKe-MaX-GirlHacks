import pygame
import random

from ..game import Game
from ..entity import Entity
from ..renderer import Renderer
from ..const import const

class Tile(Entity):

    def __init__(self, **kwargs):
        super().__init__(kwargs.name, kwargs.pos, kwargs.size, kwargs.color, kwargs.on_click, False)
        self.enabled = False
        self.enabled_color = kwargs.enabled_color
        self.disabled_color = kwargs.disabled_color
        self.number = kwargs.number

    def enable(self):
        self.enabled = True
        self.clickable = True
        self.image.fill(self.enabled_color)

    def disable(self):
        self.enabled = False
        self.clickable = False
        self.image.fill(self.disabled_color)

class MemoryMania(Game):
    tile_margin = 10
    tile_size = 50

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        info = pygame.display.Info()
        pos = MemoryMania.__generate_tile_pos( (info.current_w // 2, info.current_h // 2) )
        self.tiles = [Tile(name = "Tile_" + i, 
                           pos = pos[i], 
                           size = (MemoryMania.tile_size, MemoryMania.tile_size), 
                           color = const.color["GRAY"],
                           enabled_color = random.choice(const.color.values)) for i in range(0, 9)]          

    # loop
    def run(self):
        # seq of lit tile nums
        sequence = []

        while not self.is_game_over:
            next_tile_num = random.randint(0, 8)
            next_tile = self.tiles[next_tile_num]

    def draw(self):
        Game.ourRenderer.display_entities(self.tiles)

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