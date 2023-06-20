import pygame

class Bullet:

    WIDTH = 9
    HEIGHT = 32
    SPEED = 20

    def __init__(self, image, type, center):
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.is_alive = True
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
       
    
    def update(self, object):
        if self.rect.colliderect(object.rect):
            object.life.update(object)
            self.is_alive = False
           

    def draw(self, screen):
        screen.blit(self.image, self.rect.center)