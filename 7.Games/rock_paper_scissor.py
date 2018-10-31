from random import randint

user = input("rock,paper,scissors ?")
pick = randint(1,3)
if (pick == 1):
    computer = "rock"
    print("0")
elif (pick == 2):
    computer = "paper"
    print("-_-")
else:
    computer = "scissors"
    print("god damn not again -_-")
if (user == computer):
    print("DRAW")
elif(user == "rock" and computer == "paper"):
    print("player winns!")
elif(user == "paper" and computer == "rock" ):
    print("computer wins !")
elif(user == "scissors" and computer == "paper"):
    print("player wins !")
elif(user == "paper" and computer =="scissors"):
    print("computer wins !")
elif(user == "scissors" and computer == "rock"):
    print("computer wins !")
elif(user == "rock" and computer == "scissors"):
    print("player wins !")
else:
    print("what? :(")


