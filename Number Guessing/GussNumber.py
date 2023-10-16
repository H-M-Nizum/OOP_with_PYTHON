import random

class Random:
    histry = {}
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        self.input_number = []
        self.track_histry = {}

        
    def guess_random(self):
        return random.randrange(1, 101)
    
    def guess(self, number, random_number):
        self.input_number.append(number)
        if number == random_number:
            print('You are guess right number 🟰🤝')
            print(f"You need 💢💢 {len(self.input_number)}th 💢💢 time for guess the right number.\n")
  
        
        elif number > random_number:
            print('Your nuber is too high🆙 from the original number ❌\n')
            
        else:
            print('Your nuber is too low⏬ from the original number ❌\n')
    
    



