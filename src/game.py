import pygame
import sys
import asyncio
import os


class Game:

    def __init__(self, BLACK = (0, 0, 0) , RED = (255, 0, 0), square_size = 0, x = 0, y = 0, speed = 0, window_width = 0, window_height = 0):
        pass

    def start(self):

        os.environ['SDL_VIDEO_CENTERED'] = 1

        # Initialize pygame
        pygame.init()

        info = pygame.display.Info()

        # Set the dimensions of the window
        self.window_width = info.current_w
        self.window_height = info.current_h
        self.screen = pygame.display.set_mode((self.window_width - 10, self.window_height - 50), pygame.RESIZABLE)

        pygame.display.set_caption('Move the Red Square')

        # Define the square
        self.square_size = 50
        self.x, self.y = (self.window_width // 2, self.window_height // 2)  # Start at the center

        # Set the movement speed
        self.speed = 5

    async def main(self):

        # Main game loop
        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
            # Get keys pressed 
            keys = pygame.key.get_pressed()
            
            # Update square position based on arrow key input
            if keys[pygame.K_LEFT]:
                x -= self.speed
            if keys[pygame.K_RIGHT]:
                x += self.speed
            if keys[pygame.K_UP]:
                y -= self.speed
            if keys[pygame.K_DOWN]:
                y += self.speed
    
            # Prevent the square from moving off the screen
            x = max(0, min(self.window_width - self.square_size, x))
            y = max(0, min(self.window_height - self.square_size, y))
    
            # Fill the screen with black
            self.screen.fill(Game.BLACK)
    
            # Draw the red square
            pygame.draw.rect(Game.screen, self.RED, (x, y, self.square_size, self.square_size))
    
            # Update the display
            pygame.display.update()
    
            # Control the frame rate
            pygame.time.Clock().tick(60)
            await asyncio.sleep(0)
