class Settings:
    """A class to store all settings for example game."""

    def __init__(self):
        """Innitialize game settings"""
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (42, 181, 202)
        #ship settings
        self.ship_speed_factor = 0.245
        #Bullet settings
        self.bullet_speed_factor = 0.23
        self.bullet_width = 4
        self.bullet_height = 7
        self.bullet_color = (115, 115, 115)
        #self.bullets_allowed = x