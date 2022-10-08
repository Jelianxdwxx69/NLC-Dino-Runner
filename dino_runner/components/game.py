import pygame

from dino_runner.components.obstacles.obstacle_manager import obstacle_manager
from dino_runner.components.power_ups.power_u_manager import power_up_manager
from dino_runner.utils.constants import BG, ICON, RUNNING, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur import Dinosaur

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.player = Dinosaur()
        self.obstacle_manager = obstacle_manager()
        self.power_up_manager = power_up_manager()
        self.playing = False
        self.running = False
        self.game_speed = 15
        self.x_pos_bg = 0
        self.y_pos_bg = 380

        self.points = 0
        self.death_count = 0 

    def execute (self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu() 
            else:
                self.run()
        pygame.display.quit()            
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.playing = True
        self.game_speed = 20
        self.points = 0
        while self.playing:
            self.events()
            self.update()
            self.draw()
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        self.update_score()
        user_input = pygame.key.get_pressed() #ayuda a obtenber la tecla presionada
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self.game_speed, self.player, self.points)

    def update_score(self):
        self.points += 1
        if self.points % 100 == 0:
           self.game_speed += 5    

    def draw_score(self):
        font = pygame.font.Font("freesansbold.ttf", 30)#implremntar fondo
        text = font.render(f"POINTS:  {self.points}", True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (100, 50)
        self.screen.blit(text, text_rect)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_score()
        self.player.draw(self.screen)
        self.player.check_invicibility(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def handle_key_events_on_menu(self):
        for event in  pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                self.run()

    def show_menu(self):
        self.screen.fill((255, 255, 255))
        half_screen_height = SCREEN_HEIGHT // 2 
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            font = pygame.font.Font("freesansbold.ttf", 30)#implremntar fondo
            text = font.render("PRESS ANY KEY TO START", True, (0,0,0))
            text_rect = text.get_rect()
            text_rect.center = ((SCREEN_WIDTH//2),((SCREEN_HEIGHT//2)-120))
            self.screen.blit(text, text_rect)

        elif  self.death_count > 0:
            #**********************LETRERO DE RESTART*********************
            font = pygame.font.Font("freesansbold.ttf", 30)#implremntar fondo
            text = font.render("PRESS ANY KEY TO RESTART", True, (0,0,0))
            text_rect = text.get_rect()
            text_rect.center = ((SCREEN_WIDTH//2),((SCREEN_HEIGHT//2)-120))
            self.screen.blit(text, text_rect)
            #*****************LETRERO DE PUNTOS ACUMULADOS******************
            font = pygame.font.Font("freesansbold.ttf", 30)#implremntar fondo
            text = font.render(f"POINTS:  {self.points}", True, (0,0,0))
            text_rect = text.get_rect()
            text_rect.center = (100, 50)
            self.screen.blit(text, text_rect)  

        self.screen.blit(RUNNING[0], ((SCREEN_WIDTH//2),(SCREEN_HEIGHT//2)))
        pygame.display.update()
        self.handle_key_events_on_menu()