'''Sophia Fisher
Chapter 2 - Python Strings
Adams - 7th period
23 April 2019'''

'''the program will accept two variables: the first a string and the second
a integer that will represent the distance from the letter in the string 
for the new encrypted string'''

def cipher( s, dist ):
    #variable declarations
    alphabetString = "abcdefghijklmnopqrstuvwxyz"
    x = 0
    #y = 0
    newString = ""
    #found = "false"
    
    #loop through all letters in argument
    while (x < len(s)):
        y = 0
        #loop through all letters in alphabet
        while ((y < len(alphabetString))):
            #if the letter in argument is the same as the letter in the alphabet
            if (s[x] == alphabetString[y]):
                #set a variable to the letter in alphabet
                #letterCharacter = alphabetString[y]
                #set a variable to the index of the letter
                #calculate the new letter index
                newIndex = y - dist
                #set variable to the new letter at new index
                newString = newString + alphabetString[newIndex]
                #debugging
                #print(newString)
        
            y = y + 1
            #print("y = ",y)
        
        
        x = x + 1
   
    return newString
        #print("x = ",x)
        

print( cipher("abcdef", 1) )
print( cipher("abcdef", 2) )
print( cipher("abcdef", 3) )
print( cipher("dogcatpig", 1) )
print( cipher("dogcatpig", 3) )

