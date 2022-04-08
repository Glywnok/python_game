class Settings:
    """A class to store all settings for example game."""

    def __init__(self):
        """Innitialize game settings"""
        self.screen_width = 1200
        self.screen_height = 1000
        self.bg_color = (42, 181, 202)
        #ship settings
        self.ship_speed_factor = 1.23
        self.ship_limit = 3
        #Bullet settings
        self.bullet_speed_factor = 1.7
        self.bullet_width = 2
        self.bullet_height = 10
        self.bullet_color = (115, 115, 115)
        self.bullets_allowed = 2
        # Aliens
        self.alien_speed_factor = 2.3
        self.fleet_drop_speed = 3
        #fleet direction right = 1, left = -1
        self.fleet_direction = 1