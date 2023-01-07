try:
    a = int(input("Enter your 1st number: "))
    b = int(input("Enter your 2nd number: "))
    c = print(a/b)
    if a==0 or b==0:
        print('Undefined')
except ZeroDivisionError as e:
    print(f'Your answer is Infinite when {e}')