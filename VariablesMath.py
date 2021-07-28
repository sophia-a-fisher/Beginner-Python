'''
Sophia Fisher
Chapter 1 - Intro to Python
Adams - 7th period
28 March 2019
'''

currentYear = int(input("Enter the year: "))
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("\n", name, "is", age, "years old!")
print(name, "was born in", currentYear - age, "!")

int1 = int(input("\nPlease enter an integer: "))
int2 = int(input("Please enter another integer: "))
decimal1 = float(input("Please enter a decimal number: "))

print("\nThe result of" , int1, "*" , int2, "is", int1*int2)
print("The result of", int1, "*", int2, "*", decimal1, "is", int1*int2*decimal1)
print("The result of", int1, "% 2 is", int1%2)
print("The result of", int2, "% 2 is", int2%2)
print("The result of", decimal1, "% 2 is", decimal1%2)
