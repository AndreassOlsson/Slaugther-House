
import pygame
from pygame.sprite import Sprite

walkRight = [pygame.image.load('./Images/Players/Man.Sprite/R1.png'),pygame.image.load('./Images/Players/Man.Sprite/R2.png'),pygame.image.load('./Images/Players/Man.Sprite/R3.png'),pygame.image.load('./Images/Players/Man.Sprite/R4.png'),pygame.image.load('./Images/Players/Man.Sprite/R5.png'),pygame.image.load('./Images/Players/Man.Sprite/R6.png'),pygame.image.load('./Images/Players/Man.Sprite/R7.png'),pygame.image.load('./Images/Players/Man.Sprite/R8.png'),pygame.image.load('./Images/Players/Man.Sprite/R9.png')]
walkLeft = [pygame.image.load('./Images/Players/Man.Sprite/L1.png'),pygame.image.load('./Images/Players/Man.Sprite/L2.png'),pygame.image.load('./Images/Players/Man.Sprite/L3.png'),pygame.image.load('./Images/Players/Man.Sprite/L4.png'),pygame.image.load('./Images/Players/Man.Sprite/L5.png'),pygame.image.load('./Images/Players/Man.Sprite/L6.png'),pygame.image.load('./Images/Players/Man.Sprite/L7.png'),pygame.image.load('./Images/Players/Man.Sprite/L8.png'),pygame.image.load('./Images/Players/Man.Sprite/L9.png'),]

#Class to manage the player
class Player(Sprite):

    #Initialize the player and its starting position
    def __init__(self, sh_game):

        #Define the screen
        super().__init__()
        self.screen = sh_game.screen
        self.settings = sh_game.settings
        self.stats = sh_game.stats
        self.screen_rect = sh_game.screen.get_rect()

        #Load the player image and get its rectangle
        self.image = pygame.transform.scale(pygame.image.load('./Images/Players/Man.Sprite/standing.png'), (64,64))
        self.rect = self.image.get_rect()

        #Starting position of player
        self.rect.midbottom = (560, 588)

        #Decimal value for the player´s position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #Player movement
        self.moving_right = False
        self.moving_left = False
        self.standing = False
        self.walkCount = 0


    #Update the players position based on the movement flag
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right - 4:
            self.rect.x += self.settings.player_speed * 1.5
        elif self.moving_left and self.rect.left > 4:
            self.rect.x -= self.settings.player_speed


    #Draw the player at its current position
    def blitme(self):
        if self.walkCount + 1 > 27:
            self.walkCount = 0
        if self.moving_right and self.rect.right < self.screen_rect.right - 4:
            self.screen.blit(walkRight[self.walkCount//3], self.rect)
            self.walkCount += 1
        elif self.moving_left and self.rect.left > 4:
            self.screen.blit(walkLeft[self.walkCount//3], self.rect)
            self.walkCount += 1
        else:
            self.screen.blit(self.image, self.rect)
            self.standing = True


    def center_player(self):
        self.rect.midbottom = (560, 588)
        self.x = float(self.rect.x)
