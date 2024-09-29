import pygame
from random import randint
import const

class SuperSnake:

    def __init__(self, screen):
        self.screen = screen          

    # loop
    def run(self):
        snake = Snake()
        for seg in snake.segments:
            seg.update(self.screen)
        snake.move()

    """
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
    """


class Snake:
    def __init__(self):
        self.segments = []
        for position in [(100,100), (100-self.tile_size,100), (100-2*self.tile_size,100)]:
            new_seg = Segment(pos = position, heading = 0)
            self.segments.append(new_seg)
        self.head = self.segments[0]
        self.head.type = "head"
        self.tail = self.segments[-1]
        self.tail.type = "tail"
        self.tile_size = 20

    def extend(self):
        new_seg = Segment(pos = (self.segments[-1].x, self.segments[-1].y), heading = self.segments[-1])
        self.segments[-1].type = "body"
        self.segments.append(new_seg)
        self.segments[-1].type = "tail"

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            self.segments.pos = self.segments[seg_num-1].pos
            self.segments.heading = self.segments[seg_num-1].pos
    
    def up(self):
        if self.head.heading != 270:
            self.head.heading = 90

    def down(self):
        if self.head.heading != 90:
            self.head.heading = 270

    def left(self):
        if self.head.heading != 0:
            self.head.heading = 180

    def right(self):
        if self.head.heading != 180:
            self.head.heading = 0

    def clear(self):
        for seg in self.segments:
            del seg
        self.segments.clear()

class Segment:
    def __init__(self, type = "body", pos = (0,0), heading = 0):
        self.x = pos[0]
        self.y = pos[1]
        self.pos = pos
        self.enabled = False
        self.heading = heading
        self.type = type
        self.img = pygame.image.load(img_path = f"../assets/snake/{type}_{heading}.png")

    def update(self, screen):
        screen.blit(self.img, self.pos)

