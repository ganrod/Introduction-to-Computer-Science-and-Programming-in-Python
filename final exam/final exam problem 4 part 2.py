def longestRun(L):
    size = 1
    max_size = 1

    for i in range(len(L)-1):
        if L[i+1] >= L[i]:
           size += 1
        else:
            size = 1
        if size > max_size:
            max_size = size

    return max_size

print longestRun([0])