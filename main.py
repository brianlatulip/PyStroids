import pygame
from asteroidfield import AsteroidField
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots= pygame.sprite.Group()
    

    
    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    Shot.containers = (updateable, drawable, shots)
    
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
            for bullet in shots:
                if ast.collisionCheck(bullet):
                    ast.split()
                    bullet.kill()

        screen.fill("black")

        for drw in drawable: #draws items in drawable group to screen
            drw.draw(screen)

        pygame.display.flip()
        
        dt = clock.tick(60) / 1000 #limit framerate to 60 fps
    
if __name__ == "__main__":
    main()