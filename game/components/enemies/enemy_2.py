import random
from game.utils.constants import SCREEN_WIDTH
from game.components.enemies.enemy import Enemy

class Enemy_2(Enemy):
    def __init__(self):
        X_POST_LIST = [50, 100, 150, 200, 250, 300, 350,400,450,500]
        Y_POS = 20
        SPEED_X = 5
        SPEED_Y = 1
        LEFT = 'left'
        RIGHT = 'right'
        MOV_X = [LEFT, RIGHT]
        INTERVAL = 100
