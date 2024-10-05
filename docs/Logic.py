import pygame, random
from Data import Data

data = Data()

class Ingame_Logic():
    def __init__(self): #Update_data
        self.xy_player = data.xy_player
        self.xy_sprite = data.xy_sprite
        self.hp_player = data.hp_player
        #enemy
        self.x_sprite_enemy = data.x_sprite_enemy
        self.y_sprite_enemy = data.y_sprite_enemy
        self.x_enemy_spaw = data.x_enemy_spaw
        #time
        self.tick = 0
        #event
        self.game_over = data.game_over

    def Run_right(self):
        if data.xy_player[0] + 120 < 1400:
            data.xy_player[0] += 20
        data.xy_sprite[0] += 1
        data.player_side = 0
        if data.xy_player[1] == 450:
            data.xy_sprite[1] = 0
            if data.xy_sprite[0] > 3:
                data.xy_sprite[0] = 0          
        elif data.xy_player[1] != 450:
            data.xy_sprite[1] = 6
            if data.xy_sprite[0] > 19:
                data.xy_sprite[0] = 0

    def Run_left(self):
        if data.xy_player[0] > 0:
            data.xy_player[0] -= 20
        data.player_side = 1
        data.xy_sprite[0] += 1
        if data.xy_player[1] == 450:
            data.xy_sprite[1] = 1
            if data.xy_sprite[0] > 3:
                data.xy_sprite[0] = 0          
        elif data.xy_player[1] != 450:
            data.xy_sprite[1] = 7
            if data.xy_sprite[0] > 19:
                data.xy_sprite[0] = 0

    def Run_idle(self):
        data.xy_sprite[0] += 1
        if data.player_side == 0:
            if data.xy_player[1] == 450:
                data.xy_sprite[1] = 2
                if data.xy_sprite[0] > 0:
                    data.xy_sprite[0] = 0
            elif data.xy_player[1] != 450:
                data.xy_sprite[1] = 6
                if data.xy_sprite[0] > 19:
                    data.xy_sprite[0] = 0
        if data.player_side == 1:
            if data.xy_player[1] == 450:
                data.xy_sprite[1] = 3
                if data.xy_sprite[0] > 0:
                    data.xy_sprite[0] = 0
            elif data.xy_player[1] != 450:
                data.xy_sprite[1] = 7
                if data.xy_sprite[0] > 19:
                    data.xy_sprite[0] = 0
        
    def Jump_logic(self):
        keys = pygame.key.get_pressed()
        if data.xy_player[1] == 450:
            if keys[pygame.K_SPACE]:
                data.jump_speed = -20
        data.xy_player[1] += data.jump_speed  
        if data.xy_player[1] < 300:
            data.jump_speed = 20
        if data.xy_player[1] > 450:
            data.jump_speed = -20
        elif data.xy_player[1] == 450:
            data.jump_speed = 0  

    def Attack_logic(self):
        data.xy_sprite[0] += 1
        if data.player_side == 0:
            data.xy_sprite[1] = 0
            if data.xy_sprite[0] > 11:
                data.xy_sprite[0] = 0
        if data.player_side == 1:
            data.xy_sprite[1] = 1
            if data.xy_sprite[0] > 11:
                data.xy_sprite[0] = 0
              
    def Enemy_run(self, level, damage):
        self.tick += 1
        if len(data.x_enemy_spaw) <= level:
            for i in range(level-len(data.x_enemy_spaw)):
                if self.tick >= 30:
                    self.tick = 0
                    x = random.choice(data.spaw_enemy)
                    data.x_enemy_spaw.append(x)
        for i in range(len(data.x_enemy_spaw)):
            data.x_sprite_enemy[i] += 1
            if data.x_sprite_enemy[i] > 8:
                data.x_sprite_enemy[i] = 0
        for i in range(len(data.x_enemy_spaw)):
            if data.x_enemy_spaw[i] < data.xy_player[0] - 30:
                data.x_enemy_spaw[i] += 5
                data.y_sprite_enemy[i] = 2
            elif data.x_enemy_spaw[i] > data.xy_player[0] + 30:
                data.x_enemy_spaw[i] -= 5
                data.y_sprite_enemy[i] = 3
        for i in range(len(data.x_enemy_spaw)):
            if data.x_enemy_spaw[i] == data.xy_player[0] - 30:
                if data.xy_player[1] == 450:
                    data.y_sprite_enemy[i] = 0
                    if data.hp_player[0] > 0:
                        data.hp_player[0] -= damage
                        if data.hp_player[0] < 0:
                            data.hp_player[0] = 0
            if data.x_enemy_spaw[i] == data.xy_player[0] + 30:
                if data.xy_player[1] == 450:
                    data.y_sprite_enemy[i] = 1
                    if data.hp_player[0] > 0:
                        data.hp_player[0] -= damage
                        if data.hp_player[0] < 0:
                            data.hp_player[0] = 0
        if data.hp_player[0] == 0:
            data.game_over[0] = False
            
    def Attack_enemy(self):
        for i in range(len(data.x_enemy_spaw)):
            x = random.choice(data.spaw_enemy)
            if data.player_side == 1:
                if data.xy_player[0] - 150 <= data.x_enemy_spaw[i] and data.x_enemy_spaw[i] <= data.xy_player[0]:
                    data.x_enemy_spaw.pop(i)
                    data.x_enemy_spaw.insert(i, x)
            if data.player_side == 0:
                if data.xy_player[0] <= data.x_enemy_spaw[i] and data.x_enemy_spaw[i] <= data.xy_player[0] + 150:
                    data.x_enemy_spaw.pop(i)
                    data.x_enemy_spaw.insert(i, x)
            