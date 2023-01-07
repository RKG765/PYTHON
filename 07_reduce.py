from functools import reduce

# Reduce complies a addition with all the items in the list

l = [1,2,3,4,5,6,7,8,9,10]
add = lambda a,b : a+b
a = reduce(add,l)
print(a)