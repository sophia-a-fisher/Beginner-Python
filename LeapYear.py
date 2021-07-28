'''Sophia Fisher
Chapter 1 - If Statements
Adams - 7th period 
5 April 2019
'''

year = int(input("Enter a year: "))

if (year%4 == 0) or (year%400 == 0):
    print(year,"is a leap year")
    
else:
    print(year,"is NOT a leap year")
