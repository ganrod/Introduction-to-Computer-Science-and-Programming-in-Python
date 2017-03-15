def semordnilap(str1, str2):
    if len(str1) != len(str2):
        return False
    elif len(str1) == 0 and len(str2) == 0:
        return True
    elif str1[0] == str2[-1]:
        return semordnilap(str1[1:], str2[:-1])
    else:
        return False
        
print(semordnilap('stefan', 'nafets'))