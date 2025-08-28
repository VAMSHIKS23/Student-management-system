import tkinter as tk
from tkinter import ttk, messagebox
from db import get_all_students, delete_student, update_student

def open_student_table_window(parent):
    win = tk.Toplevel(parent)
    win.title("All Students")
    win.geometry("950x500")
    win.grab_set()

    # Search Bar
    search_frame = tk.Frame(win)
    search_frame.pack(padx=10, pady=5, fill=tk.X)
    tk.Label(search_frame, text="Search by Name or Email:").pack(side=tk.LEFT)
    search_var = tk.StringVar()
    search_entry = tk.Entry(search_frame, textvariable=search_var, width=40)
    search_entry.pack(side=tk.LEFT, padx=5)

    # Table
    cols = ("ID", "Name", "Email", "Gender", "Contact", "DOB", "Address")
    tree = ttk.Treeview(win, columns=cols, show='headings')
    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, width=120)
    tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    def refresh_table():
        students = get_all_students()
        filter_text = search_var.get().lower()
        for row in tree.get_children():
            tree.delete(row)
        for row in students:
            # Filter by name or email
            if filter_text in row[1].lower() or filter_text in row[2].lower():
                tree.insert("", tk.END, values=row)

    def on_search(*args):
        refresh_table()

    def edit_student():
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "No student selected.")
            return
        item = tree.item(selected[0], "values")
        edit_window(item)

    def delete_selected_student():
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "No student selected.")
            return
        item = tree.item(selected[0], "values")
        student_id = item[0]
        confirm = messagebox.askyesno("Confirm Delete", f"Delete student {item[1]}?")
        if confirm:
            delete_student(student_id)
            refresh_table()
            messagebox.showinfo("Deleted", "Student deleted successfully.")

    def edit_window(student):
        edit_win = tk.Toplevel(win)
        edit_win.title("Edit Student")
        edit_win.geometry("400x400")
        labels = ["Name", "Email", "Gender", "Contact", "DOB", "Address"]
        entries = {}

        for idx, label in enumerate(labels):
            tk.Label(edit_win, text=label+":").grid(row=idx, column=0, padx=10, pady=10, sticky='w')
            entry = tk.Entry(edit_win, width=30)
            entry.insert(0, student[idx+1])  # skip ID
            entry.grid(row=idx, column=1, padx=10, pady=10)
            entries[label.lower()] = entry

        def save_changes():
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
                update_student(student[0], name, email, gender, contact, dob, address)
                messagebox.showinfo("Success", "Student updated successfully.")
                edit_win.destroy()
                refresh_table()
            except Exception as e:
                messagebox.showerror("Error", f"Could not update student.\n{e}")

        tk.Button(edit_win, text="Save Changes", command=save_changes, width=20).grid(row=len(labels), column=0, columnspan=2, pady=20)

    # Button Frame
    btn_frame = tk.Frame(win)
    btn_frame.pack(fill=tk.X, pady=5)
    tk.Button(btn_frame, text="Edit Selected", command=edit_student, width=15).pack(side=tk.LEFT, padx=10)
    tk.Button(btn_frame, text="Delete Selected", command=delete_selected_student, width=15).pack(side=tk.LEFT, padx=10)
    tk.Button(btn_frame, text="Refresh", command=refresh_table, width=10).pack(side=tk.LEFT, padx=10)
    tk.Button(btn_frame, text="Close", command=win.destroy, width=10).pack(side=tk.RIGHT, padx=10)

    # Bind search
    search_var.trace_add('write', lambda *args: on_search())

    refresh_table()