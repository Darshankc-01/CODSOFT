'''TASK 4
Rock-Paper-Scissors Game
User Input: Prompt the user to choose rock, paper, or scissors.
Computer Selection: Generate a random choice (rock, paper, or scissors) for the computer.
Game Logic: Determine the winner based on the user's choice and the computer's choice.
Rock beats scissors, scissors beat paper, and paper beats rock.
Display Result: Show the user's choice and the computer's choice.
Display the result, whether the user wins, loses, or it's a tie.
Score Tracking (Optional): Keep track of the user's and computer's scores for multiple rounds.
Play Again: Ask the user if they want to play another roundUser Interface: Design a user-friendly interface with clear instructions and
feedback.This project aims to create a command-line or GUI-based application
using Python'''
import tkinter as tk
import random
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"
def on_button_click(choice):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    result = determine_winner(choice, computer_choice)
    result_label.config(text="Result: " + result)
    user_choice_label.config(text="Your choice: " + choice)
    computer_choice_label.config(text="Computer's choice: " + computer_choice)
    update_score(result)
def update_score(result):
    global user_score, computer_score
    if result == "You win!":
        user_score += 1
    elif result == "You lose!":
        computer_score += 1
    score_label.config(text="Your score: " + str(user_score) + " | Computer's score: " + str(computer_score))
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_label.config(text="Your score: 0 | Computer's score: 0")
    result_label.config(text="Result: ")
    user_choice_label.config(text="Your choice: ")
    computer_choice_label.config(text="Computer's choice: ")
window = tk.Tk()
window.title("Rock-Paper-Scissors Game")
window.geometry("400x400")
user_score = 0
computer_score = 0
instructions_label = tk.Label(window, text="Choose Rock, Paper, or Scissors!", font=("Arial", 14))
instructions_label.pack(pady=10)
rock_button = tk.Button(window, text="Rock", width=15, command=lambda: on_button_click("rock"))
rock_button.pack(pady=5)
paper_button = tk.Button(window, text="Paper", width=15, command=lambda: on_button_click("paper"))
paper_button.pack(pady=5)
scissors_button = tk.Button(window, text="Scissors", width=15, command=lambda: on_button_click("scissors"))
scissors_button.pack(pady=5)
result_label = tk.Label(window, text="Result: ", font=("Arial", 12))
result_label.pack(pady=10)
user_choice_label = tk.Label(window, text="Your choice: ", font=("Arial", 12))
user_choice_label.pack(pady=5)
computer_choice_label = tk.Label(window, text="Computer's choice: ", font=("Arial", 12))
computer_choice_label.pack(pady=5)
score_label = tk.Label(window, text="Your score: 0 | Computer's score: 0", font=("Arial", 12))
score_label.pack(pady=15)
reset_button = tk.Button(window, text="Reset Game", width=15, command=reset_game)
reset_button.pack(pady=10)
window.mainloop()
