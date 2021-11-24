coef = 1.2

def euro_to_usd ( amount ):
    return amount*coef

def usd_to_euro (amount):
    return amount/coef


print( euro_to_usd(1000) )
print( usd_to_euro(1200) )