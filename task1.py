import sqlite3

try:
    connect = sqlite3.connect('school.db')

    cursor = connect.cursor()

    print("Connection to the SQLite database was successful.")

except sqlite3.Error as e:
    print(f"Error connecting to the database: {e}")

finally:
    if connect:
        connect.close()