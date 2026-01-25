import pygame
from constants import *
from logger import log_state
from player import Player
from asteroid import Asteroid


def main():
    game_run = True
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    while game_run == True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('black')
        for sprite in drawable:
            sprite.draw(screen)
        
        clock_time = game_clock.tick(60)
        dt = clock_time/1000
        
        updatable.update(dt)
        pygame.display.flip()


    

if __name__ == "__main__":
    main()
