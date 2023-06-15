import pygame

from game.components.items.item import Item
from game.utils.constants import ITEM_SPEED


class ItemSpeed(Item):
    WIDTH = 20
    HEIGTH = 40

    def __init__(self):
        self.image = ITEM_SPEED
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        super().__init__(self.image)
    
       



    

    
  
  
          