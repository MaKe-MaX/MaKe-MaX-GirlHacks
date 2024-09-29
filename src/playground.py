import pygame
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.entity import Entity
import lib.const as const
from lib.player import Player 
# from lib.renderer import Renderer

# playground_rend = Renderer()

pygame.init()

screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)

# Fill the screen with black
screen.fill(const.dark_color["BLACK"])

pygame.display.set_caption('Disco_World')

running = True

rect = pygame.Rect(300, 300, 50, 50)
ent = Entity("test_entity", rect)

# surface = pygame.Surface([100, 100])
# pygame.Surface.fill(surface, pygame.Color(255, 100, 150))

vel = 10

bkg = Entity("Background", size = (10000, 10000), color = const.dark_color["BLACK"])
ent1 = Entity("Ent1", pos = (500, 500), size = (200, 200), color = const.alpha_color["TRANSPARENT"], img_path = "assets/player/3.png")
ent2 = Entity("Ent2", size = (50, 50))
player = Player(img_path = "assets/player/3.png", color=const.alpha_color["TRANSPARENT"])

ent1.rect.x = 200
ent1.rect.y = 200

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player.rect.y -= vel
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            player.rect.y += vel
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            player.rect.x -= vel
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            player.rect.x += vel
    
    playas = pygame.sprite.Group()
    playas.add(player)
    playas.draw(screen)

    print(player.rect.x, player.rect.y)

    pygame.display.flip()
    pygame.time.Clock().tick(const.FRAME_RATE)
    # surface.blit(playground_rend.screen, (10, 10))
    # playground_rend.display_background(bkg)
    # playground_rend.display_entities([ent1, ent2], events)
    # playground_rend.display_text([("Hello world!", const.color['WHITE'], (200, 200))])
    # playground_rend.update()

pygame.quit()