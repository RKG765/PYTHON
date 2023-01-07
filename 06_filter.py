def greter_than5(num):
    if num > 5:
        return True
    else:
        return False
lam = lambda num : num > 10
l = [1,2,3,4,5,5,6,67,7,75,3,3455,6634,634643,636,636]
print(list(filter(lam,l)))