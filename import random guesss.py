import random
num=random.radint(1,20)


while true:
    guess=int(input("guess a Number between 1 to 20:"))
    if guess==num:
        print("you Guessed a correct number")
        break
    elif guess>num:
        print("You Guessed A greater number")
        
