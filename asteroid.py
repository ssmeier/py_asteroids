from circleshape import CircleShape
import pygame
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        return pygame.draw.circle(screen, "white",(self.x,self.y),self.radius, LINE_WIDTH)

    def update(self, dt):
        return (self.velocity * dt)