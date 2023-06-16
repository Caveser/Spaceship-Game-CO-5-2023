from game.components.enemies.ship import Ship
from game.components.enemies.alien import Alien
from game.components.enemies.princess import Princess
from game.components.enemies.gatron import Gatron

class EnemyHandler:
    def __init__(self):
        self.enemies = []
        self.number_enemy_destroyed = 0

    def update(self, bullet_handler):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(bullet_handler)
            if enemy.is_destroyed:
                pass
            if not enemy.is_alive:
                self.remove_enemy(enemy)
                self.number_enemy_destroyed += 1
                
    
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
    
    def add_enemy(self):
        if len(self.enemies) < 5:
            self.enemies.append(Ship()) 
            self.enemies.append(Gatron())
            self.enemies.append(Princess())
            self.enemies.append(Alien())

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)
    
    def reset(self):
        self.enemies = []
        self.number_enemy_destroyed = 0