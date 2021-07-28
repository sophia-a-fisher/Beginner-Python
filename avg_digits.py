'''Sophia Fisher
Chapter 2 - Python loops
Adams - 7th period 
16 April 2019'''

while ( True ):
    # enter a number
    num = int(input("Enter a number :: "))

    sum = 0
    cnt = 0
    
    #add in a loop to avarage up all of the digits
    while(num>0):
        sum = sum + (num%10)
        num = num//10
        cnt = cnt + 1
    
    #print out the average
    print(sum/cnt)