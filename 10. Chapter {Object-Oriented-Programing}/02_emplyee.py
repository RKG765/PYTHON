# class attributes
class Employee:
    company = 'Google'
    salary = 200
    age = 18

harry = Employee()
raj = Employee()
raj.salary = 500
harry.salary = 600
print(raj.salary)
print(harry.salary)
# print(raj.company)
# print(harry.company)
Employee.company = 'Youtube'
print(harry.company)
print(raj.company)
