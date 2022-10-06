import random
from dino_runner.components.obstacles.obstacle import obstacle
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS

class cactus(obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type) # se untiliza super para llamar  la clase "padre" o principal, con su constructor
        if image == SMALL_CACTUS: # PARA SELECCIONAR LA ALTURA
           self.rect.y = 350
        elif image == LARGE_CACTUS:
            self.rect.y = 300 #300 PARA QUE PAREZCA MAS ALTO DE LOS OTROS :v por si acaso 
   