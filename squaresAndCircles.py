'''Sophia Fisher
Chapter 2 - Python Loops
Adams - 7th period 
16 April 2019'''

import pygame, random
from pygame.locals import *

#class squaresAndCircles:
def drawSquares(window):
        # Create variables to keep track of size and position
    width = 100
    height = 100
    squareX = 0
    squareY = 0
    blue = (0,0,255)
    #pygame.draw.rect(window, blue, (squareX,squareY,width,height))
    # Use a loop to draw squares until the size is too small
    while((width>0) & (height>0)):
        pygame.draw.rect(window, blue, (squareX,squareY, width,height))
        squareX = squareX + width + 10
        squareY = squareY + 10
        width = width - 10
        height = height - 10
        pygame.display.update() 
            
    
    
        
        
def drawCircles(window):
        # Create variables to keep track of size, position and color
    radius = 100
    circleX = 300
    circleY = 300
    R = 99
    G = 209
    B = 62
    #green = (99,209,62)
    
    # Use a loop to draw circles until the size is too small
    while (radius > 0):
        color = (R,G,B)
        pygame.draw.circle(window, color, (circleX,circleY), radius)
        radius = radius - 10
        B = B - 25
        G = G - 25
        R = R - 25
        pygame.display.update() 
        
        if B < 0:
            B = 0
        
        if G < 0:
            G = 0
            
        if R < 0:
            R = 0
            
    radius2 = 70
    circleX2 = 500
    circleY2 = 400
    #randomizes color of circle
    R2 = random.randint(0,255)
    G2 = random.randint(0,255)
    B2 = random.randint(0,255)
    #green = (99,209,62)
    
    # Use a loop to draw circles until the size is too small
    while (radius2 > 0):
        color = (R2,G2,B2)
        pygame.draw.circle(window, color, (circleX2,circleY2), radius2)
        radius2 = radius2 - 10
        B2 = B2 - 25
        G2 = G2 - 25
        R2 = R2 - 25
        pygame.display.update() 
        
        if B2 < 0:
            B2 = 0
        
        if G2 < 0:
            G2 = 0
            
        if R2 < 0:
            R2 = 0
    
