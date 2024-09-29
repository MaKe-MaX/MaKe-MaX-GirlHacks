import pygame
from random import randint
import const

from game import Game
from entity import Entity

class SuperSnake(Game):

    def __init__(self):
        pass          

    # loop
    def run(self):
        snake = Snake()
        snake.move()

    def check_food_collision(self):
        if self.snake.head.rect.colliderect(self.food.rect):
            self.snake.extend()
            self.food.rect.x = randint(0, 29) * self.snake.tile_size
            self.food.rect.y = randint(0, 29) * self.snake.tile_size
            self.current_score += 10 

    def check_wall_collision(self):
        if (self.snake.head.rect.x < 0 or 
            self.snake.head.rect.x >= Game.ourRenderer.window_width or 
            self.snake.head.rect.y < 0 or 
            self.snake.head.rect.y >= Game.ourRenderer.window_height):
            self.is_game_over = True
    
    def check_self_collision(self):
        for segment in self.snake.segments[1:]:
            if self.snake.head.rect.colliderect(segment.rect):
                self.is_game_over = True



class Snake:
    def __init__(self):
        self.segments = []
        self.create()
        self.head = self.segments [0]
        self.heading = 0
        self.tile_size = 20

    def create(self):
        for position in [(100,100), (100-self.tile_size,100), (100-2*self.tile_size,100)]:
            new_seg = Entity(pos = position, size = (self.tile_size,self.tile_size), color = const.color['GREEN'])
            self.segments.append(new_seg)
    
    def extend(self):
        last_segment = self.segments[-1]
        new_seg = Entity(
            pos=(last_segment.rect.x, last_segment.rect.y),
            size=(self.tile_size, self.tile_size),
            color=const.color['GREEN']
        )
        self.segments.append(new_seg)

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            self.segments.pos = self.segments[seg_num-1].pos
    
    def up(self):
        if self.heading != 270:
            self.heading = 90

    def down(self):
        if self.heading != 90:
            self.heading = 270

    def left(self):
        if self.heading != 0:
            self.heading = 180

    def right(self):
        if self.heading != 180:
            self.heading = 0

    def clear(self):
        for seg in self.segments:
            seg.kill()
        self.segments.clear()

class Food(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)