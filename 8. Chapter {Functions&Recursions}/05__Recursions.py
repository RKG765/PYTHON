# recursion is used mainly in mathematics as a formula
# it difines itself
# taking an example 
def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product
print(factorial_iter(4))

# making formula of factorial(!)
# n! = (n-1)! * n 
# now factorial_recursive
def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial_recursive(n-1)

f = factorial_recursive(1)
print(f)