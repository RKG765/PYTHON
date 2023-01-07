a = {
    'raj': 'loves death',
    'hari': 'he is a good boy',
    1: 342
}
# print(a.keys()) #finding keys
# print(type(a.keys())) # it's type is 'dict_keys'
# print(list(a.keys())) # finding list with .keys function
# print(a.values())  # finding values in the dictonary
# print(a.items()) # prints the (keys and values) for all contents of the dictonary
b = {
    "lovish": "friends",
    "raj": "friend",
    1: 453
}
a.update(b) # updates the dictonary with by adding key-value pairs
print(a)
print(a.get("raj2")) #returns none as it is not present in 'a'
# print(a["raj2"]) # throws an error because raj2 is not present in the dictonary
# the difference between .get and [] syntax in the syntax
