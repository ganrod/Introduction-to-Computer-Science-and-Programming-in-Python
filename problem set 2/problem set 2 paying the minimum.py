def creditCard1(balance, annualInterestRate, monthlyPaymentRate):
    
    mir = 0
    mmp = 0
    mub = balance
    ubem = balance
    total = 0
    
    for i in range(12):
        mir = annualInterestRate/12
        mmp = ubem * monthlyPaymentRate
        mub = ubem - mmp
        ubem = mub + mir*mub

        print('Month: ' + str(i+1) + '\n' 'Minimum monthly payment: ' + str(round(mmp, 2)) + '\n' 'Remaining balance: ' + str(round(ubem, 2)))
        total = total + mmp
    
    print('Total paid: ' + str(round(total, 2)) + '\n' 'Remaining balance: ' + str(round(ubem, 2)))
        