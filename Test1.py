'''
Sophia Fisher
Chapter 1 - Python Intro
Adams - 7th period
27 March 2019
'''
#this class imitates a student object
class Student:
  
    studentName = ""
    studentAge = 0
    
    #this is the constructor initializing student's age and name
    def __init__(self, name, age):
        self.studentName = name
        self.studentAge = age
    
    #this method sets the student's name
    def setName(self, newName):
        self.studentName = newName
        
    #this method returns the stored student's name
    def getName(self):
        return self.studentName
        
    #this method sets the student's age
    def setAge(self, newAge):
        self.studentAge = newAge
        
    #this method returns the stored student's age
    def getAge(self):
        return self.studentAge
    
    #this method is for later
    def setNickname(self, nickname):
        pass