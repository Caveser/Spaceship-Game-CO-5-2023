import pygame

from game.utils.constants import SCREEN_HEIGHT, BULLET_ENEMY, BULLET

class Bullet:

    WIDTH = 9
    HEIGHT = 32
    SPEED = 20
    BULLETS = {'player': BULLET, 'enemy': BULLET_ENEMY}


    def __init__(self, spacechip):
        self.image = self.BULLETS[spacechip.type]
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.center = spacechip.rect.center
        self.owner = spacechip.type
        SPEED = 20
    
    def update(self, bullets):
        if self.owner == 'enemy':
            self.rect.y += self.SPEED
            if self.rect.y >= SCREEN_HEIGHT:
                bullets.remove(self)
        if self.owner == 'player':
            self.rect.y -= self.SPEED
            if self.rect.y <= 0:
                bullets.remove(self)
  


    def draw(self, screen):
        screen.blit(self.image, self.rect)