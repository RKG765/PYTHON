class Employee:
    company =  'petroleum'
    salary = 40000
    salarybonus = 1000

    @property
    def totalSalary(self):
        return self.salary + self.salarybonus
    @totalSalary.setter
    def totalSalary(self,sal):
        self.salarybonus = sal - self.salary


e = Employee()
print(e.totalSalary)
e.totalSalary = 45000
print(e.salary)
print(e.salarybonus)
print(e.totalSalary)
