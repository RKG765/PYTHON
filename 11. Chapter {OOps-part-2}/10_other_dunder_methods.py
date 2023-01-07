# __str__ dunder method is generally used in the following ways
class Number:
    def __init__(self,num):
        self.num = num
    def __add__(self,num2):
        return self.num + num2.num
    def __floordiv__(self,num2):
        return self.num // num2.num
    def __str__(self):
        return f'Decimal number: {self.num}'
    def __len__(self):
        return 1


n = Number(19)
print(n)
print(len(n))