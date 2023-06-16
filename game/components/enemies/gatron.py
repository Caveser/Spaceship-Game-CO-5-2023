import pygame
import random
from game.components.enemies.enemy import Enemy
from game.utils.constants import GATRON, SCREEN_WIDTH, SCREEN_HEIGHT

class Gatron(Enemy):
    WIDTH = 80
    HEIGTH = 100
    SPEED_X = 10
    SPEED_Y = 10
    INTERVAL = 20
    SHOOTING_TIME = 50
    UP = 'up'
    DOWN = 'down'
    MOV_Y = [UP, DOWN]
    X_POS = 20

    def __init__(self):
        self.image = GATRON
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        super().__init__(self.image)
        self.mov_y = random.choice(self.MOV_Y)
        self.rect.x = self.X_POS
        self.rect.y = random.randint(1, 5) * 50 + 250
    
    def update(self, bullet_handler):
        if self.rect.x >= SCREEN_WIDTH:
            self.is_alive = False
        self.shooting_time += 1
        self.move()
        self.shoot(bullet_handler)

    def move(self):
        self.rect.x += self.SPEED_X
        if self.mov_y == self.UP: 
            self.rect.y -= self.SPEED_Y
            if self.index > self.INTERVAL or self.rect.y <= 0:
                self.mov_y = self.DOWN
                self.index = 0
        else:
            self.rect.y += self.SPEED_Y
            if self.index > self.INTERVAL or self.rect.y >= SCREEN_HEIGHT - self.rect.height:
                self.mov_y = self.UP
                self.index = 0
        self.index += 1
