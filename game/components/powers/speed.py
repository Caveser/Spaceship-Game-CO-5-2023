from game.components.powers.power import Power
from game.utils.constants import SPEED,SPEED_TYPE, SPACESHIP_SPEED

class Speed(Power):

    def __init__(self):
        super().__init__(SPEED, SPEED_TYPE, SPACESHIP_SPEED)