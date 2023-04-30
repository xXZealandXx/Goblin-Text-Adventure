import random

# define the options
options = ["rock", "paper", "scissors"]

# get user input
user_choice = input("Enter your choice (rock/paper/scissors): ").lower()

# generate random computer choice
computer_choice = random.choice(options)

# determine the winner
if user_choice == computer_choice:
    result = "Tie!"
elif user_choice == "rock":
    if computer_choice == "paper":
        result = "Computer wins!"
    else:
        result = "You win!"
elif user_choice == "paper":
    if computer_choice == "scissors":
        result = "Computer wins!"
    else:
        result = "You win!"
elif user_choice == "scissors":
    if computer_choice == "rock":
        result = "Computer wins!"
    else:
        result = "You win!"
else:
    result = "Invalid input! You lose."

# print the results
print(f"You chose {user_choice} and the computer chose {computer_choice}. {result}")
