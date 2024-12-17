import pygame
from src.Main_Module import Module
from src.Game_window import Control_windows
from src.Operator import Operator

Module()

while True:
    Operator().Operator_audio()
    pygame.time.Clock().tick(30)
    Control_windows()
    pygame.display.flip()