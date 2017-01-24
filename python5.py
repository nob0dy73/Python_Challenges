
def checkio(*args):
    mylist = []
    if args and len(args) <= 20:
        for arg in args:
            if arg > 100 and arg < -100:
                return 0
	        else:
	            mylist.append(arg)
	            
        largest = max(mylist)
        smallest = min(mylist)
        get_value = largest - smallest	
        print(get_value)
        return get_value
    else:
        return 0

    
    
    
    
    
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(checkio(1, 2, 3), 2, 3), "3-1=2"
    assert almost_equal(checkio(5, -5), 10, 3), "5-(-5)=10"
    assert almost_equal(checkio(10.2, -2.2, 0, 1.1, 0.5), 12.4, 3), "10.2-(-2.2)=12.4"
    assert almost_equal(checkio(), 0, 3), "Empty"

