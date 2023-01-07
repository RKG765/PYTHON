import random

user = int(input("Enter your guess[0,20]:\n"))

i = 20

rand = random.randint(0, i)

if (user > rand):
    print('Lower number please :( ')
    print(f'Random number is {rand}')
    print(f"User's number is {user}")

elif (user < rand):
    print('Highe number please ;( ')
    print(f'Random number is {rand}')
    print(f"User's number is {user}")
    
elif (user == rand):
    print('Congrats! You choose the right number')
    print(f'Random number is {rand}')
    print(f"User's number is {user}")

elif (user > i):
    print('Sorry,You have choosen a wrong number.\nPlease kindly choose a right numbber.')