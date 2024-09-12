import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('school.db')

# Create a cursor object
cursor = conn.cursor()

# Add a new column 'email' to the students table
cursor.execute('''
    ALTER TABLE students
    ADD COLUMN email TEXT
''')

# Commit the changes
conn.commit()

# Query the table schema to verify the column was added
cursor.execute('PRAGMA table_info(students)')

# Fetch and print the table schema
schema = cursor.fetchall()

# Close the connection
conn.close()

# Print the table schema
print("Table Schema:")
print("cid | Name    | Type    | Not Null | Default Value | Primary Key")
print("---------------------------------------------------------------")
for column in schema:
    print(f"{column[0]:3} | {column[1]:7} | {column[2]:7} | {column[3]:8} | {column[4] or 'NULL':12} | {column[5]}")
