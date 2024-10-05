import pygame

from Main_Module import Module
from Data import Data
from Logic import Ingame_Logic

logic = Ingame_Logic()
module = Module()
data = Data()

class Animetion():
    def __init__(self):
        #load image
        self.background = pygame.image.load("image\Background\Background.jpg")
        self.background_start_game = pygame.image.load("image\Background\Background_start_game.jpg")
        self.animetion = pygame.image.load("image\Animetion Sprite\Runing animetion.png")
        self.button = pygame.image.load("Image\Button 1\Button.png")
        self.attack_animetion = pygame.image.load("Image\Animetion Sprite\Attack Animetion.png")
        self.player = pygame.image.load("Image\Animetion Sprite\Player.png")
        self.slime_enemy = pygame.image.load("Image\Animetion Sprite\slime enemy.png")
        self.text_box = pygame.image.load("image\Background\Text_box.png")
        #set scale image
        self.button = pygame.transform.scale(self.button, (960, 80))
        self.animetion = pygame.transform.scale(self.animetion, (2400, 960))
        self.attack_animetion = pygame.transform.scale(self.attack_animetion, (3840, 240))
        self.slime_enemy = pygame.transform.scale(self.slime_enemy, (900, 450))
        self.text_box = pygame.transform.scale(self.text_box, (1280, 150))
        #set surface
        self.player_surface = pygame.Surface((120, 120))
        self.attack_player_surface = pygame.Surface((320, 120))
        self.button_surface = pygame.Surface((240, 80))
        self.slime_enemy_surface = pygame.Surface((90, 90))
        #set rect
        self.get_rect_windows = module.window.get_rect()
        #player surface
        self.player_surface = self.player_surface.get_rect()
        self.attack_player_surface = self.attack_player_surface.get_rect()
        self.attack_player_surface.y = 390
        #slime enemy surface
        self.slime_enemy_surface = self.slime_enemy_surface.get_rect()
        self.slime_enemy_surface.y = 425
        #button start
        self.button1_surface = self.button_surface.get_rect()
        self.button1_surface.centerx = self.get_rect_windows.centerx
        self.button1_surface.y = 200
        self.button2_surface = self.button_surface.get_rect()
        self.button2_surface.centerx = self.get_rect_windows.centerx
        self.button2_surface.y = 350
        self.button3_surface = self.button_surface.get_rect()
        self.button3_surface.centerx = self.get_rect_windows.centerx
        self.button3_surface.y = 500
        #text
        self.text_start = module.base_font.render(data.text['start'], True, data.white)
        self.text_setting = module.base_font.render(data.text['setting'], True, data.white)
        self.text_exit = module.base_font.render(data.text['exit'], True, data.white)
        self.text_sound_on = module.base_font.render(data.text['sound0'], True, data.white)
        self.text_sound_off = module.base_font.render(data.text['sound1'], True, data.white)
        self.text_level_easy = module.base_font.render(data.text['level1'], True, data.white)
        self.text_level_medium = module.base_font.render(data.text['level2'], True, data.white)
        self.text_level_hard = module.base_font.render(data.text['level3'], True, data.white)
        self.text_back = module.base_font.render(data.text['back'], True, data.white)
        self.game_over = module.big_font.render(data.text['game_over'], True, data.black)
        self.control = module.base_font.render(data.text['control'], True, data.black)
        self.control_a = module.base_font.render(data.text['control_a'], True, data.black)
        self.control_d = module.base_font.render(data.text['control_d'], True, data.black)
        self.control_j = module.base_font.render(data.text['control_j'], True, data.black)
        
    def Run_jump_attack_animetion(self, x_sprite, y_sprite, animetion):
        #declare a variable
        self.hp_player_surface = pygame.Surface((logic.hp_player[0], 25))
        self.player_surface.centerx = logic.xy_player[0]
        self.player_surface.centery = logic.xy_player[1]
        self.attack_player_surface.centerx = logic.xy_player[0]
        if logic.hp_player[0] > 50:
            self.hp_player_surface.fill((0, 255, 0))
        elif logic.hp_player[0] <= 50:
            self.hp_player_surface.fill((255, 0, 0))
        #background
        module.window.blit(self.background, (0, 0))
        module.window.blit(self.text_box, (0, 570))
        module.window.blit(self.control, self.control.get_rect(center = (150, 610)))
        module.window.blit(self.control_a, self.control_a.get_rect(center = (180, 640)))
        module.window.blit(self.control_d, self.control_d.get_rect(center = (187, 670)))
        module.window.blit(self.control_j, self.control_j.get_rect(center = (380, 640)))
        pygame.draw.rect(module.window, (0, 0, 0), (49, 39, 102, 27))
        if logic.hp_player[0] > 0:
            module.window.blit(self.hp_player_surface, (50, 40))
        if logic.game_over[0] == False:
            module.window.blit(self.game_over, self.game_over.get_rect(center = self.get_rect_windows.center))
        module.window.blit(self.player, (15, 15))
        #animetion
        if animetion == 0:
            module.window.blit(self.animetion, (self.player_surface), (x_sprite * 120, y_sprite * 120, 120, 120))
        elif animetion == 1:
            module.window.blit(self.attack_animetion, (self.attack_player_surface), (x_sprite * 320, y_sprite * 120, 320, 120))
        if len(logic.x_enemy_spaw) > 0:
            self.slime_enemy_surface.centerx = logic.x_enemy_spaw[0]
            module.window.blit(self.slime_enemy, self.slime_enemy_surface, (logic.x_sprite_enemy[0] * 90, logic.y_sprite_enemy[0] * 90, 90, 90))
            if len(logic.x_enemy_spaw) > 1:
                self.slime_enemy_surface.centerx = logic.x_enemy_spaw[1]
                module.window.blit(self.slime_enemy, self.slime_enemy_surface, (logic.x_sprite_enemy[1] * 90, logic.y_sprite_enemy[1] * 90, 90, 90))
                if len(logic.x_enemy_spaw) > 2:
                    self.slime_enemy_surface.centerx = logic.x_enemy_spaw[2]
                    module.window.blit(self.slime_enemy, self.slime_enemy_surface, (logic.x_sprite_enemy[2] * 90, logic.y_sprite_enemy[2] * 90, 90, 90))
                    if len(logic.x_enemy_spaw) > 3:
                        self.slime_enemy_surface.centerx = logic.x_enemy_spaw[3]
                        module.window.blit(self.slime_enemy, self.slime_enemy_surface, (logic.x_sprite_enemy[3] * 90, logic.y_sprite_enemy[3] * 90, 90, 90))
                        if len(logic.x_enemy_spaw) > 4:
                            self.slime_enemy_surface.centerx = logic.x_enemy_spaw[4]
                            module.window.blit(self.slime_enemy, self.slime_enemy_surface, (logic.x_sprite_enemy[4] * 90, logic.y_sprite_enemy[4] * 90, 90, 90))
                            if len(logic.x_enemy_spaw) > 5:
                                self.slime_enemy_surface.centerx = logic.x_enemy_spaw[5]
                                module.window.blit(self.slime_enemy, self.slime_enemy_surface, (logic.x_sprite_enemy[5] * 90, logic.y_sprite_enemy[5] * 90, 90, 90))
                                if len(logic.x_enemy_spaw) > 6:
                                    self.slime_enemy_surface.centerx = logic.x_enemy_spaw[6]
                                    module.window.blit(self.slime_enemy, self.slime_enemy_surface, (logic.x_sprite_enemy[6] * 90, logic.y_sprite_enemy[6] * 90, 90, 90))
                                    if len(logic.x_enemy_spaw) > 7:
                                        self.slime_enemy_surface.centerx = logic.x_enemy_spaw[7]
                                        module.window.blit(self.slime_enemy, self.slime_enemy_surface, (logic.x_sprite_enemy[7] * 90, logic.y_sprite_enemy[7] * 90, 90, 90))
                                        if len(logic.x_enemy_spaw) > 8:
                                            self.slime_enemy_surface.centerx = logic.x_enemy_spaw[8]
                                            module.window.blit(self.slime_enemy, self.slime_enemy_surface, (logic.x_sprite_enemy[8] * 90, logic.y_sprite_enemy[8] * 90, 90, 90))
                                            if len(logic.x_enemy_spaw) > 9:
                                                self.slime_enemy_surface.centerx = logic.x_enemy_spaw[9]
                                                module.window.blit(self.slime_enemy, self.slime_enemy_surface, (logic.x_sprite_enemy[9] * 90, logic.y_sprite_enemy[9] * 90, 90, 90))
                                                if len(logic.x_enemy_spaw) > 10:
                                                    self.slime_enemy_surface.centerx = logic.x_enemy_spaw[10]
                                                    module.window.blit(self.slime_enemy, self.slime_enemy_surface, (logic.x_sprite_enemy[10] * 90, logic.y_sprite_enemy[10] * 90, 90, 90))
                                                    if len(logic.x_enemy_spaw) > 11:
                                                        self.slime_enemy_surface.centerx = logic.x_enemy_spaw[11]
                                                        module.window.blit(self.slime_enemy, self.slime_enemy_surface, (logic.x_sprite_enemy[11] * 90, logic.y_sprite_enemy[11] * 90, 90, 90))
                                                        if len(logic.x_enemy_spaw) > 12:
                                                            self.slime_enemy_surface.centerx = logic.x_enemy_spaw[12]
                                                            module.window.blit(self.slime_enemy, self.slime_enemy_surface, (logic.x_sprite_enemy[12] * 90, logic.y_sprite_enemy[12] * 90, 90, 90))
                                                            if len(logic.x_enemy_spaw) > 13:
                                                                self.slime_enemy_surface.centerx = logic.x_enemy_spaw[13]
                                                                module.window.blit(self.slime_enemy, self.slime_enemy_surface, (logic.x_sprite_enemy[13] * 90, logic.y_sprite_enemy[13] * 90, 90, 90))
                                                                if len(logic.x_enemy_spaw) > 14:
                                                                    self.slime_enemy_surface.centerx = logic.x_enemy_spaw[14]
                                                                    module.window.blit(self.slime_enemy, self.slime_enemy_surface, (logic.x_sprite_enemy[14] * 90, logic.y_sprite_enemy[14] * 90, 90, 90))
                            
    def Background_start_game(self, button1_sprite,button2_sprite, button3_sprite):
        module.window.blit(self.background_start_game, (0, 0))
        #button start
        module.window.blit(self.button, self.button1_surface, (button1_sprite * 240, 1, 240, 80))
        module.window.blit(self.text_start, self.text_start.get_rect(center = self.button1_surface.center))
        #button setting
        module.window.blit(self.button, self.button2_surface, (button2_sprite * 240, 1, 240, 80))
        module.window.blit(self.text_setting, self.text_setting.get_rect(center = self.button2_surface.center))
        #button exit
        module.window.blit(self.button, self.button3_surface, (button3_sprite * 240, 1, 240, 80))
        module.window.blit(self.text_exit, self.text_exit.get_rect(center = self.button3_surface.center))
         
    def Background_Setting_Game(self, button1_sprite, button2_sprite, button3_sprite, event_sound, event_level):
        module.window.blit(self.background_start_game, (0, 0))
        #button sound
        module.window.blit(self.button, self.button1_surface, (button1_sprite * 240, 1, 240, 80))
        if event_sound[0] == 0:
            module.window.blit(self.text_sound_on, self.text_sound_on.get_rect(center = self.button1_surface.center))
        if event_sound[0] == 1:
            module.window.blit(self.text_sound_off, self.text_sound_on.get_rect(center = self.button1_surface.center))
        #button level
        module.window.blit(self.button, self.button2_surface, (button2_sprite * 240, 1, 240, 80))
        if event_level[0] == 0:
            module.window.blit(self.text_level_easy, self.text_level_easy.get_rect(center = self.button2_surface.center))
        if event_level[0] == 1:
            module.window.blit(self.text_level_medium, self.text_level_medium.get_rect(center = self.button2_surface.center))
        if event_level[0] == 2:
            module.window.blit(self.text_level_hard, self.text_level_hard.get_rect(center = self.button2_surface.center))
        #button back
        module.window.blit(self.button, self.button3_surface, (button3_sprite * 240, 1, 240, 80))
        module.window.blit(self.text_back, self.text_back.get_rect(center = self.button3_surface.center))
        