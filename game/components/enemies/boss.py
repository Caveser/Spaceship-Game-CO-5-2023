import pygame
import random
from game.components.enemies.enemy import Enemy
from game.utils.constants import BOSS, SCREEN_WIDTH, SCREEN_HEIGHT
from game.components.life import Life

class Boss(Enemy):
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
        self.image = BOSS
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        super().__init__(self.image)
        self.mov_y = random.choice(self.MOV_Y)
        self.rect.x = self.X_POS
        self.rect.y = random.randint(1, 5) * 50 + 250
        self.is_alive = False
        self.type = 'boss'
        self.life = Life(0)
    
    def update(self, bullet_handler):
        if self.rect.x >= SCREEN_WIDTH:
            self.rect.x = self.X_POS
        self.shooting_time += 1
        if self.is_alive:
            self.move()
            self.shoot(bullet_handler)
        else:
            self.rect.x = 2000
            self.rect.y = 4000

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

    def reset(self):
        self.life.increase_lives(10)
        self.is_alive = True
        self.rect.x = self.X_POS
        self.rect.y = random.randint(1, 5) * 50 + 250
