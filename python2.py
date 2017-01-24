def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """

    mylist = []
    
    for i in range(len(array)):
        if i%2 == 0:
            mylist.append(array[i])
 
    
    if len(mylist) == 0:
        Output = 0
        return Output
    elif len(mylist) > 0:
        sum_number = sum(mylist)
        array = array[-1]
        Output = sum_number*array
        print(Output)
        return Output
    
    



assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
assert checkio([6]) == 36, "(6)*6=36"
#assert checkio([]) == 0, "An empty array = 0"
assert checkio([-45]) == 2025
