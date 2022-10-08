import random

from dino_runner.components.obstacles.obstacle import obstacle
from dino_runner.utils.constants import BIRD


class bird(obstacle):
    BIRD_HEIGHTS = [300,290,320]
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = random.choice(self.BIRD_HEIGHTS)
        self.setp_index = 0
        self.image = BIRD[0]
                
    def draw_bird (self, screen):
        self.image = BIRD[0] if self.step_index < 2 else BIRD[1] 
        
