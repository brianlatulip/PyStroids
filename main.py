import pygame
from asteroidfield import AsteroidField
from constants import *
from player import Player
from asteroid import Asteroid

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    
    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    
    game_over = False
    dt = 0

    while game_over != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updateable.update(dt) #updates items in updateable group
        for ast in asteroids:
            if ast.collisionCheck(player):
                print("GAME OVER")
                game_over = True

        screen.fill("black")

        for drw in drawable: #draws items in drawable group to screen
            drw.draw(screen)

        pygame.display.flip()
        
        dt = clock.tick(60) / 1000 #limit framerate to 60 fps
    
if __name__ == "__main__":
    main()