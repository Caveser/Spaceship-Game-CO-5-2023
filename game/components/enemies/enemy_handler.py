from game.components.enemies.ship import Ship
from game.components.enemies.alien import Alien
from game.components.enemies.princess import Princess
from game.components.enemies.gatron import Gatron

class EnemyHandler:
    def __init__(self):
        self.enemies = []
        #self.enemies.append(Ship())
        #self.enemies.append(Alien())
        ##self.enemies.append(princess())
        #self.enemies.append(Gatron())

    def update(self, bullet_handler):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(bullet_handler)
            if not enemy.is_alive:
                self.remove_enemy(enemy)
    
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
    
    def add_enemy(self):
        if len(self.enemies) < 2:
            self.enemies.append(Ship()) 
            self.enemies.append(Gatron())
            self.enemies.append(Princess())
            self.enemies.append(Alien())

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)