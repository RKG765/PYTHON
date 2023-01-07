from functools import reduce

l = [2,3,4,5,6,7,322525]

# func = lambda a, b : str(max(a,b))
greater = reduce(max,l)
print(greater)
# note next question is about virtualenv