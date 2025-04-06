import sys
import pygame
from constants import * 
from player import *
from asteroid import * 
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    #creating groups 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #assign containers for each class
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable, )
    Shot.containers = (shots, drawable, updatable)

    #create objects
    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    #infinite while loop
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        val = clock.tick()
        dt = val/1000
        screen.fill("black")
        # using updatable and drawable groups
        updatable.update(dt)
        for entity in drawable:
            entity.draw(screen)
        for asteroid in asteroids:
            if player.detect_collision(asteroid):
                print("Game over!")
                sys.exit()    
            for shot in shots:
                if shot.detect_collision(asteroid):
                    asteroid.split()
                    shot.kill()

        pygame.display.flip()
    
    
if __name__ == "__main__": 
    main()

