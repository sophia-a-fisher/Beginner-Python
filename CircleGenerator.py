'''Sophia Fisher
Personal Project
18 April 2019'''

#import statements!
import pygame, random, sys
from pygame.locals import *
from CircleArt import*

#initialize the pygame
pygame.init()
#create a surface object
surface = pygame.display.set_mode((800,600))
#color variable
white = (255,255,255)
surface.fill(white)

#call the draw method

for x in range (30):
    drawCircles(surface)


#update the display
pygame.display.update()


while True:
    for event in pygame.event.get():
        # Check if the user closed the window
        if event.type==QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type==KEYDOWN:
            if event.key==K_UP: 
                surface.fill(white)
                for x in range (30):
                    drawCircles(surface)


