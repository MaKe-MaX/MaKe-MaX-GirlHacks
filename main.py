import pygame
import sys
import asyncio
from lib.player import Player
from lib.game import Game
# from lib.renderer import Renderer as rend
from lib.entity import Entity
from lib import const as const
import lib.renderer as rend

counter = 0

def hub(render, events):
    """
    Main Hub 
    """
    player = Player(pos = (render.window_width//2, render.window_height//2))
    # snake_machine = Entity("Snake Machine", pos = (20, rend.window_height//2), color = const.alpha_color["TRANSPARENT"], img_path = "assets/arcade/snake_off.png")
    # dance_machine = Entity("Dance Machine", pos = (rend.window_width//2, 20), color = const.alpha_color["TRANSPARENT"], img_path = "assets/arcade/dance_off.png")
    # memory_machine = Entity("Memory Machine", size = (200,200), color = const.alpha_color["TRANSPARENT"], pos = (rend.window_width - 220, rend.window_height//2), img_path = "assets/arcade/memory_off.png")
    render.display_entities([player], events)
    # rend.display_entities([player, snake_machine, dance_machine, memory_machine])
    render.update()

async def main():
    rend = Game.ourRenderer
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        hub(rend, events)
        # Code for hub
        await asyncio.sleep(0)

asyncio.run(main())