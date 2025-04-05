import pygame
from constants import * 
from player import *

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
    Player.containers = (updatable, drawable)
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

        pygame.display.flip()
    
    
if __name__ == "__main__": 
    main()

