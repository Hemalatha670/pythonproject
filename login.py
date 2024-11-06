import tkinter as tk
from tkinter import messagebox
import mysql.connector

 
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",  
        password="",   
        database="project"   
    )

class SignupPage:
    def _init_(self, master):
        self.master = master
        self.master.title("Signup")
        self.master.geometry("500x500")
        self.master.configure(bg="white")

        tk.Label(self.master, text="Username:", bg="pink", font=("Arial", 18)).pack(pady=10)
        self.username_entry = tk.Entry(self.master, font=("Arial", 18))
        self.username_entry.pack(pady=5)

        tk.Label(self.master, text="Password:", bg="pink", font=("Arial", 18)).pack(pady=10)
        self.password_entry = tk.Entry(self.master, show="*", font=("Arial", 18))
        self.password_entry.pack(pady=5)

        tk.Button(self.master, text="Create Account", command=self.signup, bg="#4CAF50", fg="black", font=("Arial", 18)).pack(pady=10)

    def signup(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        
        if not username or not password:
            messagebox.showerror("Error", "Username and password cannot be empty!")
            return

        try:
            connection = connect_to_database()   
            cursor = connection.cursor()

            
            cursor.execute("SELECT * FROM login WHERE username = %s", (username,))
            if cursor.fetchone():
                messagebox.showerror("Error", "User already exists!")
            else:
                 
                cursor.execute("INSERT INTO login (username, password) VALUES (%s, %s)", (username, password))
                connection.commit()   

                messagebox.showinfo("Success", "Signup successful!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            cursor.close()
            connection.close()   

        self.master.destroy()   
        LoginPage(tk.Tk())   

class LoginPage:
    def _init_(self, master):
        self.master = master
        self.master.title("Login")
        self.master.geometry("500x500")
        self.master.configure(bg="white")

        tk.Label(self.master, text="Username:", bg="pink", font=("Arial", 18)).pack(pady=10)
        self.username_entry = tk.Entry(self.master, font=("Arial", 18))
        self.username_entry.pack(pady=5)

        tk.Label(self.master, text="Password:", bg="pink", font=("Arial", 18)).pack(pady=10)
        self.password_entry = tk.Entry(self.master, show="*", font=("Arial", 18))
        self.password_entry.pack(pady=5)

        tk.Button(self.master, text="Login", command=self.login, bg="#4CAF50", fg="black", font=("Arial", 18)).pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        
        if not username or not password:
            messagebox.showerror("Error", "Username and password cannot be empty!")
            return

        try:
            connection = connect_to_database()   
            cursor = connection.cursor()

             
            cursor.execute("SELECT * FROM login WHERE username = %s AND password = %s", (username, password))
            if cursor.fetchone():
                messagebox.showinfo("Success", "Login successful!")
            else:
                messagebox.showerror("Error", "Invalid username or password.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            cursor.close()
            connection.close()   

 
if _name_ == "_main_":
    root = tk.Tk()
    app = SignupPage(root)   
    root.mainloop()
