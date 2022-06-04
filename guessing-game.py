#!/usr/bin/python3

from random import randint

secret:int = randint(1, 100)

print("An integer has been selected by random by the computer [1 to 100].")

guess:int = int(input("Please input your guess: "))

while guess != secret:
    if guess > secret:
        print("Too high")
    elif guess < secret:
        print("Too low")
    else:
        break
    guess = int(input("Guess again: "))


print("You won the game.")