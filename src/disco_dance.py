import pygame
import os

size1 = (150, 150)
size2 = (200, 200)
grav = 30

# First digit is speed, 0: slowest speed(10), 1: slow(15), 2: fast(20), 3: fastest(35)
# second digit is the direction, 0: down, 1: left, 2: right, 3: up
# color is 100% correlated with direction
danceArrows = [0o01, 0o11, 0o21, 0o02, 0o13, 0o42, 0o10, 0o02, 0o40, 0o42]

musicList = []

# DiscoDance minigame
class DiscoDance:


    class Arrow(pygame.sprite.Sprite):

        def __init__(self, type, speed = grav, pos = (0,0)):
            self.type = type
            # 0o70 = 0b111000
            self.speed = type & 0o70
            super.__init__()
            # 0o7 = 0b111
            self.img = pygame.image.load(f"../assets/arrow{type & 0o7}.png")
            
            


    def __init__(self, screen):
        self.screen = screen
        self.cols = [self.screen.get_width()//8 + n*self.screen.get_width()//4 for n in range(0,4)]
        self.solid_arrows = [
                [pygame.transform.scale(pygame.image.load(os.path.join('assets/dance', 'left_arrow.png')), size1), [self.cols[0], 20]], 
                [pygame.transform.scale(pygame.image.load(os.path.join('assets/dance', 'up_arrow.png')), size1), [self.cols[1], 20]],
                [pygame.transform.scale(pygame.image.load(os.path.join('assets/dance', 'down_arrow.png')), size1), [self.cols[2], 20]],
                [pygame.transform.scale(pygame.image.load(os.path.join('assets/dance', 'right_arrow.png')), size1), [self.cols[3], 20]]
                      ]
        self.characters = [
                [pygame.transform.scale(pygame.image.load(os.path.join('assets/dance', '1.png')), size2), [self.cols[0], 200]], 
                [pygame.transform.scale(pygame.image.load(os.path.join('assets/dance', '2.png')), size2), [self.cols[1], 200]],
                [pygame.transform.scale(pygame.image.load(os.path.join('assets/dance', '3.png')), size2), [self.cols[2], 200]],
                [pygame.transform.scale(pygame.image.load(os.path.join('assets/dance', '4.png')), size2), [self.cols[3], 200]]
                    ]
        self.arrowsComing = []
        self.currentArrows = pygame.sprite.Group
        
        
        
        # self.outline_arrows = [
        #         [pygame.transform.scale(pygame.image.load(os.path.join('assets/dance', 'left_arrow.png')), (100,100)), [self.cols[0], 50]], 
        #         [pygame.transform.scale(pygame.image.load(os.path.join('assets/dance', 'up_arrow.png')), (100,100)), [self.cols[1], 50]],
        #         [pygame.transform.scale(pygame.image.load(os.path.join('assets/dance', 'down_arrow.png')), (100,100)), [self.cols[2], 50]],
        #         [pygame.transform.scale(pygame.image.load(os.path.join('assets/dance', 'right_arrow.png')), (100,100)), [self.cols[3], 50]]
        #               ]
        
        pygame.time.delay(500)

    def addToCurrent(self, arrow):
        self.currentArrows.add(arrow)


        


    def run(self):
        for ar in self.solid_arrows:
            ar[1] = [ar[1][0], ar[1][1]+self.grav]
            self.screen.blit(ar[0], ar[1])


        

            

