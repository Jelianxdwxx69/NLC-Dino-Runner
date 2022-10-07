from turtle import update
import pygame

from pygame.sprite import Sprite #importamos Sprite de pygame
from dino_runner.utils.constants import DUCKING, DUCKING_HAMMER, DUCKING_SHIELD, HAMMER_TYPE, JUMPING_HAMMER, JUMPING_SHIELD, RUNNING , JUMPING, DEFAULT_TYPE, RUNNING_HAMMER, RUNNING_SHIELD, SHIELD_TYPE

DUCK_IMAGE = {DEFAULT_TYPE : DUCKING, SHIELD_TYPE:DUCKING_SHIELD, HAMMER_TYPE:DUCKING_HAMMER}
JUMP_IMAGE = {DEFAULT_TYPE : JUMPING, SHIELD_TYPE:JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}
RUN_IMAGE = {DEFAULT_TYPE : RUNNING, SHIELD_TYPE:RUNNING_SHIELD, HAMMER_TYPE:RUNNING_HAMMER}

class Dinosaur (Sprite): #Sprite para herencia 
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 350 #NUEVA POSICION PARA DUCK EN Y 
    JUMP_VEL =8.5
#**************BUILDER METHOD*************
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMAGE[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

        self.step_index = 0

        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False

        self.jump_vel = self.JUMP_VEL #velocidad del dinosaurio
    def setup_state (self):
        self.has_power_up = False
        self.shield = False
        self.show_text = False
        self.shield_time_up = 0
        self.hammer = False
        self.show_text = False
        self.hammer_time_up = 0 
#************UPDATE METHOD**************          
    def update(self, user_input):
        if self.dino_run: # CONDICIONAL PARA DETECTAR SI ESTA CORRIENDO
            self.run()
        elif self.dino_jump:
            self.jump()
        if self.dino_duck:
            self.duck()
            
        if user_input[pygame.K_UP] or user_input[pygame.K_SPACE] and not self.dino_jump:#detectando evento del usuario (ADICIONAR SPACE) K_SAPACE(EXTRA PROYECTO)
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_jump = False
            self.dino_run = False         
        elif not self.dino_jump:
            self.dino_jump = False
            self.dino_run = True
            self.dino_duck = False    

        if self.step_index >=10:
            self.step_index = 0    #step_index ayuda a intercalar las imagenes 
#************JUMP METHOD**************             
    def jump (self):
        self.image = JUMP_IMAGE[self.type]
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            print(self.dino_rect.y)
            self.jump_vel -=0.8
            print(self.jump_vel)
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_jump  = False
            self.jump_vel = self.JUMP_VEL 
#*************DUCK METHOD****************
    def duck(self):
        self.image = DUCK_IMAGE[self.type][self.step_index //5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS #RESETEANDO SU POSICION 
        self.dino_rect.y =  self.Y_POS_DUCK
        self.step_index += 1
#**************RUN METHOD******************                  
    def run (self):
        self.image = RUN_IMAGE[self.type][self.step_index //5]
        self.image = RUNNING[0] if self.step_index <5 else RUNNING[1]  #INTERCAMBIENADO DE IMAGENE PARA DAR LA IMPRESION DE CAMINAR 
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS#RESETEANDO SU POSICION 
        self.dino_rect.y =  self.Y_POS
        self.step_index += 1 
#**************DRAW METHOD**************        
    def draw(self, screen: pygame.Surface ): #surface es un tipo de dato
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def check_invicibility (self):
        pass 

    #implementar power ups (martillo) luego lo qeu se pueda 
    # usa el 200% o mas estupida   