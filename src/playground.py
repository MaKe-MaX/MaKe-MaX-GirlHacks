import pygame
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import lib.variables as vars

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

running = True
stuff = vars.color["PINK"]

rect = pygame.Rect(300, 300, 50, 50)

lst = [i for i in range(0, 8)]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.rect(screen, (255, 0, 255), rect)
    pygame.display.update()
    clock.tick(vars.frame_rate)

pygame.quit()