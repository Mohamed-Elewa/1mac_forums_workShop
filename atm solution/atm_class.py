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
            allowed_papers = [100, 50, 10, 5]
            for paper in allowed_papers:
                paper_number = request / paper
                request -= paper * paper_number
                for i in range(paper_number):
                    print 'give', paper
            if request > 0:
                print 'give', request

        print '=' * 35
        return self.balance
