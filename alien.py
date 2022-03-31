import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Clas fot alien description"""
    def __init__(self, game_settings, screen):
        """Create alien object and specify it's start position"""
        super().__init__()
        self.screen = screen
        self.game_settings = game_settings
        #Load alien image and rect atributes
        self.image = pygame.image.load("image/alien.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #Set alien position
        self.x = float(self.rect.x)
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    def update(self):
        """Update alien position"""
        self.x += self.game_settings.alien_speed_factor
        self.rect.x = self.x
