import pygame

from game.utils.constants import SCREEN_HEIGHT

class Bullet:

    WIDTH = 9
    HEIGHT = 32
    SPEED = 20
   
    def __init__(self, image, type, center):
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.center = center
        self.is_alive = True
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        SPEED = 20
    
    def update(self, object):
        if self.rect.colliderect(object.rect):
            object.is_alive = False
            self.is_alive = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)