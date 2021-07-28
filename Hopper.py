'''Sophia Fisher
Chaper 1 - Python Gaming
Adams - 7th period 
6 April 2019'''

import pygame
from pygame.locals import *

class Hopper:
    # initialize all variables
    def __init__(self, newX, newY):
        self.x = newX
        self.y = newY
        self.up = False
        self.upCounter = 0
        self.img = pygame.image.load("dudeR.gif")
    
    # draw hopper
    def draw(self, window):
        window.blit(self.img, (self.x,self.y))
        
        
    # move left unless you hit the edge
    def moveLeft(self):
        if (self.x > 0):
            self.x = self.x - 5
        
    # move left unless you hit the edge 
    def moveRight(self):
        myRec = self.getRec()
        self.width = myRec[2]
        if  (self.x + self.width < 800):
            self.x = self.x + 5
    
    # This DOES NOT change self.y
    # sets self.up to True if the self.up variable is False and self.upCounter is 0
    def moveUp(self):
        if self.up == False and self.upCounter == 0:
            self.up = True
        
    
    # moves hopper up or down based on the values
    # of self.up and self.upCounter
    def update(self):
        # if up is true
        if self.up == True:
            # move hopper up
            self.y = self.y - 30
            # increase upCounter
            self.upCounter += 1
            # if hopper has moved up a number of times
            if self.upCounter > 3:
                # set up to false
                self.up = False

                # else if upCounter is greater than 0
        elif self.upCounter > 0:
                # move hopper down
            self.y = self.y + 30
                # decrease upCounter
            self.upCounter = self.upCounter - 1
        
    
    
    # determine if hopper has collided with an object 
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

    
    # DO NOT CHANGE THIS
    # This method returns a rectangle - (x, y, width, height) - that represents
    # the object
    def getRec(self):
        myRec = self.img.get_rect()
        return (self.x, self.y, myRec[2], myRec[3])
