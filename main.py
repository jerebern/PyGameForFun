import pygame
import Colors
import Tile
colors = Colors.Colors()
WINDOW_WIDTH = int(1024)
WINDOW_HEIGHT = int(768)
tileSize = int(32)
tiles = []

def drawTitle(window):
    for tile in tiles:
        tile.draw(window)
    
def initTile():
    posX = 0
    posY = 0
    for i in range(int(WINDOW_WIDTH/tileSize)) :
        for j in range(int(WINDOW_HEIGHT/tileSize)):
            tiles.append(Tile.Tile(posX,posY,tileSize,colors.GREEN))
            posY+=32
        posY=0
        posX+=32

def main():
    clock = pygame.time.Clock()
    exitWindow = False
    size = (WINDOW_WIDTH , WINDOW_HEIGHT)
    pygame.init()
    mainWindow = pygame.display.set_mode(size)
    initTile()
    while exitWindow == False : 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
               exitWindow = True 
        mainWindow.fill(colors.BLACK)
        drawTitle(mainWindow)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

main()
