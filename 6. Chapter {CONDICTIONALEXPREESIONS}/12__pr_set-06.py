# writing a program to calculate the grade of a student from his 
# marks from the following scheme
# 90-100 = ex 
# 80-90 = a 
# 70-80 = b 
# 60-70 = c 
# 50-60 = d 
# <50 = f 
number = int(input("Enter your number\n"))
if number>=90:
    print("Ex")
elif number>=80:
    print("A")
elif number>=70:
    print("B")
elif number>=60:
    print("C")
elif number<50:
    print("F")
else:
    print("You are fail")
