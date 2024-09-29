import pygame
import const
import time
import random

class Tile:
    size = 150

    def __init__(self, num, pos, color, callback=None):
        self.x = pos[0]
        self.y = pos[1]
        self.num = num
        self.pos = pos
        self.on_color = color
        self.off_color = pygame.Color(100, 100, 100)
        self.enabled = False
        self.image = pygame.Surface((Tile.size, Tile.size))
        self.callback = callback

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False
    
    def turn_on(self):
        self.image.fill(self.on_color)
    
    def turn_off(self):
        self.image.fill(self.off_color)

    def update(self):
        if not self.enabled:
            return
        events = pygame.event.get()

        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN:
                if (e.x > self.x and e.x < self.x + Tile.size and e.y > self.y and e.y < self.y + Tile.size):
                    self.callback(self)

class MemoryMania:
    score = 0
    tile_margin = 10
    tile_size = 50
    Tile.size = tile_size

    def __init__(self, screen):
        pos = MemoryMania.__generate_tile_pos({"x": screen.get_width() // 2, "y": screen.get_height() // 2})
        colors = set(const.color.values())
        self.tiles = [Tile(i, pos[i], colors.pop(), self.__tile_callback) for i in range(0, 9)]
        self.correct_sequence = []
        self.player_sequence = []
        self.waiting = False
        self.need_to_evaluate = False

    def update(self):
        for tile in self.tiles:
            tile.update()
            self.screen.blit(tile.image, (tile.x, tile.y))

        if (not self.waiting):
            # choose next tile
            chosen_tile_num = random.randint(0, 8)
            self.correct_sequence.append(chosen_tile_num)

            # show sequence
            for n in self.correct_sequence:
                self.tiles[n].turn_on()
                time.sleep(self.tile_sleep)
                self.tiles[n].turn_off()
                time.sleep(self.tile_sleep / 2)

            # let user click
            for tile in self.tiles:
                tile.enable()
            
            self.waiting = True

        if (self.need_to_evaluate):
            self.need_to_evaluate = False

            # compare sequences
            for i in range(len(self.correct_sequence)):
                if (self.player_sequence[i] != self.correct_sequence[i]):
                    self.is_game_over = True
                    return
                
            for tile in self.tiles:
                tile.disable()
                tile.turn_off()

            score += len(self.correct_sequence) * 10

    def __tile_callback(self, tile):
        tile.turn_on()
        if len(self.player_sequence) < len(self.correct_sequence):
            self.player_sequence.append(tile.num)
        else:
            tile.disable()
            self.need_to_evaluate = True
            
    @classmethod
    def __generate_tile_pos(cls, center_pos):
        return [
            (center_pos.x - cls.tile_size - cls.tile_margin, center_pos.y - cls.tile_size - cls.tile_margin),
            (center_pos.x, center_pos.y - cls.tile_size - cls.tile_margin),
            (center_pos.x + cls.tile_size + cls.tile_margin, center_pos.y - cls.tile_size - cls.tile_margin),
            (center_pos.x - cls.tile_size - cls.tile_margin, center_pos.y),
            center_pos,
            (center_pos.x + cls.tile_size + cls.tile_margin, center_pos.y),
            (center_pos.x - cls.tile_size - cls.tile_margin, center_pos.y + cls.tile_size + cls.tile_margin),
            (center_pos.x, center_pos.y + cls.tile_size + cls.tile_margin),
            (center_pos.x + cls.tile_size + cls.tile_margin, center_pos.y + cls.tile_size + cls.tile_margin)
        ]