#!/usr/bin/python3

# Lalita
# Parada
# Yada K.

import random
print("Welcome to the Guess the Number Game!")

print("I've generated a secret number between 1 and 100. You ave 5 guesses.")

lower_bound = 1
upper_bound = 100
answer = random.randint (lower_bound, upper_bound)

attempt = 5
while attempt != 0:
    print("Attempts left: ", attempt)
    guess = int(input("Enter your guess: "))
    if guess == answer:
        print("Congratulations! You guessed the correct number!")
        break
    elif guess < answer:
        lower_bound = guess + 1    
    elif guess > answer:
        upper_bound = guess - 1
    print("Your guess is not correct."
    f"The secret number is between {lower_bound} and {upper_bound}")
    attempt -= 1

if attempt == 0:
    print(f"You've run out guesses. The secret number was {answer}")