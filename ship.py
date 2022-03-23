import pygame

class Ship():
    def __init__(self, screen):
        """Innitialize ship and it's starter position"""
        self.screen = screen
        self.image = pygame.image.load("image/ship.jpg")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw ship at this position"""
        self.screen.blit(self.image, self.rect)
