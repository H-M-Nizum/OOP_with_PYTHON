class BalanceException(Exception):
    pass
class User:
    Total_balance = 10000000000
    Total_loan_amount = 0
    loan_feature = True
    Bank_account = {}
    def __init__(self, name, email, address, account_type) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account = self.account_type + str(len(self.name)) + self.name
        self.transaction_history = []
        self.count_loan = 0
        
    
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\n Sorry, account '{self.name}' only hase a balance of ${self.balance:.2f}"
            )
            
    def check_balance(self):
        print(f"\nAccount '{self.name}' created. Balance = ${self.balance:.2f}")
        
    
    def deposit(self, amount):
        self.balance += amount
        User.Total_balance += amount
        print('\nDeposit succesfully complete')
        self.check_balance()
        self.transaction_history.append(amount)
    
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            User.Total_balance -= amount
            print('\nWithdraw complete.')
            self.transaction_history.append(amount * (-1))
            self.check_balance()
        except BalanceException as error:
            print(f"\nWithdrawal amount exceeded : {error} 🥲")
    
    def transfer(self, amount, account):
        try:
            print('\n***********\n\nBeginning Transer ... 🚀')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer complete! 👍')
        except BalanceException as error:
            print(f"\nTransfer interrupted! '❌ {error}")
    
    def loan(self):
        if User.loan_feature == True:
            self.count_loan += 1
            if self.count_loan < 3:
                loan = int(input('How much need your loan: '))
                if loan <= User.Total_balance:
                    print('Your loan accepted.')
                    self.deposit(loan)
                    User.Total_balance -= loan
                    User.Total_loan_amount += loan
                else:
                    print('Sorry This amount of money has not the Bank. Bank is.\n')
            else:
                print('You can not take loan more then 2 time\n')
        else:
            print('Now loan option are not available')
            
    def deatils(self):
        print(f"Oner name : {self.name} email : {self.email} address : {self.address} Account type : {self.account_type} current balance : {self.balance} current loan: {self.count_loan}")
        print(self.transaction_history)
        
        