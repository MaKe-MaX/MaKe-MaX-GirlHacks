import pygame
import sys
import asyncio
import lib
import renderer
import variables

class Game:

    ourRenderer = renderer.Renderer()

    def __init__(self, name):
        self.name = name
        self.current_score = 0
        self.high_score = 0
        self.is_game_over = False
    
    def run():
        pass

    async def loop(self):

        # Main game loop
        while True:
            self.run()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    
            
            # # Handle events
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         pygame.quit()
            #         sys.exit()

            Game.ourRenderer.update()
            await asyncio.sleep(0)


    def game_over(self):
        # Display game over screen with options: Play Again and Go Back to Hub
        font = renderer.Font["GAMEOVER"]

        Game.ourRenderer.display_text(["",],"GAMEOVER")

        Game.ourRenderer.screen.fill(variables.colors('BLACK'))

        Game.ourRenderer.update()

    def reset(self):
        self.current_score = 0
        self.is_game_over = False

    def exit(self):
        pass