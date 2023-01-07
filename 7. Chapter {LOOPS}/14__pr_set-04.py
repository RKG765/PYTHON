# writing a program to find a number is given is  prime or not

num = int(input("Enter your number :"))

prime = True

for i in range(2, num):
    if (num%i == 0):
        prime = False
        break
if prime:
    print("this number is prime")
else:
    print("this number is not prime")