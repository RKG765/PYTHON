class Animal:
    species = 'Mammals'

class Pets(Animal):
    domesticpets = 'Dogs'

class Dog(Pets):
    def  __init__(self,Dogname):
        self.Dogname = Dogname
    def __str__(self):
        return f'Hey ! {self.Dogname}'
    @staticmethod
    def Dogbark():
        print('...... bow bow bow......bow :)')

jony = Dog('jony')
print(jony)
jony.Dogbark()

