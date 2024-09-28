import pygame
from random import randint
import const

from ..game import Game
from ..entity import Entity

class SuperSnake(Game):

    def __init__(self):
        self.tiles = [Entity("Tile_" + i) for i in range(0, 9)]            

    # loop
    def run(self):

        while not self.is_game_over:
            next_tile_num = randint(0, 8)
            next_tile = self.tiles[next_tile_num]

class Snake:
    def __init__(self):
        self.segments = []
        self.create()
        self.head = self.segments [0]

    def create(self):
        for pos in [(10,100), (120,100), (140,100)]:
            new_seg = Entity(pos = pos, size = (20,20), color = const.color['GREEN'])
            self.segments.append(new_seg)
    
    def extend(self):
        new_seg = Entity(pos = self.segments[-1].pos, size = (20,20), color = const.color['GREEN'])
        self.segments.append(new_seg)

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            self.segments.pos = self.segments[seg_num-1].pos
            