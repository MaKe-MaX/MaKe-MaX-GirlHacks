import pygame
import os
import lib
import lib.const

MAX_WINDOW_WIDTH, MAX_WINDOW_HEIGHT = 1,1
MIN_WINDOW_WIDTH = 1
MIN_WINDOW_HEIGHT = 1


class Renderer:
    def __init__(self):

        MAX_WINDOW_WIDTH, MAX_WINDOW_HEIGHT = pygame.display.set_mode((0,0), pygame.FULLSCREEN).get_width(), pygame.display.set_mode((0,0), pygame.FULLSCREEN).get_height()
        MIN_WINDOW_WIDTH = 3*MAX_WINDOW_WIDTH//4
        MIN_WINDOW_HEIGHT = 3*MAX_WINDOW_HEIGHT//4

        # Centers video
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        # Initialize pygame
        pygame.init()

        #pygame.display.get_desktop_sizes()

        # Set the dimensions of the window
        self.window_width = MIN_WINDOW_WIDTH
        self.window_height = MIN_WINDOW_HEIGHT

        self.screen = pygame.display.set_mode((self.window_width, self.window_height), pygame.RESIZABLE, pygame.SCALED)

        # Fill the screen with black
        self.screen.fill(lib.const.dark_color["BLACK"])

        pygame.display.set_caption('Disco_World')

    def display_entities(self, entities, events):
        """
        Displays a list of entities\n
        precondition: len(pygame_objs) = len(pos_list)\n
        parameters: List[Entity]\n
        return_type: List[Rect]
        """

        group = pygame.sprite.Group()
        for e in entities:
            e.image.blit(e.img, (e.rect.x + e.rect.width // 2, e.rect.y + e.rect.height // 2))
            group.add(e)
        group.update(events)
        group.draw(self.screen)
    
    def display_background(self, background):
        self.screen.fill(lib.const.dark_color["BLACK"])
        back = pygame.sprite.Group()
        back.add(background)
        back.draw(self.screen)

    def display_text(self, text_color_pos_tuples = [("",lib.const.color["WHITE"],(0, 0))], font = lib.const.font["GAMEOVER"], backdrop = None):
        """ 
        Displays a list of text fonts
        @parameters: (text, color, (x,y) ), font,  backdrop
        @return_type: List[Rect]
        """

        for tcp in text_color_pos_tuples:
            self.screen.blit( font.render(tcp[0], True, tcp[1], backdrop), tcp[2] )

    def update(self):
        """
        Updates the screen size and displays\n
        """
        self.window_width = pygame.display.Info().current_w
        self.window_height = pygame.display.Info().current_h
        # Update the display size
        # if the width or height are too small they are set there minimums
        if self.window_width < MIN_WINDOW_WIDTH:
            self.screen = pygame.display.set_mode((MIN_WINDOW_WIDTH, self.window_height), pygame.RESIZABLE, pygame.SCALED)
            self.window_width = MIN_WINDOW_WIDTH
        if self.window_height < MIN_WINDOW_HEIGHT:
            self.screen = pygame.display.set_mode((self.window_width, MIN_WINDOW_HEIGHT), pygame.RESIZABLE, pygame.SCALED)
            self.window_height = MIN_WINDOW_HEIGHT
        if(self.window_width/self.window_height != MAX_WINDOW_WIDTH/MAX_WINDOW_HEIGHT):
            self.window_height = self.window_width*MAX_WINDOW_HEIGHT/MAX_WINDOW_WIDTH

        self.window_width = pygame.display.Info().current_w
        self.window_height = pygame.display.Info().current_h

        # Update the display
        pygame.display.update()
    
        # Control the frame rate
        pygame.time.Clock().tick(lib.const.FRAME_RATE)
            
        

    
