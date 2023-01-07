# it is the best way to open a file it dosen't need to write the .close statement
with open('another.txt', 'r') as d:
    s = d.read()
print(s)
with open('mini world', 'w') as e:
    a = e.write("this world is .......")
print(a)