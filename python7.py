def checkio(number):

    if number > 10**6:
        return 0
    a = number
    b = str(a)
    c = []
    
    for digit in b:
        if digit == "0":
            continue
        else:
            c.append (int(digit))
    
    print(reduce(lambda x, y: x*y, c))
    return reduce(lambda x, y: x*y, c)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1

