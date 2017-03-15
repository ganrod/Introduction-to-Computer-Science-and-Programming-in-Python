def debtYear(balance, annualInterestRate):

    minPay = 10
    monthlyInterestRate = annualInterestRate / 12
    newBalance = balance

    while newBalance > 0:

        for month in range(12):
            newBalance = (newBalance - minPay) * (1 + monthlyInterestRate)

            if newBalance <= 0:
                break

        if newBalance <= 0:
            print('Lowest Payment: ' + str(minPay))
        else:
            minPay += 10
            newBalance = balance


debtYear(4773, 0.2)