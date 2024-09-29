import pygame
import random
import time

from game import Game
from entity import Entity
from renderer import Renderer
from const import const

class Tile(Entity):

    def __init__(self, **kwargs):
        super().__init__(kwargs.name, kwargs.pos, kwargs.size, kwargs.color, kwargs.on_click, False)
        self.enabled = False
        self.on_color = kwargs.on_color
        self.off_color = kwargs.off_color
        self.number = kwargs.number

    def enable(self):
        self.enabled = True
        self.clickable = True
        # self.image.fill(self.on_color)

    def disable(self):
        self.enabled = False
        self.clickable = False
        self.image.fill(self.off_color)

    def turn_on(self):
        self.image.fill(self.on_color)

    def turn_off(self):
        self.image.fill(self.off_color)
    

class MemoryMania(Game):
    tile_margin = 15
    tile_size = 100

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        info = pygame.display.Info()
        pos = MemoryMania.__generate_tile_pos( (info.current_w // 2, info.current_h // 2) )
        color_set = set(const.color.values())

        self.tiles = [Tile(name = "Tile_" + i, 
                           pos = pos[i], 
                           size = (MemoryMania.tile_size, MemoryMania.tile_size), 
                           color = const.color["GRAY"],
                           on_click = self.__tile_callback,
                           on_color = color_set.pop(),
                           off_color = const.dark_color["GRAY"],
                           number = i) for i in range(0, 9)]
        self.tile_sleep = 1                                     # in seconds 
        self.chosen_sequence = []       
        self.player_sequence = []   
        self.waiting = False            # if waiting for user_input
        self.need_to_evaluate = False   # if the game has to check whether the user's sequence is correct

    # runs each round when a new tile is added to the sequence
    def run(self):
        if (not self.waiting):
            # show sequence
            chosen_tile_num = random.randint(0, 8)
            self.chosen_sequence.append(chosen_tile_num)

            for n in self.chosen_sequence:
                self.tiles[n].turn_on()
                time.sleep(self.tile_sleep)
                self.tiles[n].turn_off()
                time.sleep(self.tile_sleep / 2)

            # let user click
            for tile in self.tiles:
                tile.enable()

        if (self.need_to_evaluate):
            self.need_to_evaluate = False

            # compare sequences
            for i in range(len(self.chosen_sequence)):
                if (self.player_sequence[i] != self.chosen_sequence[i]):
                    self.is_game_over = True 

    def draw(self):
        Game.ourRenderer.display_entities(self.tiles)

    def __tile_callback(self, tile):
        tile.turn_on()
        if len(self.player_sequence) < len(self.chosen_sequence):
            self.player_sequence.append(tile.number)
        else:
            tile.disable()
            self.need_to_evaluate = True

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