'''Sophia Fisher
Chapter 2 - Lists
Adams - 7th period
30 April 2019'''

import pygame, random
from enemy import *

class enemies:
    def __init__(self):
        self.myList = [enemy(0,200,25),
                       enemy(750,270,-25),
                       enemy(150,340,25),
                       enemy(550,410,-25)]
        
        self.changedrecs = []
        
    def drawAndCollision(self, screen, guy, changedrecs):
        """ Loop through the list of enemies """
        for i in range (len(self.myList)):
            """  if guy collides with any enemies, return True  """
            if guy.collide(self.myList[i]):
                return True
            #we ended here!!!
            
        
        
            """ Add the old position of the enemy to the array of rectangles to be redrawn  """
            self.changedrecs.append(self.myList[i].getRec())
        
        
            """  Move and draw the enemies  """
            self.myList[i].move()
            self.myList[i].draw(screen)
            
            
            """ Add the old position of the enemy to the array of rectangles to be redrawn  """
            self.changedrecs.append(self.myList[i].getRec())
            
            
            """  If the enemy has gone off the screen, remove it  """
            getRecTuple = self.myList[i].getRec()
            if (self.myList[i].getRec().x > 800):
                self.myList.remove(i)

    
        return False
          
          
    """ create a new enemy and add it to the list of enemies """  
    def addEnemy(self, x, y, speed):
        1/1
       
    
    """ Return the length of the list of enemies """
    def numEnemies(self):
        return 1
