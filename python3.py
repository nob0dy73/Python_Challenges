import re

def find_message(text):
    """Find a secret message"""

    pattern = '[A-Z]'
    trans = re.findall(pattern, text)
    trans2 = "".join(trans)
    print(trans2)
    
    return trans2
        	
        	
    
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"

