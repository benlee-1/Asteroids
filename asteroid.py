import pygame
from circleshape import *

class Asteriod(CircleShape):

    def __init__(self, x, y, radius): 
        super().__init__(x, y, radius)
        
    def draw(self):
        pygame.draw.circle(self.screen, "white", self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt