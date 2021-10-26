#importing necessary libraries
import random as rd
#take guessed number as input
x=rd.randrange(1,100)
#guessing the number
for i in range(0,7):
    guess=int(input("Guess the number"))
    if guess==x:
        print("You won")
        break
    else:
        print("Sorry! you are wrong")
        if guess>x:
            print("you are guessing higher number")
        else:
            print("you are guessing lower number")