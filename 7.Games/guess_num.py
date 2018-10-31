import random
print("Hey what's your name ?")
name = input()
secretnumber = random.randint(1,20)
print(name + "i am thinking number between 1 to 20")
for guess in range(1,7):
    print("take a guess")
    guess = int(input())
    if guess < secretnumber:
        print("your guess is too low")
    elif guess > secretnumber:
        print("your guess is to high")
    else:
        break
if guess == secretnumber:
    print("congo,"+ name + "you gussed the correct number")
else:
    print("sorry. the number was " + str(secretnumber))


