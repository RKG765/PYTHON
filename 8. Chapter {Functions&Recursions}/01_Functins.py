# making functionn
# def is used for making function 

def percent(marks):
    a = 0
    b = 0
    for i in marks:
        a+=marks[b]
        if (b>(len(marks)+1)):
            b+=1
    # return((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
    return a/len(marks)

b = int(input("Enter number of subbjects: "))
a = 0
while (a>b):
    marks1 = []
    marks1.append[a] = int(input("Enter marks ",a+1,": "))
    a+=1
percentage1 = percent(marks1)
print(percentage1)

# marks2 = [89,78,64,90]
# percentage2 = percent(marks2)
# print(percentage1, percentage2)