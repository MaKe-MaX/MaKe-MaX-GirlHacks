import pygame
import sys
import asyncio

from src.game import Game

mainGame = Game()
mainGame.start()
    
asyncio.run(mainGame.main())