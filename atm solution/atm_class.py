class ATM:
    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name = bank_name
        self.withdrawals_list = []

    def withdraw(self, request):
        print 'Welcome to', self.bank_name
        print 'Current balance =', self.balance
        self.seperator()

        if request > self.balance:
            print 'can\'t give you all the money !!'
        elif request <= 0:
            print 'invalid request'
        else:
            self.withdrawals_list.append(request)
            self.balance -= request  # getting balance before loop
            allowed_papers = [100, 50, 10, 5]
            for paper in allowed_papers:
                paper_number = int(request / paper)
                request -= paper * paper_number
                for i in range(paper_number):
                    print 'give', paper
            if request > 0:
                print 'give', request

        self.seperator()
        return self.balance

    def show_withdrawals(self):
        print '-' * 10, 'INVOICE', '-' * 10
        previous_balance = self.balance + sum(self.withdrawals_list)
        print 'Previous balance:', previous_balance

        for withdrawal in self.withdrawals_list:
            print 'withdrawal:', withdrawal

        print 'All withdrawals:', sum(self.withdrawals_list)
        print 'Current balance:', previous_balance - sum(self.withdrawals_list)
        self.seperator()

    def seperator(self):
    	print '=' * 35
