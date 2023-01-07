# it is mainly used for making a new class from a existing class 
# this also uses DRY principle means do not repeat

class Employee:
    company = 'Microsoft'
    def getStatus(self):
        print(f'You are now a worker in {self.company}')

class Programmer(Employee):
    company = 'Youtube'
    def getInfo(self,name):
        self.name = name
        print(f'{self.name} is a worker in {self.company}')

raj = Employee()
lol = Programmer()
raj.getStatus()
lol.getInfo('lol')
lol.getStatus()
print(lol.company)
# raj.getInfo('raj') this is not working  and  i don't know  why  