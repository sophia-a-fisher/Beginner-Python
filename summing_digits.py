'''Sophia Fisher
Chapter 2 - Python Loops
Adams - 7th period
16 April 2019'''
while ( True ):
    # enter a number
    num = int(input("Enter a number :: "))

    sum = 0
    
    #add in a while loop 
    while(num>0):
       #sum digit
       sum = sum + (num%10)
       #chop off right most digit
       num = num//10
       
    print("The sum of your digits is:", sum)