def bisectionBank(balance, annualInterestRate):
    
    monthlyInterestRate = annualInterestRate/12
    newBalance = balance
    lowerBound = balance/12
    upperBound = (balance * (1 + monthlyInterestRate)**12) / 12
    epsilon = 0.01
    bisec = (upperBound + lowerBound)/2.0

    while abs(0 - newBalance) >= epsilon:
        newBalance = balance

        for month in range(0, 12):
            newBalance = round(((newBalance - bisec) * (1 + monthlyInterestRate)), 2)
        if (newBalance <= 0 and newBalance >= -0.01):
            break
        elif newBalance >= 0:
            lowerBound = bisec            
        else:
            upperBound = bisec

        bisec = (upperBound + lowerBound)/2.0
    print('Lowest Payment: ' + str(round(bisec, 2)))