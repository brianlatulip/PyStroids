import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        #set all game object base attributes. Position on game screen, velocity of movement on game screen, and radius (size of game object)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    
    #checks if there is collision between two CircleShape objects (player/asteroid and bullet/asteroid)
    #adds the radius of both objects, calculates the positional distance between objects
    #if the pos distance is <= the radi sum, then there is collision
    def collisionCheck(self, plyr):
        radi_sum = self.radius + plyr.radius
        
        if pygame.math.Vector2.distance_to(self.position, plyr.position) <= radi_sum:
            return True
        else:
            return False