a = 1009 # Global variable

def fun1():
    global a #It will change the local variable into the global variable 
    print(f'It runs the global varable {a}.....')
    a = 23 #Local variable
    print(f"It will print the local variable {a}.....")

fun1()
print(f"It will print the global variable {a} , as it is changed in the func1 by global a.....") 