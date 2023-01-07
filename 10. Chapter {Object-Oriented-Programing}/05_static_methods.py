'''sometimes we need a function that doesn't use the self paprameter.
we can define a static method like following:--> :) '''
class Employee:
    company = 'Google'

    def getSalary(self):
        print(f"Salary of this emplyee working in {self.company} is {self.salary}")
    
    @staticmethod
    def greet():
        print('Good Morning,Sir')

raj = Employee()
raj.salary = 1000
raj.getSalary =50000
raj.greet()
print(raj.getSalary)
