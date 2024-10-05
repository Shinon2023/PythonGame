import pygame
from Main_Module import Module
from Game_window import Control_windows
from Operator import Operator
Module()
while True:
    Operator().Operator_audio()
    pygame.time.Clock().tick(30)
    Control_windows()
    pygame.display.flip()