import random

n=random.randint(1,100)

while True:
    guess=int(input("Enter a Number between 1 to 100 : "))

    if guess==n:
        print("It is Correct Number ")
        break
    elif guess>n:
        print("It is Greater Number")
    elif guess<n:
        print("It is Smaller Number")
