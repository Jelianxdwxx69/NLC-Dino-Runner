import pygame

from pygame.sprite import Sprite #importamos Sprite de pygame
from dino_runner.utils.constants import DUCKING, RUNNING , JUMPING

class Dinosaur (Sprite): #Sprite para herencia 
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 350 #NUEVA POSICION PARA DUCK EN Y 
    JUMP_VEL =8.5
#**************BUILDER METHOD*************
    def __init__(self):
        self.image = RUNNING [0] #IMPORTANDO DINOSAURIO CORRIENDO
        self.image = JUMPING #IMPORTANDO DINOSAURIO SALTANDO
        self.image = DUCKING #IMPORTANDO DINOSAURIO AGACHADO 

        self.dino_rect = self.image.get_rect()   #get_rect ayuda a obtener la posicion de un objeto
        #AttributeError: 'list' object has no attribute 'get_rect' ? (solucionar :c)
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

        self.step_index = 0

        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False

        self.jump_vel = self.JUMP_VEL #velocidad del dinosaurio
#***********RUN VERIFICATION METHOD(BETA)************       
    def run_verification(self):
        if self.dino_run: # CONDICIONAL PARA DETECTAR SI ESTA CORRIENDO
            self.run()
        elif self.dino_jump:
            self.jump()
        update_object = Dinosaur()
        update_object.update()
#************UPDATE METHOD**************          
    def update(self, user_input):
        if user_input[pygame.K_UP] and not self.dino_jump:#detectando evento del usuario
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False    
        elif not self.dino_jump:
            self.dino_jump = False
            self.dino_run = True
            self.dino_duck = False
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_jump = False
            self.dino_run = False 
        elif not self.dino_duck:
            self.dino_jump = False
            self.dino_run = True
            self.dino_duck = False           
        if self.step_index >=10:
            self.step_index = 0    #step_index ayuda a intercalar las imagenes 
#************JUMP METHOD**************             
    def jump (self):
        self.image = JUMPING
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
        self.image = DUCKING [0] if self.step_index <5 else DUCKING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS#RESETEANDO SU POSICION 
        self.dino_rect.y =  self.Y_POS_DUCK
        self.step_index += 1
#**************RUN METHOD******************                  
    def run (self):
        self.image = RUNNING[0] if self.step_index <5 else RUNNING[1]  #INTERCAMBIENADO DE IMAGENE PARA DAR LA IMPRESION DE CAMINAR 
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS#RESETEANDO SU POSICION 
        self.dino_rect.y =  self.Y_POS
        self.step_index += 1 
#**************DRAW METHOD**************        
    def draw(self, screen: pygame.Surface ): #surface es un tipo de dato
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))