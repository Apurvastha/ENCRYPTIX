import tkinter as tk
import random

class RockPaperScissorsGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock-Paper-Scissors Game")
        self.user_score = 0
        self.computer_score = 0

        # Create GUI elements
        self.main_frame = tk.Frame(master)
        self.main_frame.pack(pady=20)

        self.label = tk.Label(self.main_frame, text="Choose your move:", font=("Helvetica", 16, "bold"))
        self.label.pack(pady=10)

        self.choice_frame = tk.Frame(self.main_frame)
        self.choice_frame.pack()

        self.user_choice_label = tk.Label(self.choice_frame, text="Your Choice: ", font=("Helvetica", 14))
        self.user_choice_label.grid(row=0, column=0, padx=10)

        self.computer_choice_label = tk.Label(self.choice_frame, text="Computer's Choice: ", font=("Helvetica", 14))
        self.computer_choice_label.grid(row=1, column=0, padx=10)

        self.result_label = tk.Label(self.main_frame, text="", font=("Helvetica", 16, "bold"))
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(self.main_frame, text=f"Score: You {self.user_score} - {self.computer_score} Computer", font=("Helvetica", 14))
        self.score_label.pack()

        self.button_frame = tk.Frame(self.main_frame)
        self.button_frame.pack(pady=10)

        self.rock_button = tk.Button(self.button_frame, text="Rock", font=("Helvetica", 14), bg="#D3D3D3", activebackground="#A9A9A9", padx=20, pady=10, command=lambda: self.play_game("rock"))
        self.rock_button.pack(side=tk.LEFT, padx=10)

        self.paper_button = tk.Button(self.button_frame, text="Paper", font=("Helvetica", 14), bg="#D3D3D3", activebackground="#A9A9A9", padx=20, pady=10, command=lambda: self.play_game("paper"))
        self.paper_button.pack(side=tk.LEFT, padx=10)

        self.scissors_button = tk.Button(self.button_frame, text="Scissors", font=("Helvetica", 14), bg="#D3D3D3", activebackground="#A9A9A9", padx=20, pady=10, command=lambda: self.play_game("scissors"))
        self.scissors_button.pack(side=tk.LEFT, padx=10)

    # Rest of the code remains the same...

    def play_game(self, user_choice):
        computer_choice = random.choice(["rock", "paper", "scissors"])
        self.update_choice_labels(user_choice, computer_choice)

        result = self.determine_winner(user_choice, computer_choice)
        self.update_result_label(result)
        self.update_score(result)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            return "You win!"
        else:
            return "Computer wins!"

    def update_choice_labels(self, user_choice, computer_choice):
        self.user_choice_label.config(text=f"Your Choice: {user_choice.capitalize()}")
        self.computer_choice_label.config(text=f"Computer's Choice: {computer_choice.capitalize()}")

    def update_result_label(self, result):
        self.result_label.config(text=result)

    def update_score(self, result):
        if result == "You win!":
            self.user_score += 1
        elif result == "Computer wins!":
            self.computer_score += 1
        self.score_label.config(text=f"Score: You {self.user_score} - {self.computer_score} Computer")

root = tk.Tk()
game = RockPaperScissorsGUI(root)
root.mainloop()