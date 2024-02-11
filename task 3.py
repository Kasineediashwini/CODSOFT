import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the winner of the game
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

# Function to play the game
def play_game():
    user_choice = user_var.get()
    computer_choice = random.choice(choices)

    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"Computer's Choice: {computer_choice}\n{result}")

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

# Choices for the game
choices = ["rock", "paper", "scissors"]

# Create and place widgets
instruction_label = tk.Label(root, text="Choose rock, paper, or scissors:")
instruction_label.pack()

user_var = tk.StringVar()
user_var.set("rock") # default choice
choices_radio = tk.Frame(root)
for choice in choices:
    radio = tk.Radiobutton(choices_radio, text=choice.capitalize(), variable=user_var, value=choice)
    radio.pack(side=tk.LEFT)
choices_radio.pack()

play_button = tk.Button(root, text="Play", command=play_game)
play_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Run the main event loop
root.mainloop()
