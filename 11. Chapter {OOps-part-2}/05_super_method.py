# It only works with a def function inside a class 
# It can also used for init function
class Human:
    name = 'Homosapines'
    origin = 'Earth'
    def city(self):
        print('Earth')
    def __init__(self):
        print('Initializng Human')

class Person(Human):
    country = 'India'
    state = 'Bihar'
    def city(self):
        super().city()
        print('Muzaffarpur')
    def __init__(self):
        super().__init__()
        print('Initializng Person')

class Employee(Person):
    company = 'Google'
    def city(self):
        super().city()
        print('Los Angels')
    def getSalary(self):
        print(f'Your salary is {self.salary}')
    def __init__(self):
        super().__init__()
        print('Initializng Employee')

h = Human()
h.city()
p = Person()
p.city()
e = Employee()
e.city()