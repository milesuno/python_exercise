# Working with while loops and conditional statements

answer = 5
guess_attempts = 0

print("The Python Guessing Number Game")
while guess_attempts < 3:
    guess = int(input("Guess a number between 0 - 10: "))
    guess_attempts += 1
    if guess == answer:
        print("You smart MoFo")
        break
    else:
        print("Nope, try again")
else:
    print("You Lose!")
