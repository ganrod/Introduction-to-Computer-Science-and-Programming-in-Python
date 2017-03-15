def polysum(n, s):

    '''importing the set of mathematical functions'''
    import math

    ''' checks to see if input is valid, returns None if not'''
    if n<=0 or s<=0:
        return None
    
    '''calculations'''
    perimeter = n * s
    area = (0.25 * n * math.pow(s, 2))/(math.tan((math.pi)/n))

    result = area + math.pow(perimeter, 2)

    '''returns the result rounded to 4 decimal places'''
    return round(result, 4)