def countingVowels(s):

    vowels = 0    

    for char in 'aeiou':
        lows = s.lower()
        vowels += lows.count(char)
            
    return 'Number of vowels: ' + str(vowels)