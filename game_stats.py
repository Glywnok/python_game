class GameStats():
    """Game statistics"""
    def __init__(self, game_settings):
        """Initialize statistics"""
        self.game_seettings = game_settings
        self.game_active = True
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics, change during game"""
        self.ships_left = self.game_seettings.ship_limit