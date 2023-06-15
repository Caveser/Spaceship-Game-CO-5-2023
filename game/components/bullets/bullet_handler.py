import pygame
from game.utils.constants import BULLET_ENEMY_TYPE, SCREEN_HEIGHT
from game.components.bullets.bullet import Bullet



class BulletHandler:
    def __init__(self):
        self.enemy_bullets = []
        self.player_bullets = []

    def update(self, game):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)
            if bullet.rect.colliderect(game.player) and bullet.owner == 'enemy':
                self.enemy_bullets.remove(bullet)
                game.playing = False
                pygame.time.delay(1000)
                break

        for bullet in self.player_bullets:
            bullet.update(self.player_bullets)
            for enemy in game.enemy_handler.enemies:
                if bullet.rect.colliderect(enemy) and bullet.owner == 'player':
                    self.player_bullets.remove(bullet)
                    game.enemy_handler.enemies.remove(enemy)
                    break
        
    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
        for bullet in self.player_bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == 'enemy' and len(self.enemy_bullets)<5:
            self.enemy_bullets.append(bullet)
        if bullet.owner == 'player' and len(self.player_bullets)<5:
            self.player_bullets.append(bullet)
            
