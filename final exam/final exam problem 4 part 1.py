def getSublists(L, n):
    newL = []
    for i in range(len(L)):
        testList = L[i:i+n]
        if (len(testList) == n):
            newL.append(L[i:i+n])
        else:
            return newL
    return newL
    
print getSublists([10, 4, 6, 8, 3, 4, 5, 7, 7, 2], 4)