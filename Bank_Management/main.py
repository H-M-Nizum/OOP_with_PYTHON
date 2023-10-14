from user import *

flag = True
while flag:
    print('\nWelcome our Bank ________ you can try any option_\n')
    print('1. Users (press1) \n2. Admin (press 2) \n3.Exist (press any key)\n')
    n = int(input('Enter your ans: '))
    # User.Bank_account = {}
    if n==1:
        flag1 = True
        while flag1:
            print('\nHow can i helap you_____\n')
            print('1. Create an account \n2. Your own account \n3.Exist (press any key)\n')
            
            a = int(input('Enter your option : '))
            
            if a == 1:
                flag2 = True
                nam = input('Enter your name: ')
                email = input('Enter your email account: ')
                address = input('Enter your address: ')
                account_type = input('Enter your account type: ')
                print()
                acc = User(nam, email, address, account_type)
                account_id = input('Enter new account_id: ')
                    
                while account_id in User.Bank_account:
                    account_id = input('This is invalid, try again: ')
                User.Bank_account[account_id] = acc
                while flag2:
                    print('\n1. Deposit money \n2. Withdraw money')
                    print('3. Check balance \n4. Transaction \n5. Check Transaction history')
                    print('6. If  your need loan')
                    print('press any key if you want back\n')
                        
                    b = int(input('Enter your option: '))
                        
                    if b == 1:
                        money = int(input('ENter your amount: '))
                        acc.deposit(money)
                            
                    elif b == 2:
                        money = int(input('ENter your amount: '))
                        if money > User.Total_balance:
                            print('The bank is bankrupt\n')
                        else:
                            acc.withdraw(money)
                            
                    elif b == 3:
                        acc.check_balance()
                        
                    elif b == 4:
                        money = int(input('Enter transfer money: '))
                        tranfer_id = input('ENter transfer id: ')
                        if tranfer_id in User.Bank_account:
                            acc.transfer(money, User.Bank_account[tranfer_id])
                        else:
                            print('Account does not exist\n')
                        
                    elif b == 5:
                        print(f"Transaction History______________ \n{acc.transaction_history}")
                        
                    elif b == 6:
                        acc.loan()
                        
                    else:
                        flag2 = False
            
            elif a==2:
                passward = input('Enter your passward : ')
                if passward in User.Bank_account:
                    flag2 = True
                    while flag2:
                        acc = User.Bank_account[passward]
                        print('\n1. Deposit money \n2. Withdraw money')
                        print('3. Check balance \n4. Transaction \n5. Check Transaction history')
                        print('6. If  your need loan')
                        print('press any key if you want back')
                        
                        b = int(input('Enter your option: '))
                        
                        if b == 1:
                            money = int(input('ENter your amount: '))
                            acc.deposit(money)
                            
                        elif b == 2:
                            money = int(input('ENter your amount: '))
                            if money > User.Total_balance:
                                print('The bank is bankrupt\n')
                            else:
                                acc.withdraw(money)
                            
                        elif b == 3:
                            acc.check_balance()
                            
                        elif b == 4:
                            money = int(input('Enter transfer money: '))
                            tranfer_id = input('ENter transfer id: ')
                            if tranfer_id in User.Bank_account:
                                acc.transfer(money, User.Bank_account[tranfer_id])
                            else:
                                print('Account does not exist\n')
                        elif b == 5:
                            print(f"Transaction History______________ \n{acc.transaction_history}")
                        
                        elif b == 6:
                            acc.loan()
                        
                        else:
                            flag2 = False
                    
                else:
                    print('This is incorrect passward.\n')
                      
            else:
                print('\n__________Thank you___________\n')
                flag1 = False
    
    elif n==2:
        pas = input('Enter Admin passward: ')
        if pas == '110011':
            print('__________ Welcome to bank system __________\n')
            flag1 = True
            while flag1:
                print('press any serial number____\n')
                print('1. Create an account')
                print('2. Delete any user account')
                print('3. see all user accounts list')
                print('4. Check Total balance')
                print('5. Check Total loan amount')
                print('6. can on or off the loan feature')
                print('*. press any key for exist \n')
                
                n = int(input('Enter a number: '))
                
                if n == 1:
                    nam = input('Enter your name: ')
                    email = input('Enter your email account: ')
                    address = input('Enter your address: ')
                    account_type = input('Enter your account type: ')
                    acc = User(nam, email, address, account_type)
                    account_id = input('Enter new account_id: ')
                        
                    while account_id in User.Bank_account:
                        account_id = input('This is invalid, try again: ')
                    User.Bank_account[account_id] = acc
                        
                elif n == 2:
                    a = input('Enter account id: ')
                    User.Bank_account.pop(a)
                    print('Remove account successfully! \n')
                
                elif n == 3:
                    for key in User.Bank_account:
                        print(User.Bank_account[key].deatils())
                        print('_______________-____________\n')
                
                elif n == 4:
                    print(f"Total available balance of the bank : ${User.Total_balance:.2f}\n")
                
                elif n == 5:
                    print(f"The total loan amount is: ${User.Total_loan_amount:.2f}\n")
                
                elif n == 6:
                    x = int(input('If you want loan feature can acctive press 1 otherwis press 2 : '))
                    if x == 1:
                        User.loan_feature = True
                    elif x == 2:
                        User.loan_feature = False 
                else:
                    flag1 = False
                
        
        else:
            print('Sorry This is  wrong passward ❌\n')
    
    else:
        print('Thanks for visit our Bank.\n')
        flag = False
    