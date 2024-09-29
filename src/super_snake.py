import pygame
from random import randint
import os, time

# Constants
GRID_SIZE = 16  # 16x16 grid

class SuperSnake:
    def __init__(self, screen):
        self.screen = screen
        # Calculate tile size based on screen size
        self.tile_size = min(screen.get_width(), screen.get_height()) // (GRID_SIZE + 1)
        self.score = 0
        self.snake = Snake(self.tile_size)  # Pass calculated tile size to Snake
        self.food = Food(self.tile_size, screen.get_width(), screen.get_height())
        self.is_game_over = False
    
    def check_food_collision(self):
        if self.snake.head.rect.colliderect(self.food.rect):
            self.snake.extend()
            self.food.randomize_position()
            self.score += 10

    def check_wall_collision(self):
        if (self.snake.head.rect.x < 0 or 
            self.snake.head.rect.x >= self.screen.get_width() or 
            self.snake.head.rect.y < 0 or 
            self.snake.head.rect.y >= self.screen.get_height()):
            self.is_game_over = True
    
    def check_self_collision(self):
        for segment in self.snake.segments[1:]:
            if self.snake.head.rect.colliderect(segment.rect):
                self.is_game_over = True

    def run(self):
        time.sleep(0.1)
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


class Snake:
    def __init__(self, tile_size):
        self.segments = []
        self.tile_size = tile_size
        # Start the snake at the center of the grid
        for position in [(tile_size * 8, tile_size * 8), 
                         (tile_size * 7, tile_size * 8), 
                         (tile_size * 6, tile_size * 8)]:
            new_seg = Segment(pos=position, tile_size=tile_size, heading=0)
            self.segments.append(new_seg)
        self.head = self.segments[0]
        self.head.updateImage(type = "head")
        self.tail = self.segments[-1]
        self.tail.updateImage(type = "tail")

    def extend(self):
        last_segment = self.segments[-1]
        new_seg = Segment(pos=(last_segment.rect.x, last_segment.rect.y), 
                          tile_size=self.tile_size, 
                          heading=last_segment.heading)
        self.segments[-1].updateImage(type = "body")
        self.segments.append(new_seg)
        self.segments[-1].updateImage(type = "tail")

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].rect.topleft = self.segments[seg_num - 1].rect.topleft
            self.segments[seg_num].updateImage(heading = self.segments[seg_num - 1].heading)

        # Move head based on heading
        if self.head.heading == 90:
            self.head.rect.y -= self.tile_size
        elif self.head.heading == 270:
            self.head.rect.y += self.tile_size
        elif self.head.heading == 180:
            self.head.rect.x -= self.tile_size
        elif self.head.heading == 0:
            self.head.rect.x += self.tile_size

    def up(self):
        if self.head.heading != 270:
            self.head.updateImage(heading = 90)

    def down(self):
        if self.head.heading != 90:
            self.head.updateImage(heading = 270)

    def left(self):
        if self.head.heading != 0:
            self.head.updateImage(heading = 180)

    def right(self):
        if self.head.heading != 180:
            self.head.updateImage(heading = 0)

    def clear(self):
        for seg in self.segments:
            del seg
        self.segments.clear()


class Segment(pygame.sprite.Sprite):
    def __init__(self, type="body", pos=(0, 0), heading=0, tile_size = 20):
        super().__init__()
        self.type = type
        self.heading = heading
        self.tile_size = tile_size
        self.img = pygame.transform.scale(pygame.image.load(os.path.join('assets/snake', f'{type}_{heading}.png')), (tile_size, tile_size))
        self.rect = self.img.get_rect(topleft=pos)

    def updateImage(self, type = None, heading = None):
        if type != None:
            self.type = type
        if heading != None:
            self.heading = heading
        self.img = pygame.transform.scale(pygame.image.load(os.path.join('assets/snake', f'{self.type}_{self.heading}.png')), (self.tile_size, self.tile_size))
    
    def update(self, screen):
        screen.blit(self.img, self.rect.topleft)


class Food:
    def __init__(self, tile_size, screen_width, screen_height):
        self.tile_size = tile_size
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.img = pygame.image.load(os.path.join('assets/snake', f'vinyl{randint(1,4)}.png'))
        self.rect = self.img.get_rect()
        self.randomize_position()

    def randomize_position(self):
        self.rect.x = randint(0, (self.screen_width // self.tile_size) - 1) * self.tile_size
        self.rect.y = randint(0, (self.screen_height // self.tile_size) - 1) * self.tile_size

    def update(self, screen):
        screen.blit(self.img, self.rect.topleft)

