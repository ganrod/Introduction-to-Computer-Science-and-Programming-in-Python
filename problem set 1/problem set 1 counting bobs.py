def countingBobs(s):

    n = 0

    for i in range(len(s)):
        if s[i:i+3] == 'bob':
            n += 1
        
    print 'Number of times bob occurs is: ' + str(n) 