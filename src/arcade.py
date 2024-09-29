import pygame,os

class Arcade:
    size = 150
    action_dist = 100

    def __init__(self, name, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.pos = pos
        self.off_img =  pygame.transform.scale(pygame.image.load(f'../assets/arcade/{name}_off.png'), (Arcade.size,Arcade.size))
        self.on_imgs = [pygame.transform.scale(pygame.image.load(f'../assets/arcade/{name}_on1.png'), (Arcade.size, Arcade.size))]*6 + [pygame.transform.scale(pygame.image.load(f'../assets/arcade/{name}_on2.png'), (Arcade.size, Arcade.size))]*6
        self.frame = 0
        self.img = self.off_img     # current img

    def update(self, screen, player_x, player_y):
        """
        Runs every tick. Input screen, player_rect
        """
        dist = (self.x - player_x)**2 + (self.y - player_y)**2 
        if dist <= Arcade.action_dist ** 2:
        # if self.img.get_rect().colliderect(player_rect):
            # print("self rect vs player rect:", (self.img.get_rect().x,self.img.get_rect().y), (player_rect.x, player_rect.y))
            self.img = self.on_imgs[self.frame]
            self.frame = (self.frame + 1) % (len(self.on_imgs))      # switches on images back & forth

            # keys = pygame.key.get_pressed()
            # if keys[pygame.K_E]
        else:
            self.img = self.off_img

        screen.blit(self.img, self.pos)

    def custom_collision(rect1, rect2):
        return (
            rect1.x < rect2.x + rect2.width and  # left edge of rect1 is to the left of rect2's right edge
            rect1.x + rect1.width > rect2.x and  # right edge of rect1 is to the right of rect2's left edge
            rect1.y < rect2.y + rect2.height and  # top edge of rect1 is above rect2's bottom edge
            rect1.y + rect1.height > rect2.y  # bottom edge of rect1 is below rect2's top edge
        )
        #