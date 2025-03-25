import random

top_of_range = input("Enter the top of the range: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please enter a positive number.")
        quit()
else:
    print("Please enter a number.")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    guess = input("Guess a number: ")
    if guess.isdigit():
        user_guess = int(guess)
    else:
        print("Please enter a number.")
        continue

    if user_guess == random_number:
        print("You got it")
        break
    elif user_guess < random_number:
        print("Too low!")


