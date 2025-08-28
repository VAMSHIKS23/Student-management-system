import sqlite3

DB_NAME = "students.db"

def get_connection():
    """Get a connection to the SQLite database."""
    return sqlite3.connect(DB_NAME)

def init_db():
    """Initialize the students table if it doesn't exist."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            gender TEXT,
            contact TEXT,
            dob TEXT,
            address TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_student(name, email, gender, contact, dob, address):
    """Insert a new student into the students table."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO students (name, email, gender, contact, dob, address)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, email, gender, contact, dob, address))
    conn.commit()
    conn.close()

def get_all_students():
    """Retrieve all students from the students table."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, email, gender, contact, dob, address FROM students")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete_student(student_id):
    """Delete a student by ID."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()

def update_student(student_id, name, email, gender, contact, dob, address):
    """Update student details by ID."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE students
        SET name=?, email=?, gender=?, contact=?, dob=?, address=?
        WHERE id=?
    """, (name, email, gender, contact, dob, address, student_id))
    conn.commit()
    conn.close()