# if except quits the program the it runs smoothlywith no problems
try:
    i = int(input("Enter a number: "))
    c = 1/i
except Exception as e:
    print(e)
    exit()

finally:
    print("it comes everytime")