import pygame
color = {
        "BLACK": (0, 0, 0), 
        "RED": (200, 0, 6),
        "BLUE": (0, 0, 255),
        "WHITE": (223,224,221),
        "YELLOW": (215, 216, 54),
        "TEAL": (4, 212, 150), 
        "AQUA": (20, 179, 188), 
        "PINK": (255,105,180),
        "GREEN":(6,182,56),
        "BLUE": (6, 222, 242),
        "PURPLE": (156,3,233),
        "ORANGE": (245, 95, 31)
}

frame_rate = 12

default_player_size = (50, 50)



Font = {
    
     "GAMEOVER": pygame.font.Font(None, 36)

 }

ScreenType = {
    "TITLE": 0,
    "HUB": 1,
    "SUPERSNAKE": 2,
    "DISCODANCE": 3,
    "MEMORYMANIA": 4,
    "GAMEOVER": 5
}