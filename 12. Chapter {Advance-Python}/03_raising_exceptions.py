def increase(num):
    try:
        return int(num)+1
    except:
        raise ValueError("Please enter a valid value")

a = increase('34gy')
print(a)