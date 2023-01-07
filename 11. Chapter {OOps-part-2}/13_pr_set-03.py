class Employee:
    salary = 4000
    bonus = 300
    @property
    def totalSalary(self):
        return self.salary + self.bonus
    @totalSalary.setter
    def totalSalary(self,newSalary):
        self.salary = newSalary - self.bonus

e = Employee()
e.totalSalary = 8000
print(e.salary)
print(e.bonus)
print(e.totalSalary)
