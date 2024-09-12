import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('school.db')

# Create a cursor object
cursor = conn.cursor()

try:
    # Start a transaction
    print("Starting transaction...")

    # Update the grade of students with age > 20 to 4.0
    cursor.execute('''
        UPDATE students
        SET grade = ?
        WHERE age > ?
    ''', (4.0, 20))

    # Commit the transaction
    conn.commit()
    print("Transaction successful: Grades updated for students with age > 20.")

except Exception as e:
    # Rollback the transaction in case of error
    conn.rollback()
    print(f"Transaction failed: {e}")

# Close the connection
conn.close()
