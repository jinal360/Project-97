import random

number = random.random(1,9)

while chance < 5:

    if guess == number:
        print("Congratulation YOU WON !!!")
        break
    if not chances < 5:
        print ("YOU LOSE!!! The number is", number)