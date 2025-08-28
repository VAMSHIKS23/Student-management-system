from db import init_db
from login import show_login
from student_form import open_add_student_window
from student_table import open_student_table_window
import tkinter as tk

def main_window():
    root = tk.Tk()
    root.title("Student Management System")
    root.geometry("500x300")

    # Menu Bar
    menubar = tk.Menu(root)
    student_menu = tk.Menu(menubar, tearoff=0)
    student_menu.add_command(label="Add Student", command=lambda: open_add_student_window(root))
    student_menu.add_command(label="View Students", command=lambda: open_student_table_window(root))
    student_menu.add_separator()
    student_menu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="Student", menu=student_menu)

    root.config(menu=menubar)

    tk.Label(root, text="Welcome to the Student Management System!", font=("Arial", 14)).pack(pady=80)
    root.mainloop()

if __name__ == "__main__":
    init_db()
    show_login(main_window)