from Menu import Menu
from users import *
class Restaurant:
    Balance = 0
    def __init__(self, name) -> None:
        self.name = name
        
    

Restaurant1 = Restaurant('Mugoly sahi dorbar')

flag = True
while flag:
    print('Enter one number _________ \n' )
    print('1. Customer')
    print('2. Employe')
    print('3. Exist')
    number = int(input('Enter your Number: '))
    Menu_card = Menu()
    if number == 1:
        Menu_card.show_menu()
        print('\n \n')
        flag1 = True
        while flag1:
            print('What you want___________')
            print('1. Burger')
            print('2. Pizza')
            print('3. Biryani')
            print('4. Drinks')
            print('5. Fruits')
            print('6. Turkish foods')
            print('7. Middle Eastern foods')
            print('If you want exist press any number \n \n')
            type_of_item = input('Select any Number in this menu: ')

            iteams = {'1': 'Burger', '2': 'Pizza', '3': 'Biryani', '4': 'Drinks', '5': 'Fruits', '6': 'Turkish foods', '7': 'Middle Eastern foods'}
            print('\n \n')
            if type_of_item in iteams:
                iteam = input('Enter your food iteam name: ')
                amount = int(input('Enter number of iteam: '))

                if iteam in Menu_card.food[iteams[type_of_item]]:
                    print(f" \n {iteam}'s price is : {Menu_card.food[iteams[type_of_item]][iteam]} And Total price is {Menu_card.food[iteams[type_of_item]][iteam]*amount}. \n\n")
                    print('If you order this iteam, press 1.')
                    print('If you want show again menu card, press 2.')
                    print('If you want Exist, press any number.\n')
                    press = int(input('Enter number : '))
                    if press == 1:
                        print('\n____#######    Your order Succesfully Done    ########____\n')
                        Restaurant1.Balance += Menu_card.food[iteams[type_of_item]][iteam]*amount
                    elif press == 2:
                        Menu_card.show_menu()
                        print('\n\n')
                else:
                    print('\n____#######    you select wrong iteams name    ########____\n')
            else:
                flag1 = False
    elif number == 2:
        pas = input('Enter passward : ')
        flag2 = True
        while flag2:
            if pas == '1111':
                print('_____________ Welcome back Mr Manager______________')
                print()
                print('1. Add iteams in menu')
                print('2. Add employe in Restaurant')
                print('3. Check Total balance')
                print('4. Show Menu')
                print('If you waant Exist press any other number \n')
                
                option = int(input('Enter a number : '))
                if option == 1:
                    typeOfIteams = input('Write type of iteam: ')
                    iteam_name = input('Write iteam name: ')
                    iteam_price = int(input('Write iteam price: '))
                    if typeOfIteams in Menu_card.food:
                        Menu_card.add_menu_item(typeOfIteams, iteam_name, iteam_price)
                        print('\n____#######    Succesfully added new iteam in menu    ########____\n')
                    else:
                        print('\n____#######    !!! SORRY you choose Wrong iteam !!!    ########____\n')
                elif option == 2:
                    print('___________################__________ \n')
                    print('1. Add Chef for Restaurant')
                    print('2. Add Server for Restaurant')
                    print('3. Add Supplier for Restaurant')
                    opt = int(input('Enter a number: '))
                    if opt == 1:
                        chef = Chef('kalacan', 34, 1002874734, 'Dhaka', 'Chef', 25000)
                        print('\n____#######    Succesfully added new Chef in menu    ########____\n')
                    elif opt == 2:
                        server = Server('dolacan', 23, 43584543, 'Dhaka', 'Service', 18000)
                        print('\n____#######    Succesfully added new server in menu    ########____\n')
                    elif opt == 3:
                        supplier = Supplier('lalcan', 43, 56575445645, 'Dhaka', 'SUpply', 'Depend')
                        print('\n____#######    Succesfully added new Supplier in menu    ########____\n')
                    else:
                        print('!!! You press wrong number\n')
                
                elif option == 3:
                    print(f"\n ___########### Your Restaurant current balance is : {Restaurant1.Balance} \n")
                elif option == 4:
                    Menu_card.show_menu()
                    print('\n \n')
                    
                else:
                    flag2 = False
            else:
                print('\n____#######    !!! This is wrong passward !!!    ########____\n')
                flag2 = False
    else:
        flag = False
                                    
            
                

            
                
                    