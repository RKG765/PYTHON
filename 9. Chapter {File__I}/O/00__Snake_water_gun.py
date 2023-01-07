# doing a project in which  making  a small game 
import random


def game(comp,player):
    if comp == player:
        return None
    elif comp == 's':
        if player == 'w':
            return False
        elif player == 'g':
            return True
    elif comp == 'w':
        if player == 'g':
            return False
        elif player == 'w':
            return True
    elif comp == 'g':
        if player == 's':
            return False
        elif player == 'w':
            return True


randnum = random.randint(1,3)

comp = print("Computer's turn")
player = input("Your's turn: snake(s) water(w) or gun(g) : ")
if randnum == 1:
    comp = 's'
elif randnum == 2:
    comp = 'w'
elif randnum == 3:
    comp = 'g'

a = game(comp,player)

print(f"computer chose: {comp}")
print(f"You chose: {player}")

if a == None:
    print("Match tie")
elif a == True:
    print("you win")
elif a == False:
    print("you lose")
