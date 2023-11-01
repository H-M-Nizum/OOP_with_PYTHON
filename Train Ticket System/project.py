class Train():
    def __init__(self, name, id, location, destination) -> None:
        self.name = name
        self.id = id
        self.location = location
        self.destination = destination


class Admin(Train):
    passenger_list = []
    Train_list = []
    seets = {}

    def __init__(self, email) -> None:
        self.email = email

    def add_train(self, name, id, location, destination):
        new_train = Train(name, id, location, destination)
        self.Train_list.append(new_train)
        seet = []
        for i in range(10):
            seet.append(['A', 'A', 'A', 'A'])

        self.seets[id] = seet

    def show_available_trains(self):
        print('_____________________________ Train info _________________________\n')
        for train in self.Train_list:
            print(
                f'name: {train.name}, id : {train.id}, location: {train.location}, destination : {train.destination}')
        print()

    def show_available_seets(self, id):
        print('_____________________________ Show Available seets info _________________________\n')
        for i in self.seets[id]:
            for j in i:
                print(j, end=' ')
            print()
        print()

    def book_seet(self, id, row, column):

        print()

        if self.seets[id][row][column] == 'X':
            print('This seet is already book 🥹')
        else:
            self.seets[id][row][column] = 'X'
            print('Booking seet secessfully ✅')

    def show_users(self):
        print(
            '_____________________________ Show all user info _________________________\n')
        for passenger in self.passenger_list:
            print(
                f'name: {passenger.name}, Email : {passenger.email}')
        print()


class User():
    def __init__(self, name, email, password) -> None:
        self.name = name
        self.email = email
        self.password = password


admin = Admin('Admin@gmail.com')

while True:
    user_Type = input("Admin/User/ Exist ? : ")
    print()
    if user_Type == 'User':
        print('1. login')
        print('2. rejister')
        print('3. exit \n')

        choice = int(input('chose a number : '))
        print()

        if choice == 1:
            email = input('Enter your email ID: ')
            password = input('Enter your password: ')
            print()
            flag = False
            for user in Admin.passenger_list:
                if user.email == email and user.password == password:
                    print('welcome ', user.name, '\n')
                    flag = True

                    while True:
                        print('1. show abailable train')
                        print('2. show abailable seets')
                        print('3. book seets')
                        print('4. logout \n')

                        choice = int(input('Enter your Choice: '))
                        print()
                        if choice == 1:
                            admin.show_available_trains()

                        elif choice == 2:
                            id = int(input('Train id: '))
                            print()
                            admin.show_available_seets(id)

                        elif choice == 3:
                            id = int(input('Train id: '))
                            row = int(
                                input('Enter your Row number in seets list : '))
                            column = int(
                                input('Enter your Column number in seets list: '))
                            print()
                            admin.book_seet(id, row, column)

                        elif choice == 4:
                            break
            if flag == False:
                print('\nworng email or password ❌ \n')

        elif choice == 2:
            name = input('Enter your name: ')
            email = input('Enter your email ID 📧 : ')
            password = input('Enter your password 🔑 : ')

            new_user = User(name, email, password)
            admin.passenger_list.append(new_user)
            print('\nsusccessful rejister\n')

        else:
            break
    elif user_Type == 'Admin':
        email = input('Enter your email ID 📧 : ')
        password = input('Enter your password 🔑 : ')

        if email == admin.email and password == '123':
            print('\nsuccessfully login\n')
            while (True):
                print('1 Show all abailable train')
                print('2 Show all user')
                print('3 Add  new train ')
                print('4. logout \n')

                choice = int(input('enter choice: '))
                print()
                if choice == 1:
                    admin.show_available_trains()
                elif choice == 2:
                    admin.show_users()
                elif choice == 3:
                    name = input('Enter train name: ')
                    id = int(input('Enter train id : '))
                    location = input('Enter train current location: ')
                    destination = input('Enter train destination: ')

                    admin.add_train(name, id, location, destination)
                elif choice == 4:
                    break

        else:
            print('\nWorng email or password ❌ \n')

    elif user_Type == 'Exist':
        break

    else:
        print(
            '\nInvalid ❌ ______________________ \nplease select 1️⃣: Admin or  2️⃣: User or 3️⃣: Exist\n')
