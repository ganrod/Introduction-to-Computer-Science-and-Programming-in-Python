def userGuess(secret, letters):
    value = ''
    string = ''
    
    for char in secret:
        if char in letters:
            value = char + ' '
        else:
            value = '_ '
        string += value
    return string

print userGuess('apple', ['e', 'i', 'k', 'p', 'r', 's'])