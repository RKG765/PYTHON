# In this  inheritance a chikd class becomes a parent of another child class 
class Human:
    name = 'Homosapines'
    origin = 'Earth'

class Person(Human):
    country = 'India'
    state = 'Bihar'

class Employee(Person):
    company = 'Google'
    def getSalary(self):
        print(f'Your salary is {self.salary}')

h = Human()
print(h.name)
print(h.origin)
p = Person()
print(p.origin)
print(p.country)
e = Employee()
e.salary = 100000
e.getSalary()