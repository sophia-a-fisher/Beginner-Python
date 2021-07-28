'''Sophia Fisher
Chapter 1 - Ifs
Adams - 7th period
5 April 2019
'''
#import statements
import pygame
#from Wall import *
from pygame.locals import *


class Person:
    # set all class variables in the constructor
    def __init__(self, newX, newY):
        self.x = newX
        self.y = newY
        self.image = pygame.image.load("dude.gif")
       
        
    # draw your image
    def draw(self, window):
        #self.window = window
        #self.image.blit(window, (0,0))
            
            window.blit(self.image, (self.x,self.y))
    # move left unless you hit the edge
    def moveLeft(self):
        if (self.x > 0):
            self.x = self.x - 5
    
    # move right unless you hit the edge
    #the 500 is temporary for the right edge boundary!
    def moveRight(self):
        myRec = self.getRec()
        self.width = myRec[2]
        if  (self.x + self.width < 800):
            self.x = self.x + 5
        
    # move up unless you hit the edge
    def moveUp(self):
        if  (self.y > 0):
            self.y = self.y - 5
        
    # move down unless you hit the edge
    #the 500 is temporary for the bottom edge boundary!
    def moveDown(self):
        myRec = self.getRec()
        self.height = myRec[3]
        if (self.y + self.height < 600):
            self.y = self.y + 5
        
    
    
    # This will be filled out in 2.ifs_collide_lab. 
    # It will return True if your person has 
    # collided with another object
    def collide(self, other):
        # Get other's x, y, width and height
        othersRec = other.getRec()
        othersX = othersRec[0] 
        othersY = othersRec[1]
        othersWidth = othersRec[2]
        othersHeight = othersRec[3]
        
        # Get person's width and height
        personRec = self.getRec()
        #personsX = personRec.x 
        #personsY = personRec.y
        personsWidth = personRec[2]
        personsHeight = personRec[3]
        
        # check if person is to the right of the object
        #if othersX < self.x:
        # if self.x greater than (otherX + otherWidth)
        if (self.x) > (othersX + othersWidth):
            # person and object do not intersect
            return False
        
        
        # else check if the person is to the left of the object
        #else othersX > personsX:
        # elif(self.x + width) less than otherX
        elif (self.x + personsWidth) < othersX:
            # person and object do not intersect
            return False
        
        # elif person is above the object
        elif (self.y +personsHeight) < othersY:
            # person and object do not intersect
            return False
        
        # elif person is below the object
        elif (self.y) > (othersY + othersHeight):
            # person and object do not intersect
            return False
        
        
        # else
        else:
            return True
            # person and object do intersect
        
        #return False

    
    # DO NOT CHANGE THIS
    # This method returns a rectangle - (x, y, width, height) - that represents
    # the object
    def getRec(self):
        myRec = self.image.get_rect()
        return (self.x, self.y, myRec[2], myRec[3])
        
    
    
