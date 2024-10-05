import pygame

class Audio():
    def __init__(self):
        self.main_page_ost = pygame.mixer.Sound('Audio\The First Town.wav')
        self.ingame_page_ost = pygame.mixer.Sound('Audio\Swordland.wav')

    def play_main(self, control_windows, event_sound):
        if event_sound == 0:
            if control_windows == 0:
                self.ingame_page_ost.stop()
                if pygame.mixer.get_busy() == False:
                    self.main_page_ost.play()
            elif control_windows == 2:
                self.ingame_page_ost.stop()
                if pygame.mixer.get_busy() == False:
                    self.main_page_ost.play()
        else:
            self.main_page_ost.stop()
                         
    def play_ingame(self, control_windows, event_sound):  
        if event_sound == 0:
            if control_windows == 1:
                self.main_page_ost.stop()
                if pygame.mixer.get_busy() == False:
                    print(event_sound)
                    print(control_windows)
                    self.ingame_page_ost.play()
        else:
            self.ingame_page_ost.stop()