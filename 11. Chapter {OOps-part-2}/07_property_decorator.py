# property decoretor is also known as getter
class Employee:
    company =  'petroleum'
    salary = 40000
    salarybonus = 1000

    @property
    def totalSalary(self):
        return self.salary + self.salarybonus

e = Employee()
print(e.totalSalary)
e.totalSalary = 38000

