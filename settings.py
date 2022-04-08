class Settings:
    """A class to store all settings for example game."""

    def __init__(self):
        """Innitialize game settings"""
        self.screen_width = 1200
        self.screen_height = 1000
        self.bg_color = (42, 181, 202)
        #ship settings
        self.ship_speed_factor = 0.423
        #Bullet settings
        self.bullet_speed_factor = 0.75
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (115, 115, 115)
        #self.bullets_allowed = x
        # Aliens
        self.alien_speed_factor = 1.43
        self.fleet_drop_speed = 1.23
        #fleet direction right = 1, left = -1
        self.fleet_direction = 1