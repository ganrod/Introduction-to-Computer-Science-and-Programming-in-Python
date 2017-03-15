def f(a,b):
    return a > b


def dict_interdiff(d1, d2):
    '''
   d1, d2: dicts whose keys and values are integers
   Returns a tuple of dictionaries according to the instructions above
   '''
    # Your code here
    intersect = {}
    for key in d1.keys():
        if d2.has_key(key):
            intersect[key] = f(d1[key], d2[key])
   
    diff = {}
    # Check all keys in first dict
    for key in d1.keys():
        if (not d2.has_key(key)):
            diff[key] = d1[key]
        
    # Check all keys in second dict to find missing
    for key in d2.keys():
        if (not d1.has_key(key)):
            diff[key] = (d2[key])
   
    return intersect,diff
 
d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}      
print(dict_interdiff(d1, d2))