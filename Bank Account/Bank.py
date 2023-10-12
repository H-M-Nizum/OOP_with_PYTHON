class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        
        
    def get_balance(self):
        print(f"\nAccount '{self.name}' created. \nBalance = ${self.balance:.2f}")
        
    
    def deposit(self, amount):
        self.balance += amount
        print('\nDeposit succesfully complete')
        self.get_balance()
        
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\n Sorry, account '{self.name}' only hase a balance of ${self.balance:.2f}"
            )
            
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print('\nWithdraw complete.')
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted : {error} 😁")
    
    def transfer(self, amount, account):
        try:
            print('\n***********\n\nBeginning Transer ... 🚀')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer complete! 👍')
        except BalanceException as error:
            print(f"\nTransfer interrupted! '❌ {error}")
            
class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance += (amount * 1.05) # 5% interested
        print('\nDeposit complete.')
        self.get_balance()
    
class SavingsAccount(InterestRewardsAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5
    
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance -= (amount + self.fee)
            print('\nWithdraw completed . ')
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")