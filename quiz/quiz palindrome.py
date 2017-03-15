def isPalindrome(aString):
    '''
    aString: a string
    '''
    # Your code here
    b=len(aString)
    c=0
    for i in range(b):
        if aString[i]==aString[-(i+1)]:
            c=c+1
    if c==b:
        return True
    else:
        return False

print(isPalindrome('a'))