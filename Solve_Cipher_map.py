
def map_cipher(cipher_grille):

    coords_of_X = []
    xcoord_of_X = -1

    for string in (list(cipher_grille)):
        for key, value in enumerate(string):
            if key == 0:
                xcoord_of_X += 1
            if value == 'X':
                coordinate = (xcoord_of_X, key)
                coords_of_X.append(coordinate)
                
    print(coords_of_X)
    return coords_of_X


def get_passphrase(ciphered_password, coords_of_X):

    get_passphrase = ''
    xcoord_of_ch = -1

    for i in range(len(ciphered_password)):
        for j in range(len(ciphered_password[i])):
            for key, value in coords_of_X:
                if (i, j) == (key, value):
                    get_passphrase = get_passphrase + (ciphered_password[i][j])
                        
    print(get_passphrase)
    return get_passphrase
    
    
def map_rotate(cipher_grille):

    new_grille = []
    size = len(cipher_grille)
    for row in range(size):
        newrow = []
        for col in range(size):
            newrow.append(cipher_grille[size - col - 1][row])
        new_grille.append(newrow) 
    for item in new_grille:
        print(item)
    return new_grille


def recall_password(cipher_grille, ciphered_password):
           
    for item in cipher_grille:
        print(item)          
    passphrase = ""            
    for i in range(0,4):
        coords_of_X = map_cipher(cipher_grille)      
        passphrase = passphrase + get_passphrase(ciphered_password, coords_of_X)
        cipher_grille = map_rotate(cipher_grille)
    
    print(passphrase)
    return passphrase
    
        
        








if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'

