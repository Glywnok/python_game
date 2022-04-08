class GameStats():
    """Game statistics"""
    def __init__(self, game_settings):
        """Initialize statistics"""
        self.game_seettings = game_settings
        self.reset_stats()
    def reset_stats(self):
        """Initialize statistics, change during game"""
        self.ships_left = self.game_settings.ship_limit