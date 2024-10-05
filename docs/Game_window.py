import threading
from Animetion import Animetion
from Operator import Operator
from Logic import Ingame_Logic

logic = Ingame_Logic()
animetion = Animetion()
operator = Operator()

class Window():
    def Start_game(self):
        operator.Operator_Start()
        animetion.Background_start_game(operator.button1_sprite[0], operator.button2_sprite[0], operator.button3_sprite[0])


    def Ingame(self):
        operator.Operator_move()
        threading.Thread(target=logic.Enemy_run(operator.event_level[1], operator.event_level[2]))
        animetion.Run_jump_attack_animetion(logic.xy_sprite[0], logic.xy_sprite[1], operator.animetion[0])
    
    def Setting_Game(self):
        operator.Operator_Setting()
        animetion.Background_Setting_Game(operator.button1_sprite[0], operator.button2_sprite[0], operator.button3_sprite[0], operator.event_sound, operator.event_level)
        pass
    
    
class Control_windows():
    def __init__(self):
        if operator.control_windows[0] == 0:
            Window().Start_game()
        if operator.control_windows[0] == 1:
            Window().Ingame()
        if operator.control_windows[0] == 2:
            Window().Setting_Game()