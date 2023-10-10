class Users:
    def __init__(self, name, age, phone_number) -> None:
        self.name = name
        self.age = age
        self.phone_number = phone_number
        
        
class Manager(Users):
    def __init__(self, name, age, phone_number, email) -> None:
        super().__init__(name, age, phone_number)
        self.email = email
        

class Customer(Users):
    def __init__(self, name, age, phone_number) -> None:
        super().__init__(name, age, phone_number)
    

class Employe(Users):
    def __init__(self, name, age, phone_number, adderss, department, salary) -> None:
        super().__init__(name, age, phone_number)
        self.address = adderss
        self.department = department
        self.salary = salary

class Chef(Employe):
    def __init__(self, name, age, phone_number, adderss, department, salary) -> None:
        super().__init__(name, age, phone_number, adderss, department, salary)
        
        
class Server(Employe):
    def __init__(self, name, age, phone_number, adderss, department, salary) -> None:
        super().__init__(name, age, phone_number, adderss, department, salary)
        
class Supplier(Employe):
    def __init__(self, name, age, phone_number, adderss, department, salary) -> None:
        super().__init__(name, age, phone_number, adderss, department, salary)
        
    