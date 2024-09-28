import pygame
import sys
import asyncio
import lib
from lib.game import Game 

async def game_loop():
    while True:
        for event in pygame.event.get():
            Game.ourRenderer.update()
        
        await asyncio.sleep(0)

asyncio.run(game_loop())