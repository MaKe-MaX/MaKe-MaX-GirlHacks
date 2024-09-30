import pygame
import os

size1 = (150, 150)
size2 = (200, 200)
grav = 30

# First digit is speed, 0: slowest speed(10), 1: slow(15), 2: fast(20), 3: fastest(35)
# second digit is the direction, 0: down, 1: left, 2: right, 3: up
# color is 100% correlated with direction and x position
screen = None

danceArrows = [0b000111, 0b001001, 0b010001, 0o000010, 0o001011, 0o100010, 0o001000, 0o000010, 0o100000, 0o100010]
cols = [screen.get_width()//8 + n*screen.get_width()//4 for n in range(0,4)]
musicList = []

# DiscoDance minigame controls the entire game
# Blits/draws all objects and the background to the screen
# Manages falling arrows
class DiscoDance:


    class Arrow(pygame.sprite.Sprite):

        def __init__(self, type, pos, speed = grav):
            self.type = type
            # 0o70 = 0b111000
            self.speed = type & 0o70
            self.pos = (cols[type & 0o07], 20)
            super.__init__()
            # 0o7 = 0b111
            self.img = pygame.image.load(f"../assets/arrow{type & 0o7}.png")

        def rhythm_accuracy(self, screen):
            dist = abs(screen.get_height()* (1 - 0.1) - self.pos[1])
            if(dist <= 5):
                return 3
            elif(dist <= 10):
                return 2
            elif(dist <= 15):
                return 1
            return 0


    def __init__(self, scr):
        screen = scr


        self.solid_arrows = [
                [pygame.transform.scale(pygame.image.load(os.path.join('assets/dance', 'arrow0.png')), size1), [cols[0], 20]], 
                [pygame.transform.scale(pygame.image.load(os.path.join('assets/dance', 'arrow1.png')), size1), [cols[1], 20]],
                [pygame.transform.scale(pygame.image.load(os.path.join('assets/dance', 'arrow2.png')), size1), [cols[2], 20]],
                [pygame.transform.scale(pygame.image.load(os.path.join('assets/dance', 'arrow3.png')), size1), [cols[3], 20]]
                      ]
        self.characters = [
                [pygame.transform.scale(pygame.image.load(os.path.join('assets/dance', '1.png')), size2), [cols[0], 200]], 
                [pygame.transform.scale(pygame.image.load(os.path.join('assets/dance', '2.png')), size2), [cols[1], 200]],
                [pygame.transform.scale(pygame.image.load(os.path.join('assets/dance', '3.png')), size2), [cols[2], 200]],
                [pygame.transform.scale(pygame.image.load(os.path.join('assets/dance', '4.png')), size2), [cols[3], 200]]
                    ]
        self.arrows_coming = [[]]
        self.current_arrows = pygame.sprite.Group
        
        
        
        # self.outline_arrows = [
        #         [pygame.transform.scale(pygame.image.load(os.path.join('assets/dance', 'left_arrow.png')), (100,100)), [self.cols[0], 50]], 
        #         [pygame.transform.scale(pygame.image.load(os.path.join('assets/dance', 'up_arrow.png')), (100,100)), [self.cols[1], 50]],
        #         [pygame.transform.scale(pygame.image.load(os.path.join('assets/dance', 'down_arrow.png')), (100,100)), [self.cols[2], 50]],
        #         [pygame.transform.scale(pygame.image.load(os.path.join('assets/dance', 'right_arrow.png')), (100,100)), [self.cols[3], 50]]
        #               ]
        
        pygame.time.delay(500)

    # Add arrows to the Sprite group which gets updated every frame through the run function
    def addToCurrent(self, arrow):
        self.currentArrows.add(arrow)

    # adds each arrow to the correct column list
    def organize_arrows(self, coming_arrows):
        for arrow in coming_arrows:
            direction = arrow & 0o7
            self.arrows_coming[direction].append(arrow)
    
        
            

        

    # What the game should do on a given frame that its running
    def run(self):
        for ar in self.solid_arrows:
            ar[1] = [ar[1][0], ar[1][1]+self.grav]
            self.screen.blit(ar[0], ar[1])


        

            

