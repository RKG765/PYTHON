# writing a program inwhich taking marks from from the user to elvaluate wheather a student is pass or fail subjects are
# 3 and atleast 33% in each subject and total 40%

a = int(input("marks in maths\n"))
b = int(input("marks in english\n"))
c = int(input("marks in science\n"))

if a>=33:
    print("Pass in subject maths")
else:
    print("You are fail")

if b>=33:
    print("pass in subject english")
else:
    print("Fail")

if c>=33:
    print("Pass in subject science")
else:
    print("fail")

d = int(a+b+c)

if d/3>=40:
    print("you are pass in all subject")
else:
    print("Sorry,you are Fail")
print(d)

