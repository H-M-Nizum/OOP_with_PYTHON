from GussNumber import Random
def main():
    print('\n__________Welcome to our guessing Number application_____________\n')
    flag = True
    
    while flag:
        nam = input('Enter your name📛 :- ')
        email = input('Enter your email📩 :- ')
        game = Random(nam, email)
        flag1 = True
        while flag1:     
            print('Start your game________\n')
            ranNumber = game.guess_random()
            flag2 = True
            while flag2:
                num = int(input('Guess a number🤔 :- '))
                game.guess(num, ranNumber)
                if num == ranNumber:
                    game.track_histry[ranNumber] = game.input_number
                    flag2 = False
            Random.histry[nam] = game.track_histry      
            print('\nIf you want play again press 1️⃣\nif you want see your game histry press 2️⃣ \nOtherwise press any number 🦉\n')
            n = int(input('Enter your option:- '))
            if n == 1:
                flag1 = True
            elif n == 2:
                print(Random.histry[nam])
                print('\nIf you want play again press 1️⃣ \nOtherwise press any number 🦉\n')
                n = int(input('Enter your option:- '))
                if n == 1:
                    flag1 = True
                else:
                    flag1 = False
            else:
                flag1 = False
        
        print('\nIf want to play a new player press 1️⃣\nif you want see Hole game histry press 2️⃣\nOtherwise press any number 🦉\n')
        m = int(input('Enter your option:- '))
        if m == 1:
            flag = True
        elif m==2:
            print(Random.histry)
            print('\nIf want to play a new player press 1️⃣\nOtherwise press any number 🦉\n')
            m = int(input('Enter your option:- '))
            if m == 1:
                flag = True
            else:
                flag = False
        else:
            print('\n___________Thanks for playing game________________')
            flag = False
                


if __name__ == '__main__':
    main()