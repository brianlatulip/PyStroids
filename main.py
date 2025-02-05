import pygame
from asteroidfield import AsteroidField
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot

def main():
    #initialize pygame, the game screen, and the game clock
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    #initalize all game object groups to handle game actions
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots= pygame.sprite.Group()
    
    #set game objects' containers to their respective game object groups as needed
    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    Shot.containers = (updateable, drawable, shots)
    
    #initialize player and asteroid field objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    #set variables for tracking game loop state and game loop delta time
    game_over = False
    dt = 0

    #main game loop which updates objects, draws objects, draws the game screen, tracks delta time, sets game to 60fps limit
    while game_over != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updateable.update(dt) #updates items in updateable group
        
        for ast in asteroids: #iterates over all asteroids, checks if they collide with player, ends game if so
            if ast.collisionCheck(player):
                print("GAME OVER")
                game_over = True
                
            for bullet in shots: #iterates over all bullets, checks if they collide with an asteroid, splits or kills asteroid, kills bullet
                if ast.collisionCheck(bullet):
                    ast.split()
                    bullet.kill()

        screen.fill("black") #game screen background

        for drw in drawable: #draws items in drawable group to screen
            drw.draw(screen)

        pygame.display.flip()
        
        dt = clock.tick(60) / 1000 #limit framerate to 60 fps
    
if __name__ == "__main__":
    main()