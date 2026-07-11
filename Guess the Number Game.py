# Guess the Number Game

import random

rand_num = random.randint(1, 100)

while True:
    user_choice = int(input("Guess the Number: "))

    if rand_num == user_choice:
        print("You won!")
        break
    elif rand_num < user_choice:
        print("You entered a too big number! Guess again :)")
    else:
        print("You entered a too small number! Guess again :)")

print("-------- GAME IS OVER --------")
