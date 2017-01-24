

def place_pawns(pawns):
    
    pawns_indexes = set()
    for p in pawns:
        row = int(p[1]) - 1
        col = ord(p[0]) - 97
        pawns_indexes.add((row, col))
    print(pawns_indexes)
    return pawns_indexes    
    #row - 1, col - 1 and col + 1   


def safe(loc_pawns):
    
    count = 0
    for row, col in loc_pawns:
        is_safe = ((row - 1, col - 1) in loc_pawns) or ((row - 1, col + 1) in loc_pawns)
        if is_safe:
            count += 1
    print(count)
    return(count)


def safe_pawns(pawns):

    loc_pawns = place_pawns(pawns)
    count = safe(loc_pawns)
    return count
    
    

    



    











if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1

