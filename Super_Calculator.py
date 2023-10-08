class Calculator:
    """ Do addition, Subtraction, Multiplication, Division and Modulus."""
    
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def addition(self):
        return f"num1 + num2 = {self.num1 + self.num2}"
    
    def subtraction(self):
        if self.num1 > self.num2:
            return f"num1 - num2 = {self.num1 - self.num2}"
        else:
            return f"num2 - num1 = {self.num2 - self.num1}"
    
    def multiplication(self):
        return f"num1 * num2 = {self.num1 * self.num2}"
    
    def division(self):
        try:
            return f"num1 / num2 = {self.num1 / self.num2}"
        except ZeroDivisionError:
            return 'It is impossible to divide by zero.'
    
    def modulus(self):
        ans1 = self.num1 % self.num2
        ans2 = self.num2 % self.num1
        
        return f"num1 % num2 = {ans1} and num2 % num1 = {ans2}"

# Inheritance
class SuperCalculator(Calculator):
    def __init__(self, num1, num2, number):
        super().__init__(num1, num2)
        self.number = number
        
    def square(self):
        return f"Number ^ 2 : {self.number * self.number}"
    
    def cube(self):
        return f"Number ^ 3: {self.number ** 3}"
    
    # Method Overriding
    def addition(self):
        return f"num1 + num2 + number = {self.num1 + self.num2 + self.number}"


number1 = int(input('Enter your 1st number : '))
number2 = int(input('Enter your 2nd number : '))
number3 = int(input('Enter your 3rd number : '))

my_calculator = SuperCalculator(number1, number2, number3)


sum = my_calculator.addition()
print(sum)

difference = my_calculator.subtraction()
print(difference)

multiple = my_calculator.multiplication()
print(multiple)

divide = my_calculator.division()
print(divide)

mod = my_calculator.modulus()
print(mod)

squr = my_calculator.square()
print(squr)

cub = my_calculator.cube()
print(cub)

