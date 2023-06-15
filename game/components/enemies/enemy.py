import random
import pygame

from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, BULLET_ENEMY_TYPE
from game.components.bullets.bullet import Bullet
class Enemy:
    X_POST_LIST = [50, 100, 150, 200, 250, 300, 350,400,450,500]
    Y_POS = 20
    SPEED_X = 5
    SPEED_Y = 1
    LEFT = 'left'
    RIGHT = 'right'
    MOV_X = [LEFT, RIGHT]
    INTERVAL = 100
    SHOOTING_TIME = 30

    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POST_LIST)
        self.rect.y = self.Y_POS
        self.mov_x = random.choice(self.MOV_X)
        self.index = 0
        self.is_alive = True
        self.shooting_time = 0
        self.type = 'enemy'

    def update(self, bullet_handler):
        if self.rect.y >= SCREEN_HEIGHT:
            self.is_alive = False
        self.shooting_time += 1
        self.move()
        self.shoot(bullet_handler)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    
    def move(self):
        self.rect.y += self.SPEED_Y
        if self.mov_x == self.LEFT: 
            self.rect.x -= self.SPEED_X
            if self.index > self.INTERVAL or self.rect.x <= 0:
                self.mov_x = self.RIGHT
                self.index = 0
        else:
            self.rect.x += self.SPEED_X
            if self.index > self.INTERVAL or self.rect.x >= SCREEN_WIDTH - self.rect.width:
                self.mov_x = self.LEFT
                self.index = 0
        self.index += 1

    def shoot(self, bullet_handler):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            bullet = Bullet(self)
            bullet_handler.add_bullet(bullet)
            self.shooting_time += random.randint(20, 50)
        

    