import sys
import pygame
from settings import Settings

def run_game():
    #init game and create display object
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height ))
    pygame.display.set_caption("Example Game, from the teacher")

    while True:
        #control keyboard snd mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #Background screen fill
        screen.fill(game_settings.bg_color)
        #display the last screen
        pygame.display.flip()

# test game
run_game()