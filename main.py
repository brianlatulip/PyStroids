import pygame
from constants import *

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_over = False
    
    clock = pygame.time.Clock()
    dt = 0
    
    while game_over != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        
        dt = clock.tick(60) / 1000
    
if __name__ == "__main__":
    main()