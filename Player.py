import pygame
class Player():
    def __init__(self,x,y,sizeX,sizeY):
        self.rectangle = pygame.rect(sizeX,sizeY)