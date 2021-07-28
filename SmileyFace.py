
'''Sophia Fisher
Chapter 1 - Smiley Face Activity
Adams - 7th period 
2 April 2019'''

import pygame
import sys
from math import pi


pygame.init()

screen = pygame.display.set_mode((640,480))

white = (255,255,255)
screen.fill(white)

yellow = (255,255,0)
orange = (255,69,0)
green = (0, 255, 0)
red = (255, 0 , 0)

# draw a smiley face

# draw eyes
pygame.draw.circle(screen, yellow,(200,100), 50, 10)
pygame.draw.circle(screen, yellow,(350,100), 50, 10)
# draw a nose

# draw a mouth

# update the screen
pygame.display.update()

while (True):
    for event in pygame.event.get() :
         if ( event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
              pygame.quit(); 
              sys.exit();


