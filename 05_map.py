def square(num):
    return num * num

l = [1,4,6,78]
# method 1
l2 = []
for items in l:
    l2.append(square(items))
print(l2)
# Eaiser method by map
print(list(map(square,l)))