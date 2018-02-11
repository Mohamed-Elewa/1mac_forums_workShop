from atm_class import *

balance1 = 500
balance2 = 1000

atm1 = ATM(balance1, "Smart Bank")
atm2 = ATM(balance2, "Baraka Bank")

atm1.withdraw(277.5)
# atm1.withdraw(800)
atm1.withdraw(120)
atm1.show_withdrawals()

atm2.withdraw(100)
# atm2.withdraw(2000)
atm2.withdraw(560)
atm2.withdraw(25)
atm2.show_withdrawals()
