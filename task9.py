import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('school.db')

# Create a cursor object
cursor = conn.cursor()

# Record with duplicate id = 1
duplicate_student = (1, 'Alice', 20, 3.8, 'alice@example.com')

try:
    # Try inserting the duplicate record
    cursor.execute('''
        INSERT INTO students (id, name, age, grade, email)
        VALUES (?, ?, ?, ?, ?)
    ''', duplicate_student)

    # Commit the changes
    conn.commit()
    print("Record inserted successfully.")
    
except sqlite3.IntegrityError as e:
    # Handle the IntegrityError when trying to insert a duplicate
    print(f"Error: Cannot insert duplicate record with id = 1. {e}")

# Close the connection
conn.close()
