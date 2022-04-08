import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship

from game_stats import GameStats

from alien import Alien
import game_functions as gf

def run_game():
    #init game and create display object
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height ))
    pygame.display.set_caption("Space ship BETA")
    #Game statistics object
    stats = GameStats(game_settings)

    #create ship
    ship = Ship(game_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(game_settings, screen, ship, aliens)

    #Create alien
    alien = Alien(game_settings, screen)

    while True:
        gf.check_events(game_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(game_settings, ship, aliens, bullets, screen )
            gf.update_aliens(game_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(game_settings, screen, ship, aliens, bullets)

# test game
run_game()