# writing a program to find out whether a given post is talking about "harry"
# or not
a = input("Enter a post\n")
if 'harry' in a:
    print("yes")
elif 'Harry'in a:
    print("yes")
elif 'haRRy'in a:
    print("yes")
elif 'HARRY' in a:
    print("yes")
elif 'HArry' in a:
    print("yes")
else:
    print("no")
