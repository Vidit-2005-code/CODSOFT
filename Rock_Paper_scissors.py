import tkinter as tk
import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or (user == "scissors" and computer == "paper") or (user == "paper" and computer == "rock"):
        return "win"
    else:
        return "lose"


def play(user_choice):
    global user_score, computer_score

    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)

    computer_choice_label.config(text=f"Computer chose: {computer_choice}")
    user_choice_label.config(text=f"You chose: {user_choice}")
    if result == "tie":
        result_label.config(text="It's a tie!")
    elif result == "win":
        user_score += 1
        result_label.config(text="You win.")
    else:
        computer_score += 1
        result_label.config(text="You lose.")

    score_label.config(text=f"Score >> You: {user_score} | Computer: {computer_score}")


def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="Let's play!")
    computer_choice_label.config(text="Computer chose: ?")
    score_label.config(text=f"Score >> You: 0 | Computer: 0")


user_score = 0
computer_score = 0

window = tk.Tk()
window.title("Rock, Paper, Scissors")
window.geometry("500x400")
window.resizable(False, False)

title_label = tk.Label(window, text="Rock, Paper, Scissors", font=("Calibri", 24,"bold"),fg="red")
title_label.pack(pady=10)

label = tk.Label(window, text="-"*75)
label.pack()

result_label = tk.Label(window, text="Let's play!", font=("Calibri", 20,"bold"), fg="blue")
result_label.pack(pady=10)

computer_choice_label = tk.Label(window, text="Computer chose: ?", font=("Calibri", 14))
computer_choice_label.pack()

user_choice_label = tk.Label(window, text="You chose: ?", font=("Calibri", 14))
user_choice_label.pack()

score_label = tk.Label(window, text="Score >> You: 0 | Computer: 0", font=("Calibri", 14),bg="pink")
score_label.pack()

button_frame = tk.Frame(window)
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", width=10,bg="cyan", command=lambda: play("rock"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", width=10,bg="cyan", command=lambda: play("paper"))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", width=10,bg="cyan", command=lambda: play("scissors"))
scissors_button.grid(row=0, column=2, padx=10)

reset_button = tk.Button(window, text="Reset Game",bg="black",fg="white", command=reset_game)
reset_button.pack(pady=10)

label = tk.Label(window, text="-"*75)
label.pack()

window.mainloop()
