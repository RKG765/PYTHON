# operators  in python can be overloaded using dunder methods.
# following are the operators used  methods
# __add__ for adding
''' __sub__ for minus
__mul__ for multiplication
__truediv__ for divide
__floordiv__ for \\ ''' 
class Number:
    def __init__(self,num):
        self.num = num
    def __add__(self,num2):
        return self.num + num2.num
    def __floordiv__(self,num2):
        return self.num // num2.num

n1 = Number(2)
n2 = Number(100)
print(n1 + n2)
f = n2 // n1
print(f)