class Data():
    def __init__(self):
        self.i = 0
        #windowscale
        self.width_height = [1280, 720]
        #player
        self.hp_player = [100]
        self.player_side = 0
        self.jump_speed = 0
        self.xy_player = [200, 450]
        #enemy
        self.x_enemy_spaw = []
        self.spaw_enemy = [-180, -120, -60, 0, 1280, 1340, 1400, 1460]
        self.x_sprite_enemy = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.y_sprite_enemy = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        #sprite sheet
        self.animetion = [0]
        self.button1_sprite = [3]
        self.button2_sprite = [3]
        self.button3_sprite = [3]
        self.xy_sprite = [0, 0] #{"run_right" : 0, "run_left" : 1, "idle_right" : 2, "idle_left" : 3, "stun_left" : 4,  "stun_right" : 5, "jump_right" : 6, "jump_left" : 7}
        #text
        self.text = {'start' : "START", 'setting' : "SETTING", 'exit' : "EXIT", 'sound0' : "SOUND : ON", 'sound1' : "SOUND : OFF", 'level1' : "LEVEL : EASY",
                    'level2' : "LEVEL : MEDIUM", 'level3' : "LEVEL : HARD", 'back' : "BACK", 'game_over' : "GAME OVER", 'control' : "CONTROL", 'control_a' : "A : MOVE LEFT",
                    'control_d' : "D : MOVE RIGHT", 'control_j' : "J : ATTACK"}
        #color
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        #loop game
        self.control_windows = [0]
        #check event
        self.event_sound = [0]
        self.event_level = [0, 5, 1]
        self.game_over = [True]