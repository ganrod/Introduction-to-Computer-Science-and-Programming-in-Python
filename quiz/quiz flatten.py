def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    for element in aList:
        if aList == []:
            return aList
        if (str(type(element) == 'list')):
            return flatten(element) + flatten(element[1:])
        return aList[:1] + flatten(aList[1:])

print flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5])