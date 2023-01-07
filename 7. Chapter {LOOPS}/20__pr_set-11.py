# writing apython program to print multiplication table of n using for loop in reversed order
n = int(input("Enter the number:"))
for i in range(1,11):
    print(str(n)+ "x"+ str(i)+ '=',end="")
    print(n*i)