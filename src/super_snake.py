import pygame
from random import randint
import const
import random

class SuperSnake:
    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.snake = Snake()  # Add snake initialization
        self.food = Food(self.snake.tile_size, self.screen.get_width(), self.screen.get_height())
        self.is_game_over = False
    
    def check_food_collision(self):
        if self.snake.head.rect.colliderect(self.food.rect):
            self.snake.extend()
            self.food.randomize_position()
            self.score += 10

    def check_wall_collision(self):
        if (self.snake.head.rect.x < 0 or self.snake.head.rect.x >= self.screen.get_width() or self.snake.head.rect.y < 0 or self.snake.head.rect.y >= self.screen.get_height()):
            self.is_game_over = True
    
    def check_self_collision(self):
        for segment in self.snake.segments[1:]:
            if self.snake.head.rect.colliderect(segment.rect):
                self.is_game_over = True

    def run(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_w] or keys[pygame.K_UP]:
                    self.snake.up()
                if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                    self.snake.down()
                if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                    self.snake.left()
                if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                    self.snake.right()
        
        self.snake.move()
        
        # Render snake
        for seg in self.snake.segments:
            seg.update(self.screen)
        
        # Render food
        self.food.update(self.screen)
        
        # Check for collisions
        self.check_food_collision()
        self.check_wall_collision()
        self.check_self_collision()

        pygame.display.update()

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

class Segment(pygame.sprite.Sprite):
    def __init__(self, type = "body", pos = (0,0), heading = 0):
        self.x = pos[0]
        self.y = pos[1]
        self.pos = pos
        self.enabled = False
        self.heading = heading
        self.type = type
        self.img = pygame.image.load(img_path = f"../assets/snake/{type}_{heading}.png")
        self.rect = self.img.get_rect()

    def update(self, screen):
        screen.blit(self.img, self.pos)

class Food:
    def __init__(self, tile_size, screen_width, screen_height):
        self.tile_size = tile_size
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.img = pygame.image.load(img_path = f"../assets/snake/vinyl{random.randint(1,4)}.png")
        self.rect = self.img.get_rect()
        self.randomize_position()

    def randomize_position(self):
        self.rect.x = randint(0, (self.screen_width // self.tile_size) - 1) * self.tile_size
        self.rect.y = randint(0, (self.screen_height // self.tile_size) - 1) * self.tile_size

    def update(self, screen):
        screen.blit(self.img, self.rect.topleft)


