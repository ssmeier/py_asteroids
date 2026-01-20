import pygame
from constants import *
from logger import log_state
from player import Player


def main():
    game_run = True
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while game_run == True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('black')
        player.draw(screen)
        pygame.display.flip()
        clock_time = game_clock.tick(60)
        dt = clock_time/1000
       

    

if __name__ == "__main__":
    main()
