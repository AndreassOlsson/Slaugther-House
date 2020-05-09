
import pygame, random

class Settings:

    def __init__(self):

        #Screen Settings
        self.screen_width = 1100
        self.screen_height = 655
        self.bg = pygame.transform.scale(pygame.image.load('./Images/Scenes/BgS.jpg'), (1120, 655))
        self.game_over = False
        self.score = 0

        #Player settings
        self.player_speed = 3
        self.player_limit = 3

        #Bullet Settings
        self.bullet_speed = 4
        self.bullet_width = 12
        self.bullet_height = 4
        self.bullet_color = (255, 255, 0)
        self.bullets_allowed = 5
        self.bullet_disappear = True
        self.bullet_damage = 1


        #Enemies settings
        self.enemy_speed = 1
        self.fleet_drop_speed = 20
        self.fleet_direction = 1

        #Speedup
        self.speedup_scale = 2
        self.initialize_dynamic_settings()

        #Scoring
        self.enemy_points = 100
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        self.player_speed = float(1.5)
        self.bullet_speed = 3
        self.enemy_speed = 1
        self.fleet_direction = 1


    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.enemy_speed *= self.speedup_scale
        print(self.enemy_points)
