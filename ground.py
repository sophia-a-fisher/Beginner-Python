'''Sophia Fisher
Chapter 2 - Lists
Adams - 7th period
30 April 2019'''

import pygame, random
from pygame.locals import *

def drawGround(window):
    """
    load all images into a list 
    """
    imageList = [pygame.image.load("grass.gif"), pygame.image.load("gtoroad.gif"), pygame.image.load("road.gif"), pygame.image.load("rtograss.gif"), ]
    
    """
    Create variables to keep track of where to
    draw the grass
    """
    x = 0
    y = 0
    
    """
    Outer loop runs as long as x is 
    not past the right edge of the screen
    """
    while x <= (750):
        
        """
        Inner loop runs as long as y is 
        not past the bottom edge of the screen
        Use the y position to determine which tile to draw
        Increase the y
        """
        while y <= 550:
            if (y <= 50):
                window.blit(imageList[0], (x,y))
            elif (y == 100):
                window.blit(imageList[1], (x,y))
            elif (y <= 450):
                window.blit(imageList[2], (x,y))
            elif (y == 500):
                window.blit(imageList[3], (x,y))
            else :
                window.blit(imageList[0], (x,y))
            y = y + 50
        y = 0
            
        x = x + 50
        
            
        """
        Increase the x and reset the y
        """
 
