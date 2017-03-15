def isIn(char, aStr):
    if aStr == '':
        return False
    elif len(aStr) == 1 and char != aStr:
        return False
    elif len(aStr) == 1 and char == aStr:
        return True
    elif char == aStr[len(aStr)/2]:
        return True
    elif char < aStr[len(aStr)/2]:
        return isIn(char, aStr[:len(aStr)/2])
    else:
        return isIn(char, aStr[len(aStr)/2:])

print(isIn('s', 'aefnst'))