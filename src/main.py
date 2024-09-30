import pygame, sys, os, asyncio, time

from arcade import Arcade
from disco_dance import DiscoDance
from memory_mania import MemoryMania
from super_snake import SuperSnake
import const

pygame.init()
screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)

pygame.mixer.init()
pygame.mixer.music.set_volume(0.25)
sound = pygame.mixer.Sound(os.path.join('assets/music', 'track1.mp3'))
sound.play()

# ------------------ Game Over ----------------- #
def game_over_screen(score, events):        # returns whether to restart
    events = pygame.event.get()
    screen.fill(pygame.Color(0, 0, 0))
    text_color_pos_tuples = [("GAME OVER",const.color["WHITE"],(screen.get_width() // 2, 100)), 
                             (f"You got {score} points",const.color["WHITE"],(screen.get_width() // 2, screen.get_height() // 2))] 
                            #  ("Press `r` to restart or `h` to return to the hub",const.color["WHITE"],(screen.get_width() // 2, screen.get_height() - 100))]
    font = const.font["GAMEOVER"]
    backdrop = None
    for tcp in text_color_pos_tuples:
        screen.blit( font.render(tcp[0], False, tcp[1], backdrop), tcp[2] )
        pygame.display.update()
        time.sleep(1.5)
    # while True:
    #     for event in events:
    #         if event.type == pygame.KEYDOWN:
    #             keys = pygame.key.get_pressed()
    #             if keys[pygame.K_r]:
    #                 return True
    #             if keys[pygame.K_h]:
    #                 sound = pygame.mixer.Sound(os.path.join('assets/music', 'track1.mp3') )
    #                 pygame.mixer.music.set_volume(0.5)
    #                 sound.play()
    #                 return False

    sound = pygame.mixer.Sound(os.path.join('assets/music', 'track1.mp3') )
    pygame.mixer.music.set_volume(0.5)
    sound.play()

def quit_management(events):
    for event in events:
        if event.type == pygame.QUIT:
            pygame.mixer.init()
            sound = pygame.mixer.Sound(os.path.join('assets/music', 'track1.mp3') )
            pygame.mixer.music.set_volume(0.5)
            sound.play()
            pygame.quit()
            sys.exit()
            return True
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_m]:
                pygame.mixer.init()
                sound = pygame.mixer.Sound(os.path.join('assets/music', 'track1.mp3') )
                pygame.mixer.music.set_volume(0.5)
                sound.play()
                pygame.quit()
                sys.exit()
                return True

# --------------- Main Game Loop  -------------- #
async def main():
    
    # ------- player image & walking frames ------- #
    file_names = [os.path.join('assets/player', f'{i}.png') for i in range(1,5)]
    frame = 0

    floor_list = [pygame.image.load(os.path.join('assets/arcade', 'disco_floor1.png'))]*6  + [pygame.image.load(os.path.join('assets/arcade', 'disco_floor2.png'))]*6
    left = [pygame.image.load(file_names[0])]*5 + [pygame.image.load(file_names[1])]*1 + [pygame.image.load(file_names[2])]*5 + [pygame.image.load(file_names[3])]*1
    right = [pygame.transform.flip(pygame.image.load(file_names[0]), True, False)]*5 + [pygame.transform.flip(pygame.image.load(file_names[1]), True, False)]*1 + [pygame.transform.flip(pygame.image.load(file_names[2]), True, False)]*5 + [pygame.transform.flip(pygame.image.load(file_names[3]), True, False)]*1
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
        
        screen.blit(pygame.transform.scale(floor_list[frame], (screen.get_width(), screen.get_height())), (0,0))
        rect.x = x
        rect.y = y
        
        snake_result = snakeArcade.update(screen, x, y)
        dance_result = danceArcade.update(screen, x, y)
        memory_result = memoryArcade.update(screen, x, y)
        
        if snake_result:
            pygame.mixer.stop()
            game_over = False
            try_again = True
            quit = False
            while try_again:
                inst = SuperSnake(screen)
                while not game_over:
                    if quit_management(events):
                        quit = True
                        break

                    screen.fill(pygame.Color(134,0, 56))
                    inst.run()
                    clock.tick(12)
                    game_over = inst.is_game_over
                    # game_over_screen(inst.score, events)
                    pygame.display.update()
                print("Game possibly over for snake")
                if not quit and not game_over_screen(inst.score, events):
                    pygame.display.update()
                    try_again = False
        elif dance_result:
            pygame.mixer.stop()
            game_over = False
            try_again = True
            quit = False
            while try_again:
                inst = DiscoDance(screen)
                while not game_over:
                    if quit_management(events):
                        quit = True
                        break

                    # here is code of the game
                    screen.fill(pygame.Color(0, 0, 255))
                    inst.run()
                    clock.tick(12)
                    pygame.display.update()
                if not quit and not game_over_screen(0, events):
                    try_again = False
        elif memory_result:
            pygame.mixer.stop()
            game_over = False
            try_again = True
            quit = False
            
            while try_again:
                mem_game = MemoryMania(screen)
                while not game_over:
                    events = pygame.event.get()
                    if quit_management(events):
                        quit = True
                        break

                    # here is code of the game
                    
                    screen.fill(pygame.Color(255, 0, 255))
                    mem_game.update(events)
                    game_over = mem_game.is_game_over
                    clock.tick(12)
                    pygame.display.update()
                if not quit and not game_over_screen(mem_game.score, events):
                    try_again = False

        # Known Bug: track x & y for each image obj to make arcades turn off if far away
        #print("x, y vs rect.x, rect.y:", (x, y), (guy.get_rect().centerx, guy.get_rect().centery))
        screen.blit(guy, (x, y))
        clock.tick(12)
        pygame.display.update()

        await asyncio.sleep(0)

asyncio.run(main())