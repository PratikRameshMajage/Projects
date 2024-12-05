import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.current_player = "X"
        self.board = [" "]*9
        self.winning_combinations = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe")

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.root, text="", width=10, height=5, command=lambda i=i, j=j: self.button_click(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

        reset_button = tk.Button(self.root, text="Reset", command=self.reset)
        reset_button.grid(row=3, column=1)

    def button_click(self, row, col):
        button = self.buttons[row][col]
        if button["text"] == "":
            button["text"] = self.current_player
            self.board[row*3+col] = self.current_player
            if self.check_win():
                messagebox.showinfo("Tic-Tac-Toe", f"{self.current_player} wins!")
                self.reset()
            elif self.check_tie():
                messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
                self.reset()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_win(self):
        for combination in self.winning_combinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] != " ":
                return True
        return False

    def check_tie(self):
        return " " not in self.board

    def reset(self):
        self.current_player = "X"
        self.board = [" "]*9
        for row in self.buttons:
            for button in row:
                button["text"] = ""

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
