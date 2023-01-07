class calculator:
    def __init__(self,num):
        self.num = num
    def square(self):
        print(f'Square of {self.num} is {self.num **2}')
    def squareroot(self):
        print(f'Squareroot of {self.num} is {self.num **0.5}')
    def cube(self):
        print(f'Cube of {self.num} is {self.num **3}')
    @staticmethod
    def greet():
        print('******** Welcome to the calculator app ********')


a = calculator(4)
a.square()
a.squareroot()
a.cube()
a.greet()