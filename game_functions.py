import sys
import pygame
def check_events(ship):
    """check keyboard snd mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.rect.centerx += 1
            if event.key == pygame.K_LEFT:
                ship.rect.centerx -= 1
'''           if event.type == pygame.K_UP:
                ship.rect.bottom -= 1
            if event.type == pygame.K_DOWN:
                ship.rect.bottom += 1       '''

def update_screen(game_settings, screen, ship):
    """Update image on screen and draw new screen, eg frame after frame"""
    # Background screen fill
    screen.fill(game_settings.bg_color)
    # add ship to the screen
    ship.blitme()
    # display the last screen
    pygame.display.flip()
