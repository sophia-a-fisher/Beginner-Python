'''
Sophia Fisher
JAdams Python - Chapter 1
Adams - 7th period
Created on Mar 14, 2019
'''

#I can write comments

#printing out Hello World and using carriage things
print("hello world!\n")
print('\"hello world! Again!\"')

#creating Strings
message = "Python is a language"
print(message)
firstName = "Sophia"
print(firstName)

#messing around with String methods
print(firstName.title())
nameLength = len(firstName)
print(nameLength)
print(firstName.find("o"))
print(firstName.rfind("o"))

#String concatenation
adjective = "happy"
pet = "cat"
petDescription = adjective + " " + pet
print(petDescription)
print(petDescription.title())

#playing with integers
print(1)
print(1+3)
print(1/2)
number = 3
print(number/2)
secondNumber = 3/2
print(secondNumber)
expression = (1+2/2)**2 #should return 4 according to operator precedence
print(expression)

