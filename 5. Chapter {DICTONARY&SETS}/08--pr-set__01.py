# writing a program to create a dictonary of hindi words with their english values
a = {
    "mango": "aam",
    'car': 'gari',
    'banana': 'kela'
}
print("Options are ",a.keys())
b = input("Enter your Word:\n")
print("The meaning of your word is:",a.get(b)) # for not seeing error
# English to Hindi
