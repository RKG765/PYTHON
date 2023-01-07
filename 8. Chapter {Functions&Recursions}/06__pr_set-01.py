
def maximum(num1, num2, num3):
    if (num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if (num2>num3):
            return num2
        else:
            return num3

b = maximum(43,5,5)
print("the greatest number is "+ str(b))
print(b)
