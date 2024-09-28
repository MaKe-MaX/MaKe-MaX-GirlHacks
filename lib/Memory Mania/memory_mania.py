import pygame
from random import randint

from ..game import Game
from ..entity import Entity

class MemoryMania(Game):
    

    def __init__(self):
        self.tiles = [Entity("Tile_" + i) for i in range(0, 8)]            

    # loop
    def run(self):
        # seq of lit tile nums
        sequence = []

        while not self.is_game_over:
            next_tile_num = randint(0, 8)
            next_tile = self.tiles[next_tile_num]

