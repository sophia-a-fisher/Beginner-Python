'''Sophia Fisher
Chapter 2 - Python Loops
Adams - 7th period 
16 April 2019'''

import pygame

# Ask user for number of seconds
seconds = int(input("How many seconds?"))
minutes = 0

# Loop while seconds are greater than or equal to 0
while (seconds >= 0):
    print(seconds)
    # Part 1 - Print the time left as seconds
    # Part 2 - Print the time left as minutes and seconds
    minutes = minutes + seconds//60
    print(minutes, ":", seconds)
    seconds = seconds - 1
    pygame.time.wait(1000)