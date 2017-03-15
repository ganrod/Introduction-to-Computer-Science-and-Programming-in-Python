def available(letters):
    import string
    lowcase = string.ascii_lowercase
    value = ''
    str1 = ''
    
    for char in lowcase:
        if char not in letters:
            value = char
        else:
            value = ''
        str1 += value
    return str1
    
print available(['e', 'i', 'k', 'p', 'r', 's'])