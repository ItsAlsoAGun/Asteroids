# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# import everything from the constants module
# into the current file
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill('black')
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()
        
        #limits the fremarate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()