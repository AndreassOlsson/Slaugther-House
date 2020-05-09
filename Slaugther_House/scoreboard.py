

import pygame.font
from pygame.sprite import Group

from player import Player

#Storing score information
class Scoreboard:

    def __init__(self, sh_game):
        self.sh_game = sh_game
        self.screen = sh_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = sh_game.settings
        self.stats = sh_game.stats

        self.text_color = (255,255,255)
        self.score_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_player()


    def prep_score(self):

        score_str = str(self.stats.score)
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.score_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20


    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.players.draw(self.screen)

    def prep_high_score(self):
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.score_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top


    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()


    def prep_level(self):
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.score_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10



    def prep_player(self):
        self.players = Group()
        for player_number in range(self.stats.players_left):
            player = Player(self.sh_game)
            player.rect.x = 10 + player_number * player.rect.width
            player.rect.y = 10
            self.players.add(player)
