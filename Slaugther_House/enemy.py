
import pygame, random
from pygame.sprite import Sprite

#A class to represent a single enemy
class Enemy(Sprite):



    #Initialize the enemy and set its starting position
    def __init__(self, sh_game):
        super().__init__()
        self.screen = sh_game.screen
        self.settings = sh_game.settings

        #Load the alien image and set its rect attribute
        self.image = pygame.transform.scale(pygame.image.load('./Images/Enemies/Enemy.Sprite/bat.png'), (64,64))
        self.rect = self.image.get_rect()


        #Start position of enemy
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the enemy´s exact position
        self.x = float(self.rect.x)

        #Moving statements
        self.moveLeft = False
        self.moveRight = False
        self.walkCount = random.choice([0, 50, 100, 150, 200, 250, 300])


    #Check if an enemy has hit the edge of the screen
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    #Move enemy to the right
    def update(self):
        self.x += (self.settings.enemy_speed * self.settings.fleet_direction)
        self.rect.x = self.x
