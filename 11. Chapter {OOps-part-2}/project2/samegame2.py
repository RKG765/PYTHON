import random

rand = random.randint(1, 100)
# print(rand)
user = None
gueses = 0
while(user != rand):
    user = int(input("Enter your number :"))
    gueses += 1
    if (user==rand):
        print("You guessed it right")
    else:
        if (user > rand):
            print('You guess was bigger than actual number')
        elif (user < rand):
            print("Your guess was smaller than actual number")
        print('Your guess was wrong.\nTry again!')
    
print(f"You guessed right number in {gueses} times")

with open("hiscore.txt",'w') as f:
    f.write(str(gueses))
