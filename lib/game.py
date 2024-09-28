import pygame
import sys
import asyncio
import lib
import renderer
import const

class Game:

    ourRenderer = renderer.Renderer()

    def __init__(self, name):
        self.name = name
        self.current_score = 0
        self.high_score = 0
        self.is_game_over = False
    
    def run():
        pass

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

        textObjs = [("GAMEOVER", lib.variables.color["WHITE"], game_over_pos,), 
                    ("Play Again", lib.variables.color["WHITE"], play_again_pos), 
                    ("Return to Arcade", lib.variables.color["WHITE"], return_arcade)]

        Game.ourRenderer.display_text(textObjs)

        Game.ourRenderer.update()

    def reset(self):
        self.current_score = 0
        self.is_game_over = False

    def exit(self):
        pass