#project 8
#number guessing game


import random
n=random.randint(1,10)
guess =int(input(" enter a number from 1 to 10:"))
while True:
        if guess < n:
            print("your guess is low")
            guess=int(input(" try again"))
        elif guess > n:
            print(" your guess is high")
            guess =int(input(" try again"))
        else:
            print("your guess is correct")
            break
