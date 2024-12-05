import random

# Set up the game
words = ['python', 'programming', 'computer', 'science', 'software', 'development']
word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0

# Define the function to display the hangman
def display_hangman():
    if incorrect_guesses == 0:
        print("  +---+")
        print("      |")
        print("      |")
        print("      |")
        print("      |")
        print("      |")
        print("=========")
    elif incorrect_guesses == 1:
        print("  +---+")
        print("  |   |")
        print("      |")
        print("      |")
        print("      |")
        print("      |")
        print("=========")
    elif incorrect_guesses == 2:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print("      |")
        print("      |")
        print("      |")
        print("=========")
    elif incorrect_guesses == 3:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print("  |   |")
        print("      |")
        print("      |")
        print("=========")
    elif incorrect_guesses == 4:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(" /|   |")
        print("      |")
        print("      |")
        print("=========")
    elif incorrect_guesses == 5:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(" /|\  |")
        print("      |")
        print("      |")
        print("=========")
    else:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(" /|\  |")
        print(" /    |")
        print("      |")
        print("=========")
        print("You lose! The word was:", word)
        return True
    return False

# Start the game loop
while True:
    # Display the hangman and the word
    print()
    display_hangman()
    print()
    for letter in word:
        if letter in guessed_letters:
            print(letter, end=' ')
        else:
            print('_', end=' ')
    print()

    # Check if the player has won
    if all(letter in guessed_letters for letter in word):
        print("You win!")
        break

    # Take input from the user
    guess = input("Guess a letter: ").lower()

    # Check if the letter has already been guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add the letter to the guessed letters list
    guessed_letters.append(guess)

    # Check if the letter is in the word
    if guess not in word:
        incorrect_guesses += 1
        if incorrect_guesses == 6:
            print("You lose! The word was:", word)
            break
        print("Incorrect guess.")
