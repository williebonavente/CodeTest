import tkinter as tk
import random

class GuessTheNumberGame:
    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        self.window = tk.Tk()
        self.window.title("Guess the Number Game")
        self.window.geometry("400x200")

        self.label = tk.Label(self.window, text="I have a secret number between 1 and 100.\nCan you guess it?")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.window)
        self.entry.pack()

        self.button = tk.Button(self.window, text="Guess", command=self.check_guess)
        self.button.pack(pady=10)

        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack()

        self.window.mainloop()

    def check_guess(self):
        guess = int(self.entry.get())
        self.attempts += 1

        if guess == self.secret_number:
            self.result_label.config(text=f"Congratulations! You guessed the correct number {self.secret_number} in {self.attempts} attempts.")
        elif guess < self.secret_number:
            self.result_label.config(text="Too low. Try again.")
        else:
            self.result_label.config(text="Too high. Try again.")

if __name__ == "__main__":
    game = GuessTheNumberGame()
