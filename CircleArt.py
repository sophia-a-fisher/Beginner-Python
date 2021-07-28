'''Sophia Fisher
Personal Project
18 April 2019'''

import pygame, random
from pygame.locals import *

def drawCircles(surface):
    
    #define some color variables
    #R = random.randint(180,255)
    #G = random.randint(43,150)
    #B = random.randint(0,77)
    R = random.randint(161,255)
    G = random.randint(0,50)
    B = random.randint(0,50)
    R2 = random.randint(0,63)
    G2 = random.randint(0,106)
    B2 = random.randint(129,255)
    X = random.randint(0,800)
    Y = random.randint(0,600)
    radius = random.randint(50,100)
    shading = random.randint(0,100)
   
    while ((radius > 0) & ((shading > 0) & (shading < 40))):
        
        color = (R,G,B)
        coordinate = (X,Y)
        pygame.draw.circle(surface, color, coordinate, radius)
        pygame.display.update()
        
        R = R + 25
        G = G + 25
        B = B + 25
        radius = radius - 10
        
        #make sure it won't crash
        if(R>255):
            R = 255
        if(G>255):
            G = 255
        if(B>255):
            B = 255
    
    while ((radius > 0) & ((shading > 40) & (shading < 80))):
        color = (R,G,B)
        coordinate = (X,Y)
        pygame.draw.circle(surface, color, coordinate, radius)
        pygame.display.update()
        
        R = R - 25
        G = G - 25
        B = B - 25
        radius = radius - 10
        
        #make sure it won't crash
        if(R<0):
            R = 0
        if(G<0):
            G = 0
        if(B<0):
            B = 0
    
    while ((radius > 0) & ((shading > 80) & (shading < 100))):
        color = (R2,G2,B2)
        coordinate = (X,Y)
        pygame.draw.circle(surface, color, coordinate, radius)
        pygame.display.update()
        
        R2 = R2 - 25
        G2 = G2 - 25
        B2 = B2 - 25
        radius = radius - 10
        
        #make sure it won't crash
        if(R2<0):
            R2 = 0
        if(G2<0):
            G2 = 0
        if(B2<0):
            B2 = 0
        
        
        
    
    
    

