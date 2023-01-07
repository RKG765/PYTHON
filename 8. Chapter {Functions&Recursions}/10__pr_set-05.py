def factorial_sum(n):
    if n == 1 or n ==0:
        return 1
    return (n + factorial_sum(n-1))

a = int(input("Enter your number :"))
b = factorial_sum(a)
print("some of first "+str(a)+" numbers" +" = "+str(b))
