import sys
import pygame
import time
def check_events(ship):
    """check keyboard snd mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            if event.key == pygame.K_LEFT:
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                ship.moving_left = False

def update_screen(game_settings, screen, ship):
    """Update image on screen and draw new screen, eg frame after frame"""
    # Background screen fill
    screen.fill(game_settings.bg_color)
    # add ship to the screen
    ship.blitme()
    # display the last screen
    pygame.display.flip()
