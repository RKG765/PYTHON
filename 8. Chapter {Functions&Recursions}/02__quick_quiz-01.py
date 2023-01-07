# writing a program to say a user good day

name = input("Enter your name: ")

def greet(name):
    print("Good Day, "+ name) #function definition
greet(name) #function call

def sum(num):
    print(num[0] + num[1]+num[2])
num = [32,54,64]
sum(num)