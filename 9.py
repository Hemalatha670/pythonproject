import tkinter as tk
from tkinter import messagebox
import os

class TicTacToe:
    def _init_(self, root):
        self.root = root
        self.root.title("9x9 Tic Tac Toe")
        self.root.geometry("600x600")
        self.root.configure(bg='lightblue')   

         
        self.board = [['' for _ in range(9)] for _ in range(9)]
        self.current_player = "🦋"   

        
        self.instruction_label = tk.Label(self.root, text="5 in a row!", font=("Arial", 20), bg='blue')
        self.instruction_label.grid(row=0, column=0, columnspan=9)

         
        self.buttons = [
            [tk.Button(self.root, text='', font='Arial 14', width=4, height=2,
                       bg='lightblue', activebackground='blue',
                       command=lambda row=row, col=col: self.on_button_click(row, col))
             for col in range(9)] for row in range(9)
        ]

        for row in range(9):
            for col in range(9):
                self.buttons[row][col].grid(row=row + 1, column=col)   

         
        self.restart_button = tk.Button(self.root, text="Restart", command=self.reset_board, font=("Arial", 14),
                                        bg='lightblue', activebackground='skyblue')
        self.restart_button.grid(row=10, column=0, columnspan=9)

         
        self.home_button = tk.Button(self.root, text="Home", command=self.go_home, font=("Arial", 14),
                                     bg='lightblue', activebackground='skyblue')
        self.home_button.grid(row=11, column=0, columnspan=9)

    def on_button_click(self, row, col):
        """Handle button click event"""
        if self.board[row][col] == '':   
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

             
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_board()
            elif all(self.board[r][c] != '' for r in range(9) for c in range(9)):   
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_board()
            else:
                 
                self.current_player = "🐣" if self.current_player == "🦋" else "🦋"

    def check_winner(self):
        """Check if the current player has won"""
        
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == self.current_player:
                     
                    if j + 4 < 9 and all(self.board[i][j + k] == self.current_player for k in range(5)):
                        return True
                     
                    if i + 4 < 9 and all(self.board[i + k][j] == self.current_player for k in range(5)):
                        return True
                     
                    if i + 4 < 9 and j + 4 < 9 and all(self.board[i + k][j + k] == self.current_player for k in range(5)):
                        return True
                     
                    if i + 4 < 9 and j - 4 >= 0 and all(self.board[i + k][j - k] == self.current_player for k in range(5)):
                        return True
        return False

    def reset_board(self):
        """Reset the game board"""
        self.board = [['' for _ in range(9)] for _ in range(9)]
        for row in range(9):
            for col in range(9):
                self.buttons[row][col].config(text='')
        self.current_player = "🦋"   

    def go_home(self):
        """Redirect to home.py"""
        self.root.quit()   
        os.system('python players.py')   

if _name_ == "_main_":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
