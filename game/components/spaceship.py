import pygame
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT

class Spaceship:
    X_POS = (SCREEN_WIDTH // 2) - 40
    Y_POS = 500

    def __init__(self):
        self.image = pygame.transform.scale(SPACESHIP, (40, 60))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.speed = 10
        self.is_alive = True

    def upadte(self, user_input):
        if  user_input[pygame.K_LEFT]:
            self.move_left()
        if user_input[pygame.K_RIGHT]:
            self.move_right()
        if user_input[pygame.K_UP]:
            self.move_up()
        if user_input[pygame.K_DOWN]:
            self.move_down()

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