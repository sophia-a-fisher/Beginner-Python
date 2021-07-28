'''Sophia Fisher
Chapter 1 - Personal Example
Adams - 7th period 
4 April 2019'''

import sys, pygame, random

pygame.init()

pygame.init()

screen = pygame.display.set_mode((600,600))

white = (255,255,255)
screen.fill(white)

yellow = (255, 255, 0)
orange = (255, 69, 0)
green = (0, 255, 0)
red = (255, 0 , 0)
pink = (255,192,203)
black = (0,0,0)
purple = (128, 0, 128)
beige = (245, 222, 179)
beige2 = (230, 245, 230)

faceCoordinates = ((100,55), (400,55), (450,125), (450,175), (300,300), (200,300), (50,175), (50,125))
earCoordinates = ((100,55), (150,5), (200,55))
ear2Coordinates = ((400,55),(300,55), (350,5))
noseCoordinates = ((250,250),(225,225), (275,225))


pygame.draw.polygon(screen, beige, faceCoordinates, 5)
pygame.draw.polygon(screen, beige2, earCoordinates, 5)
pygame.draw.polygon(screen, black, ear2Coordinates, 5)
pygame.draw.polygon(screen, pink, noseCoordinates, 5)
pygame.draw.line(screen, black, (250,250), (210,265))
pygame.draw.line(screen, black, (210,265), (180,250))
pygame.draw.line(screen, black, (250,250), (290,265))
pygame.draw.line(screen, black, (290,265), (320,250))
pygame.draw.polygon(screen, black, )

pygame.display.update()

while (True):
    for event in pygame.event.get() :
         if ( event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
              pygame.quit(); 
              sys.exit();
