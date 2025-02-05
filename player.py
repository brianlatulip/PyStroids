import pygame
from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOT_SPEED, PLAYER_SHOT_COOLDOWN, SHOT_RADIUS

#initializes player object as a CircleShape with additional attributes of rotation, timer
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0 #determines rotational direction of player object
        self.timer = 0 #time counter used to determin shot cooldowns
    
    #makes the player object appear as a triangle, though its hitbox is still a CircleShape under the hood
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    #draws the player object on the screen with a "radius" (aka shape) of triangle
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    #handles the rotation of the player object by multiplying the turn speed by delta time(aka frame), then adding to rotation
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    #update player sprite with rotation left/right based on a/d keypress
    #update the player sprite with forward/reverse movement based on w/s keypress
    #increments timer down per frame, timer is used to determine when player can next shoot
    def update(self, dt):
        self.timer -= dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)
    
    #called on W/S keypress, uses a vector set to same rotational direction as player 
    #accelerates that vector by the playerspeed per frame
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    #checks if the cooldown timer is greater than zero, doesnt shoot if true
    #if off cooldown, create a shot object (bullet) set to same position as player
    #set bullet to accelerate from player in direction player faces, at speed of shot_speed constant
    #sets cooldown for shot    
    def shoot(self, dt):
        if self.timer > 0:
            return
        else:
            bullet = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            bullet.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED
            self.timer = PLAYER_SHOT_COOLDOWN
        
        
