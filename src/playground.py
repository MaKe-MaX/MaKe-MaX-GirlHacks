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

vel = 10

ent1 = Entity("Ent1", size = (50, 50))
ent2 = Entity("Ent1", size = (50, 50))

ent2.rect.x = 200
ent2.rect.y = 200

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            print("up")
            ent1.rect.y -= vel
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            print("down")
            ent1.rect.y += vel
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            print("left")
            ent1.rect.x -= vel
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            print("right")
            ent1.rect.x += vel



    # surface.blit(playground_rend.screen, (10, 10))
    playground_rend.display_text([("Hello world!", const.color['WHITE'], (200, 200))])
    playground_rend.display_entities([ent1, ent2])
    # playground_rend.display_sprites([ent])
    playground_rend.update()

pygame.quit()