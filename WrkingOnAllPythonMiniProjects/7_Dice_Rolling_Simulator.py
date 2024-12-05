import random

# Set up the game
min_value = 1
max_value = 6

# Start the game loop
while True:
    # Take input from the user
    roll_again = input("Roll the dice? (y/n): ").lower()

    # Check if the user wants to roll again
    if roll_again == 'y':
        # Roll the dice
        print("Rolling the dice...")
        print("The values are:")
        dice1 = random.randint(min_value, max_value)
        dice2 = random.randint(min_value, max_value)
        print(dice1, dice2)
        print("Total value:", dice1 + dice2)
    elif roll_again == 'n':
        # Exit the game loop
        print("Goodbye!")
        break
    else:
        # Handle invalid input
        print("Invalid input. Please enter 'y' or 'n'.")
