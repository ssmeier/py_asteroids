from circleshape import CircleShape
import pygame
from constants import *
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        return pygame.draw.circle(screen, "white",self.position,self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        # if small destory
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_angle = random.uniform(20,50)
            rock_a_velocity = self.velocity.rotate(new_angle)
            rock_b_velocity = self.velocity.rotate(new_angle*-1)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            # generate new asteroids
            half_a = Asteroid(self.position[0], self.position[1], new_radius)
            half_b = Asteroid(self.position[0], self.position[1], new_radius)
            half_a.velocity = (rock_a_velocity*1.2)
            half_b.velocity = (rock_b_velocity*1.2)