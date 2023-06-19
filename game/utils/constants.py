import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = 'default'
SHIELD_TYPE = 'shield'
SPEED_TYPE = 'speed'

SPACESHIP_SPEED = pygame.image.load(os.path.join(IMG_DIR, 'Other/spaceship_speed.png'))
SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
BULLET_GATRON = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_gatron.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ALIEN = pygame.image.load(os.path.join(IMG_DIR, 'Enemy/alien.png'))
PRINCESS = pygame.image.load(os.path.join(IMG_DIR, 'Enemy/princess.png'))
BOSS = pygame.image.load(os.path.join(IMG_DIR, 'Enemy/gatron.png'))
SPEED = pygame.image.load(os.path.join(IMG_DIR, 'Other/speed.png'))
LIFE_BAR_1 = pygame.image.load(os.path.join(IMG_DIR, 'Other/life_bar_1.png'))
LIFE_BAR_2  = pygame.image.load(os.path.join(IMG_DIR, 'Other/life_bar_2.png'))
LIFE_BAR_3  = pygame.image.load(os.path.join(IMG_DIR, 'Other/life_bar_3.png'))
LIFE_BAR_4  = pygame.image.load(os.path.join(IMG_DIR, 'Other/life_bar_4.png'))



FONT_STYLE = 'freesansbold.ttf'
BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)

BULLET_ENEMY_TYPE = 'enemy'
BULLET_SPACESHIP_TYPE = 'spaceship'


pygame.mixer.init()
SHOOT_SPACESHIP = pygame.mixer.Sound(os.path.join(IMG_DIR, "Sound/spaceship_shoot.mp3"))
ENEMY_SHOOT = pygame.mixer.Sound(os.path.join(IMG_DIR, "Sound/enemy_shoot.mp3"))
