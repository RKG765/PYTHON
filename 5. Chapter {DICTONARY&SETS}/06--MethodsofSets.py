a = set()
a.add(7) # adding in the empty set
a.add(321)
a.add(7) # as we know it is a collection of non-repeatative element
# print(a)
# we can't add list in the but we can add tuple in the set ---> As below
a.add((1,2,3,4,5))
# print(a)
# We can't add dictonary in the set
# a.add({"raj": "good person"})
# print(a)
# hasseble means it can't be changed then it can be add in set

#  removal & Length of set
# print(len(a)) # it shows the length of set

# a.remove(321) # remove 321 from set
# print(a)

# print(a.pop())
# a.clear() # clears the sets 
print(a)