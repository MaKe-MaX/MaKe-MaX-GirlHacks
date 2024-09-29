from game import Game

from lib.entity import Entity 



class Arrow(Entity):
        def __init__(self):
            super().__init__()

        def distance(self, arr) -> float:
            return self.rect.y - arr.rect.y

class DiscoDance(Game):

    def __init__(self, cols, arrows, ):
        super.__init__()
        self.cols = [DiscoDance.ourRenderer.window_width()//8 + n*DiscoDance.ourRenderer.window_width()//4 for n in range(0,3)]

    def run(self):


        arrows = [Arrow(name="", pos=(self.cols[0],y), img_path = "../assets/dance/left_arrow.png"  ), ]

        DiscoDance.ourRenderer.display_entities([])
        

            

