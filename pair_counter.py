'''Sophia Fisher
Chapter 2 - Python Strings
Adams - 7th period
23 April 2019'''

def count_pairs( s ):
  #add in code to count 

  repeatingCounter = 0
  x = 0
  while (x < len(s)):
      character1 = ""
      character2 = "" 
      if (len(s) < 2):
          repeatingCounter = 0
          return repeatingCounter
      character1 = s[x]
      character2 = s[(x+1)]
      if (character1 == character2):
          repeatingCounter = repeatingCounter + 1
      x = x + 1   
      #print(repeatingCounter)
      if (x == (len(s) - 1)):
        return repeatingCounter    
      
      
  #how many pairs of letters exist
  #return the number of letter pairs in each string
  #aadogbbcatcc would return 3
  #aadogcatcc would return 2
  return 0

print ( count_pairs("ddogccatppig") )
print ( count_pairs("dogcatpig") )
print ( count_pairs("xxyyzz") )
print ( count_pairs("a") )
print ( count_pairs("abc") )
print ( count_pairs("aabb") )
print ( count_pairs("dogcatpigaabbcc") )
print ( count_pairs("aabbccdogcatpig") )
print ( count_pairs("dogabbcccatpig") )
print ( count_pairs("aaaa") )
print ( count_pairs("AAAAAAAAA") )
