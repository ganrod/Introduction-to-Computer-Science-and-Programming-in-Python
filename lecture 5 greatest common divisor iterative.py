def gcdIter(a, b):
    min = a
    if min > b:
        min = b
    while min > 1:
        if a%min == 0 and b%min == 0:
            return min
        else:
            min -= 1

print(gcdIter(8, 12))