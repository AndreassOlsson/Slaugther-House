
import pygame
from pygame.sprite import Sprite


#Class to manage bullets in the game
class Bullet(Sprite):


    def __init__(self, sh_game):

        #Create a bullet object at the players current position
        super().__init__()
        self.screen = sh_game.screen
        self.settings = sh_game.settings
        self.image = pygame.transform.scale(pygame.image.load('./Images/Attacks/laser_red.png'), (9,15))


        #Create a bullet rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = (sh_game.player.rect.x + 33, sh_game.player.rect.y + 16)

        #Store the bullet's positional value as a decimal value
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


    #Move the bullet on the screen
    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    #Draw the bullet on the screen
    def draw_bullet(self):
        self.screen.blit(self.image, (self.x, self.y))
