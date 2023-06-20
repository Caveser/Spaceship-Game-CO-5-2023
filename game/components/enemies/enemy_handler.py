import pygame
import random

from game.components.enemies.ship import Ship
from game.components.enemies.alien import Alien
from game.components.enemies.princess import Princess
from game.components.enemies.boss import Boss

class EnemyHandler:
    def __init__(self):
        self.enemies = [Boss()]
        self.number_enemy_destroyed = 0
        self.when_appears_enemies = random.randint(3000, 4000)
        self.when_appears_boss = random.randint(20000, 21000)
        self.when_appears_alien = random.randint(5000, 6000)
        self.when_appears_princess = random.randint(10000, 11000)
        self.time = 0 

    def update(self, bullet_handler):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(bullet_handler)
            if enemy.is_destroyed:
                pass
            if not enemy.is_alive and enemy.type != 'boss':
                self.remove_enemy(enemy)
                self.number_enemy_destroyed += 1
                
                
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
    
    def add_enemy(self):
        current_time = pygame.time.get_ticks() - self.time
        difficulty = (current_time // 40000) + 1
        if current_time >= self.when_appears_enemies:
            for x in range(difficulty):
                self.enemies.append(Ship())            
                self.enemies.append(Ship()) 
            self.when_appears_enemies += random.randint(6000, 10000) 
        if current_time >= self.when_appears_boss and not(self.enemies[0].is_alive):
            self.enemies[0].reset()
            self.when_appears_boss += random.randint(25000, 30000)
        if current_time >= self.when_appears_alien:
            for x in range(difficulty):
                self.enemies.append(Alien())
                self.enemies.append(Alien())
                self.enemies.append(Alien())
                self.enemies.append(Alien())
            self.when_appears_alien += random.randint(15000, 16000)
        if current_time >= self.when_appears_princess:
            for x in range(difficulty):
                self.enemies.append(Princess())
                self.enemies.append(Princess())
                self.enemies.append(Princess())
            self.when_appears_princess += random.randint(10000, 20000)


    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)
    
    def reset(self):
        self.enemies = [Boss()]
        self.number_enemy_destroyed = 0
        self.time = pygame.time.get_ticks()
        self.when_appears_enemies = random.randint(3000, 4000)
        self.when_appears_boss = random.randint(20000, 21000)
        self.when_appears_alien = random.randint(5000, 6000)
        self.when_appears_princess = random.randint(10000, 11000)