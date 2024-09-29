import pygame
import sys
import asyncio
from game_control import run

pygame.mixer.init()
pygame.mixer.music.set_volume(0.25)
sound = pygame.mixer.Sound('../assets/music/track1.mp3')
sound.play()

async def main():
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        run()
        await asyncio.sleep(0)

asyncio.run(main())