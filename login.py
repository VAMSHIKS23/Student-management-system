import tkinter as tk
from tkinter import messagebox

USERNAME = "admin"
PASSWORD = "admin123"

def show_login(on_success):
    def try_login():
        user = username_var.get()
        pw = password_var.get()
        if user == USERNAME and pw == PASSWORD:
            login_win.destroy()
            on_success()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    login_win = tk.Tk()
    login_win.title("Login - Student Management System")
    login_win.geometry("300x180")

    tk.Label(login_win, text="Username:").pack(pady=(20,0))
    username_var = tk.StringVar()
    tk.Entry(login_win, textvariable=username_var).pack()

    tk.Label(login_win, text="Password:").pack(pady=(10,0))
    password_var = tk.StringVar()
    tk.Entry(login_win, textvariable=password_var, show="*").pack()

    tk.Button(login_win, text="Login", width=15, command=try_login).pack(pady=20)
    login_win.mainloop()