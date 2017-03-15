def guess(secretW, lett):
    for char in secretW:
        if char not in lett:
            return False
    return True


print guess('apple', ['a', 'p', 'l', 'e'])