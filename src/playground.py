import pygame
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.entity import Entity
import lib.const as const
from lib.renderer import Renderer

playground_rend = Renderer()

running = True

rect = pygame.Rect(300, 300, 50, 50)
ent = Entity("test_entity", rect)

surface = pygame.Surface([100, 100])
pygame.Surface.fill(surface, pygame.Color(255, 100, 150))

x = 0
y = 0
vel = 10

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.key == pygame.K_w or event.key == pygame.K_UP:
            y -= vel
        if event.key == pygame.K_s or event.key == pygame.K_DOWN:
            y += vel
        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            x -= vel
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            x += vel


    # surface.blit(playground_rend.screen, (10, 10))
    playground_rend.display_text([("Hello world!", const.color['WHITE'], (200, 200))])
    playground_rend.display_sprites([surface], [(50, 50)])
    # playground_rend.display_sprites([ent])
    playground_rend.update()

pygame.quit()