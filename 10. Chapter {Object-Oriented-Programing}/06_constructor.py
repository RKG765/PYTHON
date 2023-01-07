class Employee:
    company = 'Google'
    def __init__(self,name,salary,unit):
        self.name = name
        self.salary = salary
        self.unit = unit 
        print('Employee is Added.')
    def getDetails(self):
        print(f'Name of Employee-- {self.name}')
        print(f'Salary of Employee-- {self.salary}')
        print(f'Unit of Employee-- {self.unit}')

Raj = Employee('Raj', 10000, 'YouTube')
Raj.getDetails()
