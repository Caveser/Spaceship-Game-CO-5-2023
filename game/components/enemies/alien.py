import pygame

from game.components.enemies.enemy import Enemy
from game.utils.constants import ALIEN

class Alien(Enemy):
    WIDTH = 40
    HEIGTH =60
    X_POST_LIST = [200, 250, 300, 350,400,450,500,600]
    Y_POS = 20
    SPEED_X = 5
    SPEED_Y = 5
    INTERVAL = 1

    def __init__(self):
        self.image = ALIEN
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        super().__init__(self.image)