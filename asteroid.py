import pygame
import random
from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape

#defines Asteroid class which is a sub-class of CircleShape but has additional functionality
#Asteroid is used in asteroidfield to randomly spawn asteroids
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    #draws an asteroid object on the screen based on values in initializer
    def draw(self, screen):
        pygame.draw.circle(screen, "aqua", self.position, self.radius, 2)
    
    #updates position of asteroid by multiplying the velocity by delta time, then adding that to position
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    #asteroid destruction logic checks what size asteroid is (large, medium, small)
    #if asteroid is small type, asteroid is kill, but if its large or medium it splits into 2 asteroids of next size down
    #split vectors are a rotated at a random angle between 30-50, then two asteroids are created in direction of two new split vectors 
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else: 
            rand_angle = random.uniform(30, 50)
            
            new_vect_1 = self.velocity.rotate(rand_angle)
            new_vect_2 = self.velocity.rotate(-rand_angle)
            
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            new_ast_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_ast_1.velocity = new_vect_1 * 1.2
            
            new_ast_2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_ast_2.velocity = new_vect_2 * 1.2