def f(s):
    return 'a' in s



def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    # Your function implementation here

    mList = []

    for a in range(len(L)):
        word = L[a]

        if f(word) == True:
            mList.append(word)

    L[:] = mList         # uncovers the global variable

    return len(L)

print satisfiesF(['a', 'b', 'a'])