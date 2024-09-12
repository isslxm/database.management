import sqlite3

conn = sqlite3.connect('school.db')

cursor = conn.cursor()

students_data = [
    (1, 'Alice', 20, 3.8),
    (2, 'Bob', 21, 3.5),
    (3, 'Charlie', 22, 3.9)
]


cursor.executemany('''
    INSERT INTO students (id, name, age, grade)
    VALUES (?, ?, ?, ?)
''', students_data)

conn.commit()

conn.close()

print("Records inserted successfully.")
