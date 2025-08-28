import tkinter as tk
from tkinter import messagebox
from db import add_student

def open_add_student_window(parent):
    win = tk.Toplevel(parent)
    win.title("Add Student")
    win.geometry("400x400")
    win.grab_set()

    labels = ["Name", "Email", "Gender", "Contact", "DOB", "Address"]
    entries = {}

    for idx, label in enumerate(labels):
        tk.Label(win, text=label+":").grid(row=idx, column=0, padx=10, pady=10, sticky='w')
        entry = tk.Entry(win, width=30)
        entry.grid(row=idx, column=1, padx=10, pady=10)
        entries[label.lower()] = entry

    def submit():
        name = entries["name"].get().strip()
        email = entries["email"].get().strip()
        gender = entries["gender"].get().strip()
        contact = entries["contact"].get().strip()
        dob = entries["dob"].get().strip()
        address = entries["address"].get().strip()

        if not name or not email:
            messagebox.showerror("Error", "Name and Email are required.")
            return

        try:
            add_student(name, email, gender, contact, dob, address)
            messagebox.showinfo("Success", "Student added successfully.")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Could not add student.\n{e}")

    tk.Button(win, text="Add Student", command=submit, width=20).grid(row=len(labels), column=0, columnspan=2, pady=20)