a = int(input("Enter your number: "))

t = [a*i for i in range(1,11)]
print((t))
with open('tables.txt','a') as f:
    f.write(str(t))
    f.write('\n')
