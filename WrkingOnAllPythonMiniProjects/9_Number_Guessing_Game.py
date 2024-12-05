import random

# Set up the game
min_value = 1
max_value = 100
secret_number = random.randint(min_value, max_value)
num_guesses = 0

# Start the game loop
while True:
    # Take input from the user
    guess = -1
    while guess not in range(min_value, max_value + 1):
        guess = int(input("Guess a number between 1 and 100: "))

    # Check if the guess is correct
    num_guesses += 1
    if guess == secret_number:
        print("Congratulations, you guessed the secret number in", num_guesses, "guesses!")
        break
    elif guess < secret_number:
        print("Too low, try again.")
    else:
        print("Too high, try again.")
