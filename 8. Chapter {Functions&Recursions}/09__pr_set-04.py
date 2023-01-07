def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    return (n * factorial_recursive(n-1))

b = int(input('Enter your number :'))
a = factorial_recursive(b)
print("factorial of " + str(b) + '=' + str(a))