import pygame
import os
import lib

class Renderer:

    def __init__(self):

        # Centers video
        os.environ['SDL_VIDEO_CENTERED'] = '1'

        # Initialize pygame
        pygame.init()

        info = pygame.display.Info()

        # Set the dimensions of the window
        self.window_width = info.current_w
        self.window_height = info.current_h
        self.screen = pygame.display.set_mode((self.window_width - 10, self.window_height - 50), pygame.RESIZABLE)

        # Fill the screen with black
        self.screen.fill(lib.const.color["BLACK"])

        pygame.display.set_caption('DiscoWrld')

        # Get keys pressed 
        # keys = pygame.key.get_pressed()
        
        # # Update square position based on arrow key input
        # if keys[pygame.K_LEFT]:
        #     x -= self.speed
        # if keys[pygame.K_RIGHT]:
        #     x += self.speed
        # if keys[pygame.K_UP]:
        #     y -= self.speed
        # if keys[pygame.K_DOWN]:
        #     y += self.speed

    # Displays a sprite 
    # len(pygame_objs) = len(pos_list)
    def display_entities(self, entities):

        group = pygame.sprite.Group()
        for e in entities:
            group.add(e)
        group.draw(self.screen)
    
    def display_screen(self, attributes):
        self.screen.blit()

    # (text, color, (x,y)), font,  backdrop
    def display_text(self, text_color_pos_tuples = [("",lib.const.color["WHITE"],(0, 0))], font = lib.const.font["GAMEOVER"], backdrop = None):
            for tcp in text_color_pos_tuples:
                self.screen.blit( font.render(tcp[0], True, tcp[1], backdrop), tcp[2] )

    def update(self):

        # Update the display
        pygame.display.update()
    
        # Control the frame rate
        pygame.time.Clock().tick(lib.const.frame_rate)
            
        

    
