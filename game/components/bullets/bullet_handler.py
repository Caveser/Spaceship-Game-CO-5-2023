import pygame
from game.utils.constants import BULLET_ENEMY_TYPE, SCREEN_HEIGHT
from game.components.bullets.bullet_spaceship import BulletSpaceship
from game.components.bullets.bullet_enemy import BulletEnemy

class BulletHandler:
    def __init__(self):
        self.bullets = []

    def update(self, player, enemies):
        for bullet in self.bullets:         
            if not bullet.is_alive:
                self.bullets.remove(bullet)
            else:
                if bullet.type == BULLET_ENEMY_TYPE:
                    bullet.update(player)
                else:
                    for enemy in enemies:
                        bullet.update(enemy)
        
    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)

    def add_bullet(self, type, center):
        if type == BULLET_ENEMY_TYPE:
            self.bullets.append(BulletEnemy(center))
        else:
            self.bullets.append(BulletSpaceship(center))
            
