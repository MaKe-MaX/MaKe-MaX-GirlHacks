import pygame

size = (150, 150)

# DiscoDance minigame
class DiscoDance:

    def __init__(self, screen):
        self.screen = screen
        self.grav = 50
        self.cols = [self.screen.get_width()//8 + n*self.screen.get_width()//4 for n in range(0,4)]
        self.solid_arrows = [
                [pygame.transform.scale(pygame.image.load("../assets/dance/left_arrow.png"), size), [self.cols[0], 20]], 
                [pygame.transform.scale(pygame.image.load("../assets/dance/up_arrow.png"), size), [self.cols[1], 20]],
                [pygame.transform.scale(pygame.image.load("../assets/dance/down_arrow.png"), size), [self.cols[2], 20]],
                [pygame.transform.scale(pygame.image.load("../assets/dance/right_arrow.png"), size), [self.cols[3], 20]]
                      ]
        
        # self.outline_arrows = [
        #         [pygame.transform.scale(pygame.image.load("../assets/dance/left_arrow.png"), (100,100)), [self.cols[0], 50]], 
        #         [pygame.transform.scale(pygame.image.load("../assets/dance/up_arrow.png"), (100,100)), [self.cols[1], 50]],
        #         [pygame.transform.scale(pygame.image.load("../assets/dance/down_arrow.png"), (100,100)), [self.cols[2], 50]],
        #         [pygame.transform.scale(pygame.image.load("../assets/dance/right_arrow.png"), (100,100)), [self.cols[3], 50]]
        #               ]
        
        pygame.time.delay(500)


    def run(self):
        for ar in self.solid_arrows:
            ar[1] = [ar[1][0], ar[1][1]+self.grav]
            self.screen.blit(ar[0], ar[1])
        


        

            

