import pygame

class Entity:

    def __init__(self, name, pygame_obj, callbacks, clickable=False, collidable=False):
        self.callbacks = callbacks
        self.pygame_obj = pygame_obj
        self.clickable = clickable
        self.collidable = collidable
        self.name = name

    def update(self, events, collide_ent=None):
        x = self.pygame_obj.x
        y = self.pygame_obj.y
        width = self.pygame_obj.width
        height = self.pygame_obj.height

        pos = (x, y)
        size = (width, self.height)

        if not self.clickable:
            return

        for e in events:
            if e.TYPE == pygame.MOUSEBUTTONUP:
                # click
                if (self.clickable and Entity.__is_within((e.x, e.y), pos, size)):
                    self.callbacks["on_click"](self)
                
        # collide
        collide_ent_pos = (collide_ent.oygame_obj.x, collide_ent.pygame_obj.y)
        if (Entity.__is_within(pos, collide_ent_pos, (collide_ent.pygame_obj.width, collide_ent.pygame_obj.height)) 
            or Entity.__is_within((collide_ent_pos, pos, (width, height)))):
            self.callbacks["on_collide"](self, collide_ent)

    # def draw():
    #     pass

    @staticmethod
    def __is_within(self_pos, target_pos, target_size):
        if (self_pos[0] > target_pos[1] and self_pos[0] < target_pos[0] + target_size[0] 
            and self_pos[1] > target_pos[1] and self_pos[1] < target_pos[1] + target_size[1]):
            return True