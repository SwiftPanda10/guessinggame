# Author: Samuel Bennett
# Date: 4/14/2021
# Description: A guessing game where user one enters an integer and player two attempts to guess it using looped prompts

tries = 1
print("Enter the integer for the player to guess.")
answer = int(input())
print("Enter your guess.")
guess = int(input())

while guess != answer:
    if guess < answer:
        print("Too low - try again:")
        guess = int(input())
        tries = tries + 1
    elif guess > answer:
        print("Too high - try again:")
        guess = int(input())
        tries = tries + 1

print("You guessed it in", tries, "tries.")
