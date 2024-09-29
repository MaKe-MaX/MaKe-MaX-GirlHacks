import pygame
import os
import math

color = {
        "RED": pygame.Color(200, 0, 6),
        "WHITE": pygame.Color(223,224,221),
        "YELLOW": pygame.Color(215, 216, 54),
        "TEAL": pygame.Color(4, 212, 150), 
        "AQUA": pygame.Color(20, 179, 188), 
        "PINK": pygame.Color(255,105,180),
        "GREEN": pygame.Color(6,182,56),
        "BLUE": pygame.Color(6, 222, 242),
        "PURPLE": pygame.Color(156,3,233),
        "ORANGE": pygame.Color(245, 95, 31)
}

dark_color = {
    "BLACK": pygame.Color(0, 0, 0), 
    "GRAY": pygame.Color(100, 100, 100)
}

alpha_color = {
    "TRANSPARENT": pygame.Color(0, 0, 0, 0)
}

FRAME_RATE = 12

default_player_size = (50, 50)

pygame.font.init()

font = {
    
     "GAMEOVER": pygame.font.Font(None, 36), 
     

 }