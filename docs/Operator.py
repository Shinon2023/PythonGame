import pygame, threading
from Logic import Ingame_Logic
from Animetion import Animetion
from Data import Data
from Main_Module import Module
from Audio_ost import Audio

module = Module()
data = Data()
animetion = Animetion()
logic = Ingame_Logic()
audio = Audio()

class Operator():
    def __init__(self):
        self.button1_sprite = data.button1_sprite
        self.button2_sprite = data.button2_sprite
        self.button3_sprite = data.button3_sprite
        self.control_windows = data.control_windows
        self.animetion = data.animetion
        self.event_sound = data.event_sound
        self.event_level = data.event_level
        self.check_event_attack = 0
    def Operator_move(self):
        if logic.game_over[0] == True:
            pos1 = pygame.mouse.get_pos()
            keys = pygame.key.get_pressed() 
            logic.Jump_logic()
            if self.check_event_attack > 0:
                self.check_event_attack += 1
                logic.Attack_logic()
                if self.check_event_attack > 12:
                    self.check_event_attack = 0
            elif keys[pygame.K_a]:
                logic.Run_left()
                
                data.animetion[0] = 0
            elif keys[pygame.K_d]:
                logic.Run_right()
                data.animetion[0] = 0
            elif keys[pygame.K_j]:
                if logic.xy_player[1] == 450:
                    self.check_event_attack = 1
                    data.animetion[0] = 1
                    logic.Attack_enemy()
            else:
                logic.Run_idle()
                data.animetion[0] = 0
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if logic.game_over[0] == False:
                        if animetion.get_rect_windows.collidepoint(pos):
                            data.control_windows[0] = 0       
            
    def Operator_Start(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if animetion.button1_surface.collidepoint(pos):
                    data.control_windows[0] = 1
                elif animetion.button2_surface.collidepoint(pos):
                    data.control_windows[0] = 2
                elif animetion.button3_surface.collidepoint(pos):
                    pygame.quit()  
        if pygame.mouse.get_pressed():
            pos1 = pygame.mouse.get_pos()
            if animetion.button1_surface.collidepoint(pos1):
                data.button1_sprite[0] = 0
            elif animetion.button1_surface.collidepoint(animetion.button1_surface.center):
                data.button1_sprite[0] = 3
            if animetion.button2_surface.collidepoint(pos1):
                data.button2_sprite[0] = 0
            elif animetion.button2_surface.collidepoint(animetion.button2_surface.center):
                data.button2_sprite[0] = 3
            if animetion.button3_surface.collidepoint(pos1):
                data.button3_sprite[0] = 0
            elif animetion.button3_surface.collidepoint(animetion.button3_surface.center):
                data.button3_sprite[0] = 3
                   
    def Operator_Setting(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if data.event_sound[0] == 0:    
                    if animetion.button1_surface.collidepoint(pos):
                        data.event_sound[0] = 1
                elif data.event_sound[0] == 1:
                    if animetion.button1_surface.collidepoint(pos):
                        data.event_sound[0] = 0
                if data.event_level[0] == 0:
                    if animetion.button2_surface.collidepoint(pos):
                        data.event_level[0] = 1
                        data.event_level[1] = 10
                        data.event_level[2] = 2
                elif data.event_level[0] == 1:
                    if animetion.button2_surface.collidepoint(pos):
                        data.event_level[0] = 2
                        data.event_level[1] = 15
                        data.event_level[2] = 3
                elif data.event_level[0] == 2:
                    if animetion.button2_surface.collidepoint(pos):
                        data.event_level[0] = 0
                        data.event_level[1] = 5
                        data.event_level[2] = 1
                if animetion.button3_surface.collidepoint(pos):
                    data.control_windows[0] = 0 
        if pygame.mouse.get_pressed():
            pos1 = pygame.mouse.get_pos()
            if animetion.button1_surface.collidepoint(pos1):
                data.button1_sprite[0] = 0
            elif animetion.button1_surface.collidepoint(animetion.button1_surface.center):
                data.button1_sprite[0] = 3
            if animetion.button2_surface.collidepoint(pos1):
                data.button2_sprite[0] = 0
            elif animetion.button2_surface.collidepoint(animetion.button2_surface.center):
                data.button2_sprite[0] = 3
            if animetion.button3_surface.collidepoint(pos1):
                data.button3_sprite[0] = 0
            elif animetion.button3_surface.collidepoint(animetion.button3_surface.center):
                data.button3_sprite[0] = 3
    
    def Operator_audio(self):
        audio.play_main(data.control_windows[0], data.event_sound[0])
        audio.play_ingame(data.control_windows[0], data.event_sound[0])        