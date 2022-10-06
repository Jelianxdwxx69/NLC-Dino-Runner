import random
from dino_runner.components.obstacles.obstacle import obstacle

class cactus(obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type) # se untiliza super para llamar  la clase "padre" o principal, con su constructor
        self.rect.y = 325