import re

def contain_alphanumeric(s):
    contain_numeric = False
    contain_alphabet = False
    for c in s:
        if (contain_alphabet and contain_numeric):
            return True

        if (c.isdigit()):
            contain_numeric = True
    
        if (c.isalpha()):
            contain_alphabet = True

    return False


def contain_special_chars(s, special_chars):
    regex = re.compile(special_chars)

    if (regex.search(s) == None):
        return False
    
    return True
