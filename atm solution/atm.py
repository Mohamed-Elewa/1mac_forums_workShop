def withdraw(balance, request):
    print 'Current balance = ', balance
    if request > balance:
        print "can't give you all the money !!"
    elif request <= 0:
        print 'invalid request'
    else:
        balance -= request  # getting ballance before loop
        allowed_values = [100, 50, 10, 5]
        i = 0
        while i < len(allowed_values) and request > 0:
            if request < allowed_values[i]:  # get next index in list
                i += 1
            else:
                request -= allowed_values[i]
                print 'give', allowed_values[i]
        if request > 0:  # checking request after loop
            print 'give', request
    return balance


balance = 500
balance = withdraw(balance, 277)
balance = withdraw(balance, 30)
balance = withdraw(balance, 5)
balance = withdraw(balance, 500)
