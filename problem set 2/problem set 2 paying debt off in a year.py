def bankYear(balance, annualInterestRate):
    
    monthlyInterestRate = annualInterestRate/12
    newBalance = balance
    minPay = 10
    month = 1

    while newBalance > 0:
        minPay += 10
        newBalance = balance
        month = 1
        
        while month <= 12 and newBalance >0:
            newBalance -= minPay
            interest = monthlyInterestRate * newBalance
            newBalance += interest
            month += 1
            
    print 'Lowest Payment: ' + str(minPay)



bankYear(4773, 0.2)