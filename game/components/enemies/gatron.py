import pygame

from game.components.enemies.enemy import Enemy
from game.utils.constants import GATRON

class Gatron(Enemy):
    WIDTH = 80
    HEIGTH = 100
    SPEED_X = 1
    SPEED_Y = 1
    INTERVAL = 200

    def __init__(self):
        self.image = GATRON
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        super().__init__(self.image)