def conv_cm(inch):
    inch = inch * (2.54)
    return inch
a = int(input("Enter length :"))
b = conv_cm(a)
print("Length of "+str(a)+"inch" +" = "+str(b)+"cm")