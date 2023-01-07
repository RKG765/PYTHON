class Programmer:
    company = 'Microsoft'
    def __init__(self,name,product,salary):
        self.name = name
        self.product = product
        self.salary = salary
    def getInfo(self):
        print(f"The name of programmer is {self.name}")
        print(f"Programmer works in {self.product} sub-unit")
        print(f"The salary of programmer is {self.salary}")

raj = Programmer('raj', 'Microsoft',100000)
pihu = Programmer('pihu','Github',100000)
raj.getInfo()
pihu.getInfo()