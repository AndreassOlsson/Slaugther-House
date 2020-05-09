#Imports
import pygame, sys, time
from time import sleep

#Self-written imports
from settings import Settings
from player import Player
from game_stats import GameStats
from bullet import Bullet
from enemy import Enemy
from button import Button
from scoreboard import Scoreboard


#Overall class to manage game assets and behavior
class SlaugtherHouse:


    #Initialize the game and create game resources
    def __init__(self):

        #Initialize settings (and pygame)
        pygame.init()
        self.settings = Settings()

        #Screen settings
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("SlaugtherHouse")

        #Initialize objects
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.player = Player(self)
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.sb.prep_player()
        self._create_fleet()
        self.play_button = Button(self, "Play")


    #Start the main loop
    def run_game(self):

        while True:
            self._check_events()
            if self.stats.game_active:
                self.player.update()
                self.bullets.update()
                self._update_bullets()
                self._update_enemies()
            self._update_screen()



    #Respond to overall events
    def _check_events(self):
        for event in pygame.event.get():
            if event == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)


    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.stats.reset_stats()
            self.stats.game_active = True
            self.enemies.empty()
            self.bullets.empty()
            self._create_fleet()
            self.player.center_player()
            pygame.mouse.set_visible(False)
            self.settings.initialize_dynamic_settings()
            self.sb.prep_score()
            self.sb.prep_level()


    #Respond to key presses
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = True
            self.player.moving_left = False
            self.settings.player_facing = 1

        elif event.key == pygame.K_LEFT:
            self.player.moving_left = True
            self.player.moving_right = False
            self.settings.player_facing = -1
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE or pygame.K_UP:
            self._fire_bullet()



    #Respond to key realeses
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = False



    #Create a new bullet and add it to the bullets group
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    #Update position of bullets and delete old bullets
    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.y < 0:
                self.bullets.remove(bullet)
        self._check_bullet_enemy_collisions()



    #Respond to collisions between bullets and enemies
    def _check_bullet_enemy_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.enemies, True, True)
        if not self.enemies:
            self.bullets.empty()
            self._create_fleet()
            self.stats.level += 1
            self.sb.prep_level()


        if collisions:
            for enemies in collisions.values():
                self.stats.score += self.settings.enemy_points * len(enemies)
            self.stats.score += self.settings.enemy_points
            self.sb.prep_score()
            self.sb.check_high_score()


    #Create a group of enemies
    def _create_fleet(self):
        enemy = Enemy(self)
        enemy_width, enemy_height = enemy.rect.size
        available_space_x = self.settings.screen_width - (1 * enemy_width)
        number_enemies_x = available_space_x // (2 * enemy_width)

        player_height = self.player.rect.height
        available_space_y = (self.settings.screen_height - (3 * enemy_height) - player_height)
        number_rows = available_space_y // (2 * enemy_height)

        for row_number in range(number_rows):
            for enemy_number in range(number_enemies_x):
                self._create_enemy(enemy_number, row_number)


    #Create rows of enemies
    def _create_enemy(self, enemy_number, row_number):
        enemy = Enemy(self)
        enemy_width, height = enemy.rect.size
        enemy.x = enemy_width + 2 * enemy_width * enemy_number
        enemy.rect.x = enemy.x
        enemy.rect.y = enemy.rect.height + 2 * enemy.rect.height * row_number
        self.enemies.add(enemy)


    #Update position of enemy fleet
    def _update_enemies(self):
        self._check_fleet_edges()
        self._check_enemies_bottom()
        self.enemies.update()

        if pygame.sprite.spritecollideany(self.player, self.enemies):
            self._player_hit()

    #Respond if any enemy have reached an edge
    def _check_fleet_edges(self):
        for enemy in self.enemies.sprites():
            if enemy.check_edges():
                self._change_fleet_direction()
                break


    #Change the fleet direction and drop the entire fleet
    def _change_fleet_direction(self):
        for enemy in self.enemies.sprites():
            enemy.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def _check_enemies_bottom(self):
        screen_rect = self.screen.get_rect()
        for enemy in self.enemies.sprites():
            if enemy.rect.y >= 528:
                self._player_hit()
                break


    #Respond to the player being hit by an enemy
    def _player_hit(self):
        if self.stats.players_left > 0:
            self.stats.players_left -= 1
            self.enemies.empty()
            self.bullets.empty()
            self._create_fleet()
            self.player.center_player()
            self.sb.prep_player()
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)


    #Update images on the screen and flip to the new screen
    def _update_screen(self):
        self.screen.blit(self.settings.bg, (-10,0))
        self.player.blitme()
        self.enemies.draw(self.screen)
        self.sb.show_score()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        if not(self.stats.game_active):
            self.play_button.draw_button()
        pygame.display.flip()


#Make a game instance and run the game
if __name__ == '__main__':
    sh = SlaugtherHouse()
    sh.run_game()
