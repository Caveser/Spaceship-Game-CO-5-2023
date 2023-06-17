import pygame
import random
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, BULLET_SPACESHIP_TYPE, DEFAULT_TYPE


class Spaceship:
    X_POS = (SCREEN_WIDTH // 2) - 40
    Y_POS = 500
    SPEED = 10
    SHOOTING_TIME = 5
    SPACESHIP_WIDTH = 40
    SPACESHIP_HEIGHT = 60

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (40, 60))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.is_alive = True
        self.shooting_time = 0
        self.power_type = DEFAULT_TYPE
        self.has_power = False
        self.power_time = 0

    def update(self, user_input, bullet_handler, enemy_handler):
        self.shooting_time += 1
        if  user_input[pygame.K_LEFT]:
            self.move_left()
        if user_input[pygame.K_RIGHT]:
            self.move_right()
        if user_input[pygame.K_UP]:
            self.move_up()
        if user_input[pygame.K_DOWN]:
            self.move_down()
        if user_input[pygame.K_SPACE]:
            self.shoot(bullet_handler)
        self.enemy_collide(enemy_handler)
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= self.SPEED
        else:
            self.rect.x = SCREEN_WIDTH - 40
 
    def move_right(self):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.SPEED  
        else:
            self.rect.x = 0     

    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y -= self.SPEED 

    def move_down(self):
        if self.rect.y < (SCREEN_HEIGHT):
            self.rect.y -= -self.SPEED

    def shoot(self, bullet_handler):
        if self.shooting_time % self.SHOOTING_TIME == 0:
            bullet_handler.add_bullet(BULLET_SPACESHIP_TYPE, self.rect.center)

    def enemy_collide(self, enemy_handler):
        for enemy in enemy_handler.enemies:            
            if self.rect.colliderect(enemy.rect):
                enemy.is_alive = False
                self.is_alive = False

    def reset(self):
        self.rect.x = self.X_POS
        self.y = self.Y_POS
        self.is_alive = True

    def set_power_image(self, image):
        self.image = image
        self.image = pygame.transform.scale(self.image, (40, 60))
    
    def set_default_image(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (40, 60))
