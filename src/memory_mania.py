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

    def update(self, events):
        if not self.enabled:
            print("not enabled")
            return
        events = pygame.event.get()

        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN:
                if (e.x > self.x and e.x < self.x + Tile.size and e.y > self.y and e.y < self.y + Tile.size):
                    self.callback(self)

class MemoryMania:
    tile_margin = 15
    tile_size = 100
    Tile.size = tile_size
    tile_sleep = 0.5 # in s

    def __init__(self, screen):
        pos = MemoryMania.__generate_tile_pos((screen.get_width() // 2, screen.get_height() // 2))
        
        chosen_color = random.choice(list(const.color.values()))
        colors = [chosen_color]

        for _ in range(8):
            while chosen_color in colors:
                chosen_color = random.choice(list(const.color.values()))
            colors.append(chosen_color)
        
        # print(colors)
        
        self.screen = screen
        self.score = 0
        self.tiles = [Tile(i, pos[i], colors[i], self.__tile_callback) for i in range(0, 9)]
        self.correct_sequence = []
        self.player_sequence = []
        self.waiting = False
        self.need_to_evaluate = False
        self.is_game_over = False

    def update(self, events):
        for tile in self.tiles:
            tile.update(events)
            self.screen.blit(tile.image, (tile.x, tile.y))

        if (self.need_to_evaluate):
            # print("need to evaluate")
            self.need_to_evaluate = False

            # print("pl vs co seq", self.player_sequence, self.correct_sequence)
            # compare sequences
            for i in range(len(self.correct_sequence)):
                if (self.player_sequence[i] != self.correct_sequence[i]):
                    # print("wrong")
                    self.is_game_over = True
                    return
                
            for tile in self.tiles:
                tile.disable()
                tile.turn_off()
            
            self.player_sequence = []
        elif (not self.waiting):
            # print("not waiting, so choosing sequence")
            # choose next tile
            for tile in self.tiles:
                tile.disable()
                tile.turn_off()

            chosen_tile_num = random.randint(0, 8)
            self.correct_sequence.append(chosen_tile_num)

            # print("correct seq:", self.correct_sequence)
            # print("player seq:", self.player_sequence)

            # show sequence
            for n in self.correct_sequence:
                self.tiles[n].turn_on()
                # print("turned on", n)
                time.sleep(MemoryMania.tile_sleep)
                self.tiles[n].turn_off()
                # print("turned off", n)
                time.sleep(MemoryMania.tile_sleep / 2)

            # let user click
            for tile in self.tiles:
                tile.enable()
            
            self.waiting = True
            self.score += len(self.correct_sequence) * 10

    def __tile_callback(self, tile):
        print("clicked")
        tile.turn_on()
        print('NUMBER', tile.num)
        # print("pl vs co seq", len(self.player_sequence), len(self.correct_sequence))
        if len(self.player_sequence) < len(self.correct_sequence):
            # print("after clicking", tile.num, "click more tiles", self.player_sequence)
            self.player_sequence.append(tile.num)
            # print("pl2 vs co seq2", len(self.player_sequence), len(self.correct_sequence))
        
        if len(self.player_sequence) >= len(self.correct_sequence):
            tile.disable()
            self.need_to_evaluate = True
            self.waiting = False
            
    @classmethod
    def __generate_tile_pos(cls, center_pos):
        return [
            (center_pos[0] - cls.tile_size - cls.tile_margin, center_pos[1] - cls.tile_size - cls.tile_margin),
            (center_pos[0], center_pos[1] - cls.tile_size - cls.tile_margin),
            (center_pos[0] + cls.tile_size + cls.tile_margin, center_pos[1] - cls.tile_size - cls.tile_margin),
            (center_pos[0] - cls.tile_size - cls.tile_margin, center_pos[1]),
            center_pos,
            (center_pos[0] + cls.tile_size + cls.tile_margin, center_pos[1]),
            (center_pos[0] - cls.tile_size - cls.tile_margin, center_pos[1] + cls.tile_size + cls.tile_margin),
            (center_pos[0], center_pos[1] + cls.tile_size + cls.tile_margin),
            (center_pos[0] + cls.tile_size + cls.tile_margin, center_pos[1] + cls.tile_size + cls.tile_margin)
        ]