import pygame
import sys, os
pygame.init()
screen = pygame.display.set_mode((1280, 720))

file_names = [os.path.join('assets/player', f'{i}.png') for i in range(1,5)]

frame = 0
left = [pygame.image.load(file_names[0])]*4 + [pygame.image.load(file_names[1])]*1 + [pygame.image.load(file_names[2])]*4 + [pygame.image.load(file_names[3])]*1
right = [pygame.transform.flip(pygame.image.load(file_names[0]), True, False)]*4 + [pygame.transform.flip(pygame.image.load(file_names[1]), True, False)]*1 + [pygame.transform.flip(pygame.image.load(file_names[2]), True, False)]*4 + [pygame.transform.flip(pygame.image.load(file_names[3]), True, False)]*1
imgList = left

guy = pygame.transform.scale(imgList[frame], (200, 200))

x, y = 500, 500
vel = 5

running = True

while running:
    pygame.time.delay(100)
    events = pygame.event.get()

    for e in events:
        if e.type == pygame.QUIT:
            running = False
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= vel
        frame = (frame + 1) % len(imgList)
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        y += vel
        frame = (frame + 1)%len(imgList)
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        x -= vel
        imgList = left
        frame = (frame + 1) % len(imgList)
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        x += vel
        imgList = right
        frame = (frame + 1) % len(imgList)
    
    guy = pygame.transform.scale(imgList[frame], (200, 200))

    screen.fill(pygame.Color(0, 0, 0))
    screen.blit(guy, (x, y))
    pygame.display.update()