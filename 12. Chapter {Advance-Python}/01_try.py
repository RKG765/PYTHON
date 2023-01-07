# There are many types of error like below
# value error,syntax error,name error,zero division error,type error

while(True):
    print("press q to  quit")
    a = input("Enter a number: ")
    if a == 'q':
        break
    try:
        a = int(a)
        if a > 6:
            print("Your entered number is greater then 6")
    except Exception as e:
        print(f'Your error is {e}')

print('.........Thanks for playing........') 