import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('student_management.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE students (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             first_name TEXT NOT NULL,
             last_name TEXT NOT NULL,
             course TEXT NOT NULL,
             subject TEXT NOT NULL,
             year INTEGER NOT NULL,
             age INTEGER NOT NULL,
             gender TEXT NOT NULL,
             birthday TEXT NOT NULL,
             contact TEXT NOT NULL,
             email TEXT NOT NULL)''')

# Commit and close connection
conn.commit()
conn.close()

print("Database and table created successfully.")
