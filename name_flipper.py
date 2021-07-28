'''Sophia Fisher
Chapter 2 - Python Strings
Adams - 7th period
23 April 2019'''

def flip_em( s ):   
    #add in code to flip the names
    spaceLocation = s.find(" ")
    firstName = s[(spaceLocation+1):(len(s))]
    lastName = s[0:(spaceLocation)]
    string = firstName + ", " + lastName
    print(string)
    #and add in a comma between the flipped names
    

print ( flip_em("aplus comp") )
print ( flip_em("comp aplus") )
print ( flip_em("ben sam") )
print ( flip_em("sally sue") )
print ( flip_em("big man") )
print ( flip_em("fat head") )
