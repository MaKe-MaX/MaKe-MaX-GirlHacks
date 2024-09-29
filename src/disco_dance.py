import pygame


class DiscoDance:

    def __init__(self, screen):
        self.screen = screen
        self.grav = 20
        self.cols = [self.screen.get_width()//8 + n*self.screen.get_width()//4 for n in range(0,3)]
        self.arrows = [
                (pygame.image.load("../assets/dance/left_arrow.png"), (self.cols[0], 50)), 
                (pygame.image.load("../assets/dance/up_arrow.png"), (self.cols[1], 50)),
                (pygame.image.load("../assets/dance/down_arrow.png"), (self.cols[2], 50)),
                (pygame.image.load("../assets/dance/right_arrow.png"), (self.cols[3], 50))
                      ]


    def run(self):
        for ar in self.arrows:
            self.screen.blit(ar[0], ar[1])
        


        

            

