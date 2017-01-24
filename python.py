def index_power(array, n):
    """
        Find Nth power of the element with index N.
    """
    
    for i in range(len(array)):
        if array[i] < 0 and array[i] <= 100:
            Output = "Fails Precondition"
            return Output
            
           
    
    if len(array) <= -1 and len(array) >=10:
        Output = "Fails Precondition"
        return Output
    elif n <= -1:
        Output = "Fails Precondition"
    elif n >= len(array):
        Output = -1
        print("IndexError")
        return Output
    elif n == 0:
        Output = 1
        print("Zero power")
        return Output
    elif n < len(array):
        array_number = array[n]
        Output = array_number**n
        print(Output)
        return Output
        
    
    


assert index_power([1, 2, 3, 4], 2) == 9, "Square"
assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
assert index_power([0, 1], 0) == 1, "Zero power"
assert index_power([1, 2], 3) == -1, "IndexError"
assert index_power([96,92,94],3) == -1, "IndexError"
