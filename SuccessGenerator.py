'''
Sophia Fisher
27 March 2019
'''
print("How many times do you have success in a week?")
successAWeek = int(input("Enter your answer here: "))
print("\nYou have success " , successAWeek, " times a week?")
successAMonth = successAWeek*4
if (successAWeek > 7):
    print("That means that you have success ", (successAMonth), " times a month!\nGood job! You are a VERY SUCCESSFUL person!")
if (successAWeek < 7):
    print("That means that you have success ", (successAMonth), " times a month!\nGood job! You are a SUCCESSFUL person!")