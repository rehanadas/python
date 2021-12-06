import random

number = random.randrange(1, 10)
guess = input("Please guess a number between 1 and 9.")
guess = int(guess)
if guess not in range(1, 10):
    print("You have to guess a number between 1 and 9!")
elif guess < number:
    print("You've guessed too low!")
elif guess > number:
    print("You've guessed too high!")
elif guess == number:
    print("You've guessed exactly right!")
print("The random number is: ", number)