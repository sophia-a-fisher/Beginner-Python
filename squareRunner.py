'''Sophia Fisher
Chapter 2 - Python Loops
Adams - 7th period 
16 April 2019'''

import pygame, sys
from pygame.locals import *
from squaresAndCircles import* 

pygame.init()
screen = pygame.display.set_mode((800,600))

#Colors the screen white
WHITE = (255, 255, 255)
screen.fill(WHITE)


# calls the method draw scene and sends it the screen to draw on
#WORK ON THIS NEXT TIME
drawSquares(screen)
drawCircles(screen)
  
pygame.display.update()


while True:
    for event in pygame.event.get():
        # Check if the user closed the window
        if event.type==QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
            pygame.quit()
            sys.exit()
