class ATM:
    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name = bank_name

    def withdraw(self, request):
        print 'Welcome to', self.bank_name
        print 'Current balance =', self.balance
        print '=' * 35

        if request > self.balance:
            print 'can\'t give you all the money !!'
        elif request <= 0:
            print 'invalid request'
        else:
            self.balance -= request  # getting balance before loop
            allowed_values = [100, 50, 10, 5]
            i = 0
            while i < len(allowed_values):
                if request < allowed_values[i]:  # get next index in list
                    i += 1
                else:
                    request -= allowed_values[i]
                    print 'give', allowed_values[i]
            if request > 0:  # checking request after loop
                print 'give', request

        print '=' * 35
        return self.balance
