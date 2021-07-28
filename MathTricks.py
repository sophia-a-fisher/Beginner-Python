'''
Sophia Fisher
Chapter 1 - Python Intro
Adams - 7th period
28 March 2019
'''

class Trick:
    
    def trick1(self, givenNumber):
        self.number = givenNumber
        #self.answer = self.number * 2
        self.answer = self.number * 2
        self.answer = self.answer + 6 
        self.answer = self.answer / 2
        self.answer = self.answer - self.number
        return self.answer
    
    def trick2(self, number):
        self.number = number
        self.answer = self.number * 3
        self.answer = self.answer + 45
        self.answer = self.answer * 2
        self.answer = self.answer / 6
        self.answer = self.answer - self.number 
        return self.answer