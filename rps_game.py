import random  # For the computer's random choice
import tkinter as tk  # For building the GUI

# Variables to keep track of the scores
player_score = 0
computer_score = 0

# Function to determine the winner and update scores
def determine_winner(player_choice):
    global player_score, computer_score  # Use the global score variables
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)  # Random choice for computer

    # Update the computer's choice label
    computer_choice_text.set(f"Computer chose: {computer_choice}")

    # Determine who wins
    if player_choice == computer_choice:
        result_text.set("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        result_text.set(f"You win! {player_choice.capitalize()} beats {computer_choice}!")
        player_score += 1
    else:
        result_text.set(f"Computer wins! {computer_choice.capitalize()} beats {player_choice}!")
        computer_score += 1

    # Update the score
    score_text.set(f"Player: {player_score} | Computer: {computer_score}")

# Function to reset the game
def reset_game():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    score_text.set("Player: 0 | Computer: 0")
    result_text.set("Let's play again!")
    computer_choice_text.set("")

# Create the main window
window = tk.Tk()
window.title("Rock, Paper, Scissors")

# Create StringVars to manage text updates
score_text = tk.StringVar()
score_text.set("Player: 0 | Computer: 0")
result_text = tk.StringVar()
result_text.set("Make your choice!")
computer_choice_text = tk.StringVar()
computer_choice_text.set("")

# Create a label to display the score
score_label = tk.Label(window, textvariable=score_text, font=('Helvetica', 14))
score_label.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(window, textvariable=result_text, font=('Helvetica', 14), fg='blue')
result_label.pack(pady=10)

# Create a label to display the computer's choice
computer_choice_label = tk.Label(window, textvariable=computer_choice_text, font=('Helvetica', 12), fg='gray')
computer_choice_label.pack(pady=10)

# Create buttons for Rock, Paper, and Scissors
tk.Button(window, text="Rock", width=15, height=2, command=lambda: determine_winner("rock")).pack(pady=5)
tk.Button(window, text="Paper", width=15, height=2, command=lambda: determine_winner("paper")).pack(pady=5)
tk.Button(window, text="Scissors", width=15, height=2, command=lambda: determine_winner("scissors")).pack(pady=5)

# Create a button to reset the game
tk.Button(window, text="Reset Game", width=15, height=2, command=reset_game).pack(pady=20)

# Start the GUI event loop
window.mainloop()

