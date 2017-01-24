class Friends:

    def __init__(self, connections):
        self.mylist = []
        self.connections = (connections)      
        for x in self.connections:
            self.mylist.append(set(x))

    def add(self, connection):
        self.connection = (connection)
        for node in self.mylist:
            x = node - self.connection
            if not x:
                return False 
        self.mylist.append(self.connection)
        return True

    def remove(self, connection):
        self.connection = (connection)
        for node in self.mylist:
            x = node - self.connection
            if len(x) == 0:
                self.mylist.remove(self.connection)
                return True 
        return False

    def names(self): 
        name = []
        for names in self.mylist:
            for x in names:
                if x not in name:
                    name.append(x)
        return set(name)             

    def connected(self, name):
        self.name = name
        connected = []
        unique = []
        for connection in self.mylist:
            for i, x in enumerate(connection):
                if x in self.name:
                    connected.append(connection)
        if connected == []:
            return set()

        for connected in connected:
            for x in connected:
                if x not in unique:
                    unique.append(x)
        unique.remove(self.name)       
        return set(unique)                             
        



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    f = Friends([{"And", "Or"}, {"For", "And"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert f.add({"Or", "And"}) is False
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"

