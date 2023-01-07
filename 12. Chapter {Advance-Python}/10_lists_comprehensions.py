a = [3,34,43,53,255,14,234,344,432,42,4,234,234,234,24,23,45,345,3667,456,57,54]
# A decent and bigger way.......
b = []
for item in a:
    if item%2 == 0:
        b.append(item)

print(b)

# A new easy way is like below
b = [i for  i in a if i%2==0]
print(b)