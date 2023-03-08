import pygame
import Colors
class Tile():
    def __init__(self,x,y,size,color):
        self.rectangle = pygame.Rect(size,size,size+size,size+size)
        self.rectangle.x = x
        self.rectangle.y = y
        self.color = color
    def draw(self,window):
        pygame.draw.rect(window,self.color,self.rectangle,0)

    