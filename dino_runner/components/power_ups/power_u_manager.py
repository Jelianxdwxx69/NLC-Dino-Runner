import random
import pygame
import dino_runner 

from dino_runner.components.power_ups.shield import shield
from dino_runner.utils.constants import SHIELD
from dino_runner.components.power_ups.hammer import hammer
from dino_runner.utils.constants import HAMMER

class power_up_manager :
    def __init__(self) -> None:
        self.power_ups = []
        self.when_appears = 0

    def generate_power_ups(self,points):
        if len(self.power_ups) == 0:
            if self.when_appears == points:
                self.when_appears = random.randint(self.when_appears*200,self.when_appears*300)
                self.power_ups.append(shield())
                self.power_ups.append(hammer()) 
           
                   

    def update (self, game_speed, player, points):
        self.generate_power_ups(points)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
               power_up.start_time = pygame.time.get_ticks()
               player.shield = True
               player.hammer = True
               player.show_text = True
               player.type = power_up.type
               time_random = random.randint(5,8)
               player.shield_time_up = power_up.start_time*(time_random*1000)
               player.hammer_time_up = power_up.start_time*(time_random*1000)
               self.power_ups.remove(power_up)  
            break
    def draw (self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)   

    def reset_power_ups(self):
        self.power_ups= []
        self.when_appears = random.randint(200,300)       