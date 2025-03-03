import pygame
import os
import time
from lib.entity import Entity
# from lib.renderer import Renderer
from lib.game import Game
import lib.const as const

class Player(Entity):
    def __init__(self, name="", size=(50, 50), color=const.color["WHITE"], img_path=None):
        super().__init__(name=name, size=size, color=color, img_path=img_path)
        file_names = [os.path.join('assets/player', f'{i}.png') for i in range(1,5)]
        self.left = [pygame.transform.flip(pygame.image.load(file_names[0]), False, False)]*4 + [pygame.transform.flip(pygame.image.load(file_names[1]), False, False)]*1 + [pygame.transform.flip(pygame.image.load(file_names[2]), False, False)]*4 + [pygame.transform.flip(pygame.image.load(file_names[3]), False, False)]*1
        self.right = [pygame.transform.flip(pygame.image.load(file_names[0]), True, False)]*4 + [pygame.transform.flip(pygame.image.load(file_names[1]), True, False)]*1 + [pygame.transform.flip(pygame.image.load(file_names[2]), True, False)]*4 + [pygame.transform.flip(pygame.image.load(file_names[3]), True, False)]*1
        self.frame = 0

        self.imgList = self.left
        self.img = self.imgList[self.frame]

        self.img_pos = [0,0]
        self.movementY = [False, False]
        self.movementX = [False, False]
        self.velocity = 10


    def update(self, events):
        renderer = Game.ourRenderer
        self.frame = (self.frame + 1) % (len(self.imgList))
        self.img = self.imgList[self.frame]
        self.img = pygame.transform.scale(self.img, (200, 200))
        self.img_pos[0] = max(0, min(renderer.window_height - 40, self.img_pos[0] + (self.movementX[1] - self.movementX[0])*8))
        self.img_pos[1] = max(0, min(renderer.window_width - 420, self.img_pos[1] + (self.movementY[1] - self.movementY[0])*8))

        # print("player update")

        # self.rect.x = self.img_pos[0]
        # self.rect.y = self.img_pos[1]
        # print("self.img_pos", self.img_pos[0], self.img_pos[1])

        for event in events:
            keys = pygame.key.get_pressed()
            print("keys", keys)

            if keys[pygame.K_UP] or keys[pygame.K_w]:
                print("moved up")
                self.rect.y -= self.velocity
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                self.rect.y += self.velocity
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                self.rect.x -= self.velocity
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                self.rect.x += self.velocity

            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_w or event.key == pygame.K_UP:
            #         self.movementY[0] = True
            #         print("moved up")
            #     if event.key == pygame.K_s or event.key == pygame.K_DOWN:
            #         self.movementY[1] = True
            #     if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            #         self.movementX[0] = True
            #         self.imgList = self.left
            #     if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            #         self.movementX[1] = True
            #         self.imgList = self.right

            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_w or event.key == pygame.K_UP:
            #         self.movementY[0] = False
            #         print("moved up stopped")
            #     if event.key == pygame.K_s or event.key == pygame.K_DOWN:
            #         self.movementY[1] = False
            #     if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            #         self.movementX[0] = False
            #     if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            #         self.movementX[1] = False
            if self.movementX[0] == False and self.movementX[1] == False and self.movementY[0] == False and self.movementY[1] == False:
                time.sleep(0.1)