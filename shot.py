import pygame
from constants import *
from circleshape import CircleShape

#defines Shot class which is a sub-class of CircleShape 
class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
    
    #draws bullet which is a circle size of shot_radius at player position    
    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, SHOT_RADIUS)
    
    #updates the bullet by adding velocity * delta-time to its position each update    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    