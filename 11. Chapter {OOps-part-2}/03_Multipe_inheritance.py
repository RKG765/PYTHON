# multiple  inheritance occurs when child class derived from more than one parents
class Employee:
    company = 'visa'
    eCode = 120

class Freelancer:
    company = 'Fiverr'
    level = 0
    def upgradeLevel(self):
        self.level = self.level + 1

class Programmer(Employee, Freelancer):
    name = 'Raj'

p = Programmer()
print(p.company)
p.upgradeLevel()
print(p.level)