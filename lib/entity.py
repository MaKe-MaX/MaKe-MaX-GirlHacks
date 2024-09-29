import pygame

import lib.const as const

class Entity(pygame.sprite.Sprite):

    def __init__(self, name="", pos=(0,0), size=(50, 50), color=const.color["WHITE"], on_click = None, 
                 clickable=False, img_path=None):
        super().__init__()
        self.on_click = on_click
        self.clickable = clickable
        self.name = name

        self.image = pygame.Surface(size)
        self.image.fill(color)
        if img_path != None:
            self.img = pygame.image.load(img_path)
            self.img = pygame.transform.scale(self.img, size)

        pygame.draw.rect(self.image, color, pygame.Rect(pos[0], pos[1], size[0], size[1]))

        self.rect = self.image.get_rect()

    def update(self, events):
        # x = self.pygame_obj.x
        # y = self.pygame_obj.y
        # width = self.pygame_obj.width
        # height = self.pygame_obj.height

        # pos = (x, y)
        # size = (width, self.height)

        if not self.clickable:
            return

        for e in events:
            if e.TYPE == pygame.MOUSEBUTTONUP:
                # click
                if (self.rect.collidepoint(e.x, e.y)):
                    self.on_click(self)
                
        # # collide
        # collide_ent_pos = (collide_ent.oygame_obj.x, collide_ent.pygame_obj.y)
        # if (Entity.__is_within(pos, collide_ent_pos, (collide_ent.pygame_obj.width, collide_ent.pygame_obj.height)) 
        #     or Entity.__is_within((collide_ent_pos, pos, (width, height)))):
        #     self.callbacks["on_collide"](self, collide_ent)

    # def draw():
    #     pass

    # @staticmethod
    # def __is_within(self_pos, target_pos, target_size):
    #     if (self_pos[0] > target_pos[1] and self_pos[0] < target_pos[0] + target_size[0] 
    #         and self_pos[1] > target_pos[1] and self_pos[1] < target_pos[1] + target_size[1]):
    #         return True