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
        self.screen.fill(lib.const.dark_color["BLACK"])

        pygame.display.set_caption('DiscoWrld')

    def display_entities(self, entities) -> list:
        """
        Displays a list of entities\n
        precondition: len(pygame_objs) = len(pos_list)\n
        parameters: List[Entity]\n
        return_type: List[Rect]
        """

        group = pygame.sprite.Group()
        for e in entities:
            group.add(e)
        return group.draw(self.screen)

    def display_text(self, text_color_pos_tuples = [("",lib.const.color["WHITE"],(0, 0))], font = lib.const.font["GAMEOVER"], backdrop = None) -> list:
        """ 
        Displays a list of text fonts
        @parameters: (text, color, (x,y) ), font,  backdrop\n
        @return_type: List[Rect]
        """

        for tcp in text_color_pos_tuples:
            self.screen.blit( font.render(tcp[0], True, tcp[1], backdrop), tcp[2] )

    def update(self, rectList):
        """
        Updates the screen with the displayed types\n
        """
        rectList.update()
        # Update the display
        pygame.display.flip()
    
        # Control the frame rate
        pygame.time.Clock().tick(lib.const.frame_rate)
            
        

    
