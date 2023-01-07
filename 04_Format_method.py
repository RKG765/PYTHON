# It is like a f'' method
name = "Raj Kumar Gupta"
channel = " RKG "
stream = "YouTube"
# Old method
# it can also done by indexing like below
a = "This is {2} and his channel is {1} , streaming on {0}".format(name,channel,stream)
print(a)
# this above code is also written as below
# New method
a = f"This is {name} and his channel is {channel} , streaming on {stream}"
print(a)