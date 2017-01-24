from math import sqrt

def checkio(opacity):

    listfib = []
    age_opacity = {}
    op = 10000
    
    for n in xrange(100):
        listfib.append(int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))))
        
    for year in xrange(5000):
        if year in listfib:
            op = op - year
            age_opacity[op] = year
        else:
            op = op + 1
            age_opacity[op] = year

    print(age_opacity[opacity])
    return(age_opacity[opacity])
            
    

#opacity = 10000 - fibonacci number if year is equal to fibonacci number

#opaity = 10000 + 1




#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"
