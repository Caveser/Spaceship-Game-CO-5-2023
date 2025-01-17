import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import BULLET

class BulletPlayer(Bullet):
    WIDTH = 9
    HEIGHT = 32
    SPEED = 15

    def __init__(self, center):
        self.image = BULLET
        self.image = pygame.transform.scale(self.WIDTH, self.HEIGHT)
        super().__init__(self.image, center)


    def reset(self):
        self.bullets = []
