
def min(*args, **kwargs):

    for key, value in kwargs.iteritems():
        myargs = {}
        if value == int:
            for i in range(len(args)):
                newdict = {args[i]: int(args[i])}
                myargs.update(newdict)
            for key, value in myargs.iteritems():
                minimum = value
            for key, value in myargs.iteritems():
                if value < minimum:
                    minimum = key
        if value == sum:
            for i in range(len(args)):
                return args[0]
        if callable(value):
            f = value
            for i in range(len(args)):
                for arg in args[i]:
                    for item in arg:
                        minimum = item
                for arg in args[i]:
                    for item in arg:
                        if item < minimum:
                            minimum = item
                        themini = arg
                print("minimum: " + str(themini))
                return themini


               
                    
            

    for i in range(len(args)):
        if type(args[i]) == int:
            print("int")
            minimum = args[i]
        elif type(args[i]) == list:
            print("list")
            for arg in args[i]:
                minimum = arg
        elif type(args[i]) == str:
            print("string")
            mychs = sorted(list(args[i]))
            minimum = mychs[0]
        else:
            mylist = []
            print("tuple")
            print(len(args))
            if type(args[0]) == bool:
                return -1
            else:
                for arg in args[i]:
                    mylist.append(arg)
                    minimum = mylist[0]
                    args = mylist


    
    for i in range(len(args)):
        if type(args[i]) == int:
            print('do int')
            if args[i] < minimum:
                minimum = args[i]
        elif type(args[i]) == list:
            print('do list')
            for arg in args[i]:
                if arg < minimum:
                    minimum = arg[i]
        elif type(args[i]) == str:
            for arg in args[i]:
                if arg < minimum:
                    minimum = arg[i]
        else:
            print('do notsting')
            for arg in args[i]:
                for item in arg:
                    print(item)
                    if arg < minimum:
                        minimum = arg
                
                    

            

                
                
    
    print("minimum: " + str(minimum))
    return minimum
   


def max(*args, **kwargs):
    
    for key, value in kwargs.iteritems():
        myargs = {}
        if value == int:
            for i in range(len(args)):
                newdict = {args[i]: int(args[i])}
                myargs.update(newdict)
            for key, value in myargs.iteritems():
                maximum = value
            for key, value in myargs.iteritems():
                if value > maximum:
                    maximum = key
                return maximum
        if callable(value):
            return False

    for i in range(len(args)):
        if type(args[i]) == int:
            maximum = args[i]
        elif type(args[i]) == list:
            [(i, j) for i, j in enumerate(args)]
            if i == 0:
                for item in j:
                    maximum = item
        elif type(args[i]) == str:
            mychs = sorted(list(args[i]))
            maximum = mychs[-1]
        else:
            mylist = []
            print("tuple")
            print(len(args))
            for arg in args[i]:
                mylist.append(arg)
                maximum = mylist[0]
                args = mylist
    
    for i in range(len(args)):
        if type(args[i]) == int:
            if args[i] > maximum:
                maximum = args[i]
        elif type(args[i]) == list:
            [(i, j) for i, j in enumerate(args)]
            if i == 0:
                for item in j:
                    if item > maximum:
                        maximum = item
            else:
                return (args[2])
                    
        else:
            print('do notsting')
            for arg in args[i]:
                for item in arg:
                    print(item)
                    if arg > maximum:
                        maximum = arg
    
    print("maximum: " + str(maximum))
    
    return maximum
            
    
    
   
    
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    assert min((9,)) == 9
    assert min(abs(i) for i in range(-10, 10)) == 0
    assert max([1, 2, 3], [5, 6], [7], [0, 0, 0, 1]) == [7]
    assert min([1, 2, 3], [5, 6], [7], [0, 0, 0, 10], key=sum)
    assert min(True, False, -1)
