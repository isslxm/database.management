import sqlite3

conn = sqlite3.connect('school.db')

cursor = conn.cursor()

cursor.execute('''
    DELETE FROM students
    WHERE id = ?
''', (3,))

conn.commit()

cursor.execute('SELECT * FROM students WHERE id = ?', (3,))
deleted_student = cursor.fetchone()

conn.close()

if deleted_student is None:
    print("Student with ID 3 has been successfully deleted.")
else:
    print(f"Student with ID 3 still exists: {deleted_student}")
