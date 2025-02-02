import random
import pygame
from dino_runner.components.obstacles.bird import bird
from dino_runner.components.obstacles.cactus import cactus
from dino_runner.utils.constants import BIRD, SMALL_CACTUS, LARGE_CACTUS

class obstacle_manager():

    def __init__(self) :
        self.obstacles = []
        
    def update (self, game):
        if len(self.obstacles) == 0:
            if random.randint(0,2) == 0:
                small_cactus = cactus(SMALL_CACTUS)
                self.obstacles.append(small_cactus)
            elif random.randint(0,2) == 1:    
                large_cactus = cactus(LARGE_CACTUS)   
                self.obstacles.append(large_cactus)
            elif random.randint(0,2) == 2:
                bird_obtacle = bird(BIRD)
                self.obstacles.append(bird_obtacle)

        for obstacle in self.obstacles:
             obstacle.update(game.game_speed, self.obstacles)
             if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.shield and not game.player.hammer:
                    pygame.time.delay(500)
                    game.playing = False                   
                    game.death_count += 1
                    if game.player.shield and not game.player.hummer:
                        game.playing = True
                    elif game.player.hummer and not game.player.shield:
                        self.obstacles.remove(obstacle)
                break    
                
    def draw (self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.reset_obstacles= []    