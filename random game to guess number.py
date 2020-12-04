from random import randint

for i in range(5):
    guess = int(input("Enter a number 1 between  and 10. "))
    randNum = randint(1,10)
    if guess == randNum:
        print("We matched")
        break 
    else:
        print("We did not match. Try again")