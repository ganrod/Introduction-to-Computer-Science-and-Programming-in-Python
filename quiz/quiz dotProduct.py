def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
    result = 0
    for i in range(len(listA)):
        result += listA[i] * listB[i]
    return result
    
print dotProduct([1, 2, 3, 4], [4, 5, 6, 7])