'''
Sophia Fisher
Chapter 1 - Python Intro
Adams - 7th period 
28 March 2019
'''
from Lab33 import *

mathTrick = Trick()
number = int(input("Enter a number less than 10: "))
print("Your answer is: " , mathTrick.trick1(number))
    
number2 = int(input("Enter a number: "))
print("Your answer is: ", mathTrick.trick2(number2))