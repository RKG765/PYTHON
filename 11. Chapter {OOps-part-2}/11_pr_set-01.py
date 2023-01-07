class c2dvec:
    def __init__(self,i,j):
        self.icap = i
        self.jcap = j
    def __str__(self):
        return f'{self.icap}i + {self.jcap}j'

class c3dvec(c2dvec):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k
    def __str__(self):
        return f'{self.icap}i + {self.jcap}j +{self.kcap}k'

v2d = c2dvec(3, 5)
v3d = c3dvec(4, 5, 3)
print(v2d)
print(v3d)