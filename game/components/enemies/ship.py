import pygame

from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_1
from game.utils.constants import ENEMY_2
from game.utils.constants import ENEMY_3
from game.utils.constants import ENEMY_4

class Ship(Enemy):
    WIDTH = 40
    HEIGTH = 60

    def __init__(self):
        self.image = ENEMY_1
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        super().__init__(self.image)
    
class Ship_2(Enemy):
    WIDTH = 40
    HEIGTH =60
    X_POST_LIST = [200, 250, 300, 350,400,450,500,600]
    Y_POS = 20
    SPEED_X = 1
    SPEED_Y = 1
    INTERVAL = 5

    def __init__(self):
        self.image = ENEMY_2
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        super().__init__(self.image)

class Ship_3(Enemy):
    WIDTH = 40
    HEIGTH =60
    SPEED_X = 4
    SPEED_Y = 1

    def __init__(self):
        self.image = ENEMY_3
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        super().__init__(self.image)

class Ship_4(Enemy):
    WIDTH = 80
    HEIGTH = 100
    SPEED_X = 1
    SPEED_Y = 1
    INTERVAL = 200

    def __init__(self):
        self.image = ENEMY_4
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        super().__init__(self.image)