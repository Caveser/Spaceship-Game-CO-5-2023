import pygame
import random
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, BULLET_SPACESHIP_TYPE, DEFAULT_TYPE, SHIELD_TYPE, SPEED_TYPE
from game.components.life import Life


class Spaceship:
    X_POS = (SCREEN_WIDTH // 2) - 40
    Y_POS = 500
    SHOOTING_TIME = 5
    SPACESHIP_WIDTH = 40
    SPACESHIP_HEIGHT = 60
    SPEED = 10

    def __init__(self):
        self.image = SPACESHIP
        self.life = Life(0)
        self.image = pygame.transform.scale(self.image, (40, 60))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.is_alive = True
        self.shooting_time = 0
        self.power_type = DEFAULT_TYPE
        self.has_power = False
        self.power_time = 0
        self.actual_speed = self.SPEED    

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
        self.speed_boost()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= self.actual_speed
        else:
            self.rect.x = SCREEN_WIDTH - 40
 
    def move_right(self):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.actual_speed
        else:
            self.rect.x = 0     

    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y -= self.actual_speed

    def move_down(self):
        if self.rect.y < (SCREEN_HEIGHT):
            self.rect.y += self.actual_speed

    def shoot(self, bullet_handler):
        if self.shooting_time % self.SHOOTING_TIME == 0:
            bullet_handler.add_bullet(BULLET_SPACESHIP_TYPE, self.rect.center)

    def enemy_collide(self, enemy_handler):      
        for enemy in enemy_handler.enemies:            
            if self.rect.colliderect(enemy.rect):
                if self.power_type != SHIELD_TYPE:
                    enemy.life.update(enemy)
                    self.life.update(self)
                else:
                    #enemy_handler.number_enemy_destroyed += 1
                    #enemy_handler.remove_enemy(enemy)
                    enemy.life.update(enemy)
    
    def speed_boost(self):
        if self.power_type == SPEED_TYPE:
            self.actual_speed = 20
            


    def reset(self):
        self.rect.x = self.X_POS
        self.y = self.Y_POS
        self.is_alive = True
        self.set_power_image()
        self.power_time = 0
        self.life.increase_lives(4)

    def set_power_image(self, image = SPACESHIP):
        self.image = image
        self.image = pygame.transform.scale(self.image, (40, 60))
    
    def set_default_image(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (40, 60))
