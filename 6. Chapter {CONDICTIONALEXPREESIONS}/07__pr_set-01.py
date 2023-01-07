# writing a program to find the greatest of 4 number entered by hte user

a = int(input("Enter your first number\n"))
b = int(input("Enter your second number\n"))
c = int(input("Enter your third number\n"))
d = int(input("Enter your fourth number\n"))
if a>b>c>d:
    print("The gretest number is\n ", a)
elif a<b<c<d:
    print("The greatest number is\n ", d)
elif a<b>c>d:
    print("The gretest number is\n ", b)
elif a<b<c>d:
    print("The greatest number is\n ", c)
else:
    print("Sorry,you have written all characters same\n No one greater")
