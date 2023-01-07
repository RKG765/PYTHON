# it is for using a function from a file to another file like below-->

def greet(name):
    print(f"Good Night, {name}")

# print(__name__)

if __name__ == "__main__":
    a = input("Enter your name: ")
    greet(a)