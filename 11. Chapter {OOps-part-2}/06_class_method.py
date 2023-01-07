# class attributes can't be changed
# but you can add a instance attribute
# class method is bound to the class not to the object
# @classmethod is decorator is used to create a class method 
# but through class method we can channge class attribute
# Like below --->

class Employee:
    company = 'Lucus'
    salary = 1000
    location = 'Bihar'

    @classmethod
    def changeLocation(cls, newloc):
        cls.location = newloc
    


e = Employee()
# print(e.location) # here it prints the location of class attribute
e.changeLocation('Delhi')
print(e.location)   #it doesn't change the class attribute it creats a instance attribute for the object
print(Employee.location) 

