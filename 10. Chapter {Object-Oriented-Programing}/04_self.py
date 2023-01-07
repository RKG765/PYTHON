# self is a parameter which pass automatically through object like below
# by self you can use instance and class attributes both
# it is automatically passed with a function called from an object 

class Employee:
    company = 'Google'
    salary = 100000
    def getSalary(self):
        print(f" Salary of this emplyee working in {self.company} is {self.salary}")

raj = Employee()
raj.Salary = '67676'
# raj.getSalary
# print(raj.getSalary)
# above line means 
# Employee.getSalary(raj)