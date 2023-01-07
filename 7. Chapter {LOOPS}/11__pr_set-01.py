# writing a program to print multiplication table in for loop
a = int(input("Enter the number:"))

for i in range(1,11):
    # print(str(a) + "x" +str(i) + "="+ str(a*i))
    print(f"{a}x{i}={a*i}")