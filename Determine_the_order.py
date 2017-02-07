from collections import deque

def checkio(data):


    phrases = []
    for word in data:
        a = list(word)
        phrases.append(a)

    neighbours = []
    for word in phrases:
        for i in range(len(word)):
            if i < (len(word) - 1):
                neighbours.append([(word[i]), (word[i+1])])
    
    unique_ch = set()
    for word in phrases:
        for ch in word:
            unique_ch.add(ch)
    print unique_ch

    mylist = deque([neighbours[0]])
    unique_nei = set()
    for neighbour in mylist:
        for ch in neighbour:
            unique_nei.add(ch)

    while unique_ch != unique_nei:
        for neighbour in neighbours:
            if neighbour in mylist:
                break
            elif neighbour[0] in mylist[-1][1]:
                mylist.append(neighbour)
            elif neighbour[1] in mylist[0][0]:
                mylist.appendleft(neighbour)
            
            
def parse(neighbours, start, path):
    


    print mylist

    


    
            






#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(["acb", "bd", "zwa"]) == "zwacbd", \
        "Just concatenate it"
    assert checkio(["klm", "kadl", "lsm"]) == "kadlsm", \
        "Paste in"
    assert checkio(["a", "b", "c"]) == "abc", \
        "Cant determine the order - use english alphabet"
    assert checkio(["aazzss"]) == "azs", \
        "Each symbol only once"
    assert checkio(["dfg", "frt", "tyg"]) == "dfrtyg", \
        "Concatenate and paste in"
