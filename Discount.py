'''Sophia Fisher
Chapter 1 - IFs 
Adams - 7th period 
5 April 2019'''

def getPrice( ann ):
    if ann > 2000:
        ann = ann - (ann*.1)
        return ann
    else:
        return ann

print ( getPrice( -11 ) ) 
print ( getPrice( 180 ) )
print ( getPrice( 2170 ) )
print ( getPrice( 3100 ) )
print ( getPrice( 9339 ) )
print ( getPrice( 2001 ) )

