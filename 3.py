import tkinter as tk
from tkinter import messagebox
import subprocess   
class TicTacToe:
    def _init_(self, root):
        self.root = root
        self.root.title("3x3 Tic Tac Toe")
        self.root.geometry("400x400")
        self.root.configure(bg='lightblue')   

         
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = "🦋"   

         
        self.buttons = [
            [tk.Button(self.root, text='', font='Arial 20', width=5, height=2,
                       bg='lightblue', activebackground='skyblue',
                       command=lambda row=row, col=col: self.on_button_click(row, col))
             for col in range(3)] for row in range(3)
        ]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].grid(row=row, column=col)

         
        self.restart_button = tk.Button(self.root, text="Restart", command=self.reset_board, font=("Arial", 14),
                                        bg='lightblue', activebackground='skyblue')
        self.restart_button.grid(row=3, column=0, columnspan=3)

         
        self.home_button = tk.Button(self.root, text="Home", command=self.go_home, font=("Arial", 14),
                                     bg='lightblue', activebackground='skyblue')
        self.home_button.grid(row=4, column=0, columnspan=3)

    def on_button_click(self, row, col):
        """Handle button click event"""
        if self.board[row][col] == '':   
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

             
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_board()
            elif all(self.board[r][c] != '' for r in range(3) for c in range(3)):   
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_board()
            else:
                 
                self.current_player = "🐣" if self.current_player == "🦋" else "🦋"

    def check_winner(self):
        """Check if the current player has won"""
         
        for i in range(3):
            if all(self.board[i][j] == self.current_player for j in range(3)):  
                return True
            if all(self.board[j][i] == self.current_player for j in range(3)):   
                return True

        
        if all(self.board[i][i] == self.current_player for i in range(3)):   
            return True
        if all(self.board[i][2 - i] == self.current_player for i in range(3)):   
            return True
        return False

    def reset_board(self):
        """Reset the game board"""
        self.board = [['' for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text='')
        self.current_player = "🦋"   
    def go_home(self):
        """Go back to the main menu or close the game by opening players.py"""
        self.root.quit()   
        subprocess.run(["python", "players.py"])   

if _name_ == "_main_":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
