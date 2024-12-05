import random

# Define the choices
choices = ["rock", "paper", "scissors"]

# Take input from the user
user_choice = input("Choose rock, paper, or scissors: ")

# Choose a random choice for the computer
computer_choice = random.choice(choices)

# Print the choices
print("You chose:", user_choice)
print("The computer chose:", computer_choice)

# Determine the winner
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You win!")
elif user_choice == "paper" and computer_choice == "rock":
    print("You win!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You win!")
else:
    print("The computer wins!")
