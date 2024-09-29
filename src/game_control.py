import pygame, sys, os
from arcade import Arcade
from disco_dance import DiscoDance

pygame.init()
screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)

# ------------------ Game Over ----------------- #
def game_over_screen(score):        # returns whether to restart
    screen.fill(pygame.Color(255, 0, 0))
    print("Game over!")
    print("Press `r` to restart or `h` to return to the hub")

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_r]:
                    return True
                if keys[pygame.K_h]:
                    return False

def quit_management():
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            return True
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_m]:
                return True

# --------------- Main Game Loop  -------------- #
def run():

    # ------- player image & walking frames ------- #
    file_names = [f'../assets/player/{i}.png' for i in range(1,5)]
    frame = 0
    left = [pygame.image.load(file_names[0])]*5 + [pygame.image.load(file_names[1])]*1 + [pygame.image.load(file_names[2])]*5 + [pygame.image.load(file_names[3])]*1
    right = [pygame.transform.flip(pygame.image.load(file_names[0]), True, False)]*4 + [pygame.transform.flip(pygame.image.load(file_names[1]), True, False)]*1 + [pygame.transform.flip(pygame.image.load(file_names[2]), True, False)]*4 + [pygame.transform.flip(pygame.image.load(file_names[3]), True, False)]*1
    imgList = left
    guy = pygame.transform.scale(imgList[frame], (200, 200))
    rect = guy.get_rect()

    x, y, vel = 500, 500, 12

    # ----------------- Arcade Files -------------- #
    snakeArcade = Arcade("snake", (0, screen.get_height()//2))
    danceArcade = Arcade("dance", (screen.get_width()//2 - Arcade.size//2, 10))
    memoryArcade = Arcade("memory", (screen.get_width() - Arcade.size, screen.get_height()//2))

    running = True
    clock = pygame.time.Clock()
    
    while running:
        #pygame.time.delay(100)
        events = pygame.event.get()

        for e in events:
            if e.type == pygame.QUIT:
                running = False
            
        keys = pygame.key.get_pressed()

        is_up = keys[pygame.K_w] or keys[pygame.K_UP]
        is_down = keys[pygame.K_s] or keys[pygame.K_DOWN]
        is_left = keys[pygame.K_a] or keys[pygame.K_LEFT]
        is_right = keys[pygame.K_d] or keys[pygame.K_RIGHT]

        # ----- normalize velocity for diagonal movement ----- #
        if is_up and is_left:
            y -= vel/(2 ** 0.5)
            x -= vel/(2 ** 0.5)
        elif is_up and is_right:
            y -= vel/(2 ** 0.5)
            x += vel/(2 ** 0.5)
        elif is_down and is_left:
            y += vel/(2 ** 0.5)
            x -= vel/(2 ** 0.5)
        elif is_down and is_right:
            y += vel/(2 ** 0.5)
            x += vel/(2 ** 0.5)
        elif is_up:
            y -= vel
        elif is_down:
            y += vel
        elif is_left:
            x -= vel
            imgList = left
        elif is_right:
            x += vel
            imgList = right

        # always dancing
        frame = (frame + 1) % len(imgList)
        
        guy = pygame.transform.scale(imgList[frame], (200, 200))
        
        screen.fill(pygame.Color(0, 0, 0))
        rect.x = x
        rect.y = y
        
        snake_result = snakeArcade.update(screen, x, y)
        dance_result = danceArcade.update(screen, x, y)
        memory_result = memoryArcade.update(screen, x, y)
        
        if snake_result:
            game_over = False
            try_again = True
            quit = False
            while try_again:
                while not game_over:
                    if quit_management():
                        quit = True
                        break

                    # here is code of the game
                    
                    screen.fill(pygame.Color(255, 0, 255))
                    clock.tick(12)
                    pygame.display.update()
                if not quit and not game_over_screen(0):
                    try_again = False
        elif dance_result:
            game_over = False
            try_again = True
            quit = False
            inst = DiscoDance(screen)
            while try_again:
                while not game_over:
                    if quit_management():
                        quit = True
                        break

                    # here is code of the game
                    inst.run()
                    screen.fill(pygame.Color(0, 0, 255))
                    clock.tick(12)
                    pygame.display.update()
                if not quit and not game_over_screen(0):
                    try_again = False
        elif memory_result:
            game_over = False
            try_again = True
            quit = False
            while try_again:
                while not game_over:
                    if quit_management():
                        quit = True
                        break

                    # here is code of the game
                    
                    screen.fill(pygame.Color(255, 0, 255))
                    clock.tick(12)
                    pygame.display.update()
                if not quit and not game_over_screen(0):
                    try_again = False


        # Known Bug: track x & y for each image obj to make arcades turn off if far away
        #print("x, y vs rect.x, rect.y:", (x, y), (guy.get_rect().centerx, guy.get_rect().centery))
        screen.blit(guy, (x, y))
        clock.tick(12)
        pygame.display.update()
