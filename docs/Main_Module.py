import pygame

class Module():
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1280, 720))
        self.base_font = pygame.font.Font('font\Pixeboy-z8XGD.ttf', 32)
        self.big_font = pygame.font.Font('font\Pixeboy-z8XGD.ttf', 200)
        pygame.display.set_caption('Sword Art Online')
        self.event = pygame.event.poll()
