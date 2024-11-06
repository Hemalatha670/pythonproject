import tkinter as tk
import subprocess
import os


class MainMenu:
    def _init_(self, root):
        self.root = root
        self.root.title("Tic Tac Toe - Main Menu")
        self.root.geometry("400x300")   
        self.root.configure(bg='lightblue')   

        
        self.welcome_label = tk.Label(self.root, text="Welcome to Tic Tac Toe Game", font=("Arial", 20), bg='lightblue')
        self.welcome_label.pack(pady=50)

        
        self.rules_button = tk.Button(self.root, text="Show Rules 📜", font='Arial 14', width=10,
                                      bg='deepskyblue', activebackground='dodgerblue',
                                      command=self.show_rules)
        self.rules_button.pack(pady=10)
        self.button_ai = tk.Button(self.root, text="Play with AI", font=("Arial", 14), width=20, height=2,
                                   bg='lightblue', activebackground='skyblue', command=self.play_with_ai)

        self.button_2_players = tk.Button(self.root, text="2 Players", font=("Arial", 14), width=20, height=2,
                                          bg='lightblue', activebackground='skyblue', command=self.two_players)

         
        self.root.after(2000, self.show_buttons)   

    def show_buttons(self):
        """Hide the welcome message and display the buttons"""
        self.welcome_label.pack_forget()   
         
        self.button_ai.pack(pady=10)
        self.button_2_players.pack(pady=10)

    def play_with_ai(self):
        """Open the home.py page for playing with AI"""
        self.root.quit()   
        os.system('python home.py')   

    def two_players(self):
        """Open the grid.py page for 2 players"""
        self.root.quit()   
        os.system('python grid.py')   
    def show_rules(self):
        """Show the rules by running 'rules.py'"""
        subprocess.run(["python", "rules.py"])




if _name_ == "_main_":
    root = tk.Tk()
    menu = MainMenu(root)
    root.mainloop()