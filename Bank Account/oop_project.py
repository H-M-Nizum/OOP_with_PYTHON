from Bank import *

kala = BankAccount(1000, '⬛◼️◾▪️kala▪️◾◾◼️⬛')
dola = BankAccount(2000, '🐻‍❄️🐻‍❄️Dola🐻‍❄️🐻‍❄️')

kala.get_balance()
dola.get_balance()

kala.deposit(500)

dola.withdraw(1000)
kala.withdraw(1000)

kala.transfer(999, dola)
dola.transfer(99, kala)

lala = InterestRewardsAcct(1000, '🔴🔴Lala🔴🔴')
lala.get_balance()
lala.deposit(100)

lala.transfer(100, kala)

mala = SavingsAccount(10000, '💢💢mala💢💢')
mala.get_balance()
mala.deposit(100)
mala.transfer(1000, kala)