import pygame
import os
import lib
import lib.variables

class Renderer:

    def __init__(self, window_width, window_height, screen):
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

        # Fill the screen with black
        self.screen.fill(lib.color["BLACK"])

        pygame.display.set_caption('DiscoWrld')

        """# Get keys pressed 
            keys = pygame.key.get_pressed()
            
            # Update square position based on arrow key input
            if keys[pygame.K_LEFT]:
                x -= self.speed
            if keys[pygame.K_RIGHT]:
                x += self.speed
            if keys[pygame.K_UP]:
                y -= self.speed
            if keys[pygame.K_DOWN]:
                y += self.speed"""

    # Displays a sprite 
    def display_entities(entities):
        group = pygame.sprite.Group()
        for e in entities:
            if(isinstance(e.pygameObj, pygame.sprite)):
                group.add(e.pygameObj)
            else:
                e.pygameObj.blit()
        group.draw();
    
    def display_screen(self, attributes):
        self.screen.blit();
    
    def display_text(self, textPosTuple, screentype):


        if(screentype == lib.variables.ScreenType["GAMEOVER"]):
            self.screen.fill(lib.BLACK)
            font = lib.variables.Font["GAMEOVER"]

            for tp in textPosTuple():
                self.screen.blit(font.render(tp[0], True, lib.misc.colors('WHITE')), tp[1])

           # renderTexts = [font.render(t[0], True, lib.misc.colors('WHITE')) for t in textPosTuple]
            #renderPos = [pos for pos in textPosTuple]
            
            for i in range()
            self.screen.blit(renderTexts[0], (self.window_width // 2 - 100, self.window_height // 2 - 100))
            self.screen.blit(renderTexts[1], (self.window_width // 2 - 150, self.window_height // 2))
            self.screen.blit(renderTexts[2], (self.window_width // 2 - 150, self.window_height // 2 + 50))

    def update():

        # Update the display
        pygame.display.update()
    
        # Control the frame rate
        pygame.time.Clock().tick(12)
            
        

    
