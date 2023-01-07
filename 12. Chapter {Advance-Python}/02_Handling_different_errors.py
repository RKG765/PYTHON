try:
    a = int(input("Enter a number: "))
    c = 1/a
    print(c)
except ValueError as e:
    # print(f"Eception1 occuered as {e}")
    print("Please enter a valid value")

except ZeroDivisionError as e:
    # print(f"Eception2 occuered as {e}")
    print("Dividing by 0 is not possible")