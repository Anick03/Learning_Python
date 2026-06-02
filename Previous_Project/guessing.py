import random

BOLD = '\033[1m'
END = '\033[0m'
secret_number = random.randint(1,50)
attempts = 0
print("")
print("")
print(BOLD + "                        Welcome to the Number Guessing Game!" + END)
print(BOLD + "                      You have 10 attemps to guess the number. " + END)
while True:
    guess = int(input("Enter your guessed number between 1 to 50: "))
    attempts = attempts + 1

    if attempts == 10:
        print("Unfortunately your attempts are over !")
        print(BOLD + f"The actual number is {secret_number}" + END)
        break
    elif guess < secret_number:
        print("It's low! Try again.")
    elif guess + 10 < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("It's high! Try again.")
    elif guess - 10 > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break
