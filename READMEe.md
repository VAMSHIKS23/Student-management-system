# Student Management System

A desktop application built with **Python**, **Tkinter**, and **SQLite** for managing student records efficiently. This project demonstrates core concepts of GUI programming, database integration, and CRUD operations.

---

## **Features**

- **Login System:** Secure login window to restrict access.
- **Add Student:** Form to add new student records (Name, Email, Gender, Contact, DOB, Address).
- **View Students:** Table view (with search/filter) for all students.
- **Edit/Delete Students:** Update or remove existing student records.
- **Search/Filter:** Instantly search students by name or email.
- **User-Friendly UI:** Menu-driven interface using Tkinter.

---

## **Technologies Used**

- **Python 3**
- **Tkinter** (GUI)
- **SQLite** (Database - can be replaced with MySQL/PostgreSQL)
- **Standard Python libraries**

---

## **Project Structure**

```
project/
│
├── db.py               # Database connection and CRUD functions
├── main.py             # Main application launcher and menu
├── login.py            # Login window and authentication logic
├── student_form.py     # Add/edit student form
├── student_table.py    # Table view, search, edit, delete features
├── README.md           # Project documentation
└── students.db         # SQLite database file (auto-generated)
```

---

## **How to Run**

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/student-management-system.git
   cd student-management-system
   ```

2. **Install Python 3** (if not already installed).

3. **Run the application:**
   ```sh
   python main.py
   ```

4. **Login credentials:**  
   The default credentials can be found/set in `login.py`. (e.g., username: `admin`, password: `admin`)

---
