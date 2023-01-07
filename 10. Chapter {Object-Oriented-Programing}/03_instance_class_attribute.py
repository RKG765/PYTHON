class Employee:
    company = 'Google'
    salary = 250
    

harry = Employee()
raj = Employee()
# creating instance attribute salary for both employees
# raj.salary = 500
harry.salary = 60
raj.address = 'sadikpur,muzaffarpur,bihar,843126'
print(harry.salary)
print(raj.salary)
print(raj.address)
# below line thorws an error bcoz no instance attributes are present for below line
# print(harry.address)