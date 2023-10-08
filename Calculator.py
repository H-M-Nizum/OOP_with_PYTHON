class Calculator:
    """ Do addition, Subtraction, Multiplication, Division and Modulus."""
    
    def addition(self, num1, num2):
        return f"num1 + num2 = {num1 + num2}"
    
    def subtraction(self, num1, num2):
        if num1 > num2:
            return f"num1 - num2 = {num1 - num2}"
        else:
            return f"num2 - num1 = {num2 - num1}"
    
    def multiplication(self, num1, num2):
        return f"num1 * num2 = {num1 * num2}"
    
    def division(self, num1, num2):
        try:
            return f"num1 / num2 = {num1 / num2}"
        except ZeroDivisionError:
            return 'It is impossible to divide by zero.'
    
    def modulus(self, num1, num2):
        ans1 = num1 % num2
        ans2 = num2 % num1
        
        return f"num1 % num2 = {ans1} and num2 % num1 = {ans2}"
    
my_calculator = Calculator()

number1 = int(input('Enter your 1st number : '))
number2 = int(input('Enter your 2nd number : '))

sum = my_calculator.addition(number1, number2)
print(sum)

difference = my_calculator.subtraction(number1, number2)
print(difference)

multiple = my_calculator.multiplication(number1, number2)
print(multiple)

divide = my_calculator.division(number1, number2)
print(divide)

mod = my_calculator.modulus(number1, number2)
print(mod)

