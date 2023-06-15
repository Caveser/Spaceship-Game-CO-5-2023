import pygame
import random
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT
from game.components.bullets.bullet import Bullet

class Spaceship:
    X_POS = (SCREEN_WIDTH // 2) - 40
    Y_POS = 500

    def __init__(self, bullet_handler):
        self.image = pygame.transform.scale(SPACESHIP, (40, 60))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.speed = 10
        self.is_alive = True
        self.bullet_handler = bullet_handler
        self.shooting_time = random.randint(30, 50)
        self.type= 'player'

    def update(self, user_input, bullet_handler):
        if  user_input[pygame.K_LEFT]:
            self.move_left()
        if user_input[pygame.K_RIGHT]:
            self.move_right()
        if user_input[pygame.K_UP]:
            self.move_up()
        if user_input[pygame.K_DOWN]:
            self.move_down()
        if user_input[pygame.K_SPACE]:
            self.shoot(self.bullet_handler)
        if self.rect.y >= SCREEN_HEIGHT:
            Spaceship.remove(self)




    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))


    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= self.speed
        elif self.rect.left <= 0:
            self.rect.x = (SCREEN_WIDTH)

    def move_right(self):
        if self.rect.right < (SCREEN_WIDTH):
            self.rect.x += self.speed
        elif self.rect.right >= (SCREEN_WIDTH):
            self.rect.x = 0        

    def move_up(self):
        if self.rect.y > (SCREEN_HEIGHT)//2:
            self.rect.y -= self.speed  

    def move_down(self):
        if self.rect.y < (SCREEN_HEIGHT):
            self.rect.y -= -self.speed

    def shoot(self, bullet_handler):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            bullet = Bullet(self)
            bullet_handler.add_bullet(bullet)
            self.shooting_time += random.randint(20, 50)