# Working with while loops and conditional statements
import random

print("The Python Guessing Number Game")


def number_guess_game():
    answer = random.randint(1, 10)
    guess_attempts = 0

    while guess_attempts < 3:
        guess = int(input("Guess a number between 0 - 10: "))
        guess_attempts += 1
        if guess == answer:
            print("You Win! :)")
            break

        else:
            print("Nope, try again")
    else:
        print(f"You Lose! The answer was {answer}")


number_guess_game()
