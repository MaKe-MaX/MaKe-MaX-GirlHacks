import pygame
import sys
import asyncio
from lib.player import Player
from lib.game import Game
# from lib.renderer import Renderer as rend
from lib.entity import Entity



def hub():
    """
    Main Hub 
    """
    print("hubbing")
    rend = Game.ourRenderer
    player = Player(pos = (rend.window_width//2, rend.window_height//2))
    snake_machine = Entity(pos = (20, rend.window_height//2), img_path = "assets/arcade/snake_off.png")
    dance_machine = Entity(pos = (rend.window_width//2, 20), img_path = "assets/arcade/dance_off.png")
    memory_machine = Entity(pos = (rend.window_width//2 - 20, rend.window_height//2), img_path = "assets/arcade/memory_off.png")
    rend.update(rend.display_entities([player, snake_machine, dance_machine, memory_machine]))
    #rend.update(rend.display_text([], ))

async def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Code for hub
        hub()
        await asyncio.sleep(0)

asyncio.run(main())