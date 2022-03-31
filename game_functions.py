import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, game_settings, screen, ship, bullets):
    """Check keyboard activities"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        new_bullet  = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)
        #fire_bullet(game_settings, screen, ship,bullets)
    if event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    """Check keyboard activities"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(game_settings, screen, ship, bullets):
    """check keyboard snd mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(game_settings, screen, ship, alien, bullets):
    """Update image on screen and draw new screen, eg frame after frame"""
    # Background screen fill
    screen.fill(game_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        if bullet.rect.bottom <= 0:
            bullets.remove(bullets)
        print(len(bullets))
    # add ship to the screen
    ship.blitme()
    #add alien to the screen
    alien.draw(screen)
    # display the last screen
    pygame.display.flip()


def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(event, game_settings, screen, ship, bullets):
    if len(bullets) < game_settings.bullets_allowed:
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(game_settings, screen, aliens):
    """Create alines fleet"""
    # Create aliend and compute how much aliens can exists at the row
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    available_space_x = game_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    # create first row
    for alien_number in range(number_aliens_x):
        # create aliend and put it into row
        alien = Alien(game_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)
