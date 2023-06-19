import pygame
from game.utils.constants import BULLET_ENEMY_TYPE, SCREEN_HEIGHT, BULLET_SPACESHIP_TYPE, SHOOT_SPACESHIP, ENEMY_SHOOT
from game.components.bullets.bullet_spaceship import BulletSpaceship
from game.components.bullets.bullet_enemy import BulletEnemy


class BulletHandler:
    def __init__(self):
        self.bullets = []

    def update(self, player, enemies):
        for bullet in self.bullets:        
            if not bullet.is_alive:
                self.remove_bullets(bullet)
            else:
                if bullet.type == BULLET_ENEMY_TYPE:
                    bullet.update(player)
                if bullet.type == BULLET_SPACESHIP_TYPE:
                    for enemy in enemies:
                        bullet.update(enemy)
           
    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)
            
    def add_bullet(self, type, center):
        if type == BULLET_ENEMY_TYPE:
            self.bullets.append(BulletEnemy(center))
            ENEMY_SHOOT.play()
        elif type == BULLET_SPACESHIP_TYPE:
            self.bullets.append(BulletSpaceship(center))
            SHOOT_SPACESHIP.play()

    def remove_bullets(self, bullet):
        self.bullets.remove(bullet)
            
    def reset(self):
        self.bullets = []
            
