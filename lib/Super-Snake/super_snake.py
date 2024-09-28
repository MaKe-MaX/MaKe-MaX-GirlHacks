import pygame
from random import randint

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
        for pos in [(), (), ()]:
            new_seg = Entity()
            self.segments.append(new_seg)
    
    def extend(self):
        new_seg = Entity()
        new_seg.pos = self.segments[-1].pos
        self.segments.append(new_seg)

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments.goto[new_x,new_y]
            