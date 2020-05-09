

#Track statitics for SLAKTHUSET
class GameStats:


    def __init__(self, sh_game):
        self.settings = sh_game.settings
        self.game_active = False
        self.reset_stats()
        self.high_score = 0

    def reset_stats(self):
        self.players_left = self.settings.player_limit
        self.score = 0
        self.level = 1
