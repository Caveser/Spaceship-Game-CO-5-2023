import pygame

from game.components.enemies.enemy import Enemy
from game.utils.constants import PRINCESS

class Princess(Enemy):
    WIDTH = 50
    HEIGTH =70
    SPEED_X = 4
    SPEED_Y = 1
    INTERVAL = 20

    def __init__(self):
        self.image = PRINCESS
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        super().__init__(self.image)