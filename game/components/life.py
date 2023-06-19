import pygame
from game.utils.constants import SPACESHIP, LIFE_BAR_1, LIFE_BAR_2, LIFE_BAR_3, LIFE_BAR_4, SCREEN_WIDTH

class Life():
    LIFE_BAR = [LIFE_BAR_1, LIFE_BAR_2, LIFE_BAR_3, LIFE_BAR_4]


    def __init__(self, life = 1):
        self.life = life
        

    def update(self, player):
        self.life -= 1
        if self.life <= 0:
             player.is_alive = False
       
    def draw(self, screen):
        self.image = self.LIFE_BAR[self.life - 1]
        self.image = pygame.transform.scale(self.image, (250, 82))
        self.rect = self.image.get_rect()
        screen.blit(self.image, (430,15))

        
    def increase_lives(self, num_lives):
        self.life += num_lives
