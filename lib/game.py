import pygame
import sys
import asyncio
from lib.renderer import Renderer
import lib.const as const

class Game:

    ourRenderer = Renderer()

    def __init__(self, name):
        self.name = name
        self.current_score = 0
        self.high_score = 0
        self.is_game_over = False
    
    # Virtual Function
    def run(self):
        pass

    # Main game loop
    def loop(self):

        # Main game loop
        while True:
            self.run()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if (pygame.key.get_pressed() == pygame.K_ESCAPE):
                        self.game_over()
                        break
            Game.ourRenderer.update()
                        


    def game_over(self):

        # Display game over screen with options: Play Again and Go Back to Arcade
        game_over_pos = (self.window_width // 2 - 100, self.window_height // 2 - 100)
        play_again_pos = (self.window_width // 2 - 150, self.window_height // 2)
        return_arcade = (self.window_width // 2 - 150, self.window_height // 2 + 50)

        textObjs = [("GAMEOVER", const.color["WHITE"], game_over_pos,), 
                    ("Play Again", const.color["WHITE"], play_again_pos), 
                    ("Return to Arcade", const.color["WHITE"], return_arcade)]

        Game.ourRenderer.display_text(textObjs)

        Game.ourRenderer.update()

    def reset(self):
        self.current_score = 0
        self.is_game_over = False

    def exit(self):
        pass