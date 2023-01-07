# below example is type of single inheritance in which there is only one base class 
# and only one  derived class  


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