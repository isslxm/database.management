import sqlite3

conn = sqlite3.connect('school.db')

cursor = conn.cursor()

cursor.execute('''
    UPDATE students
    SET grade = ?
    WHERE id = ?
''', (3.7, 2))

conn.commit()

cursor.execute('SELECT * FROM students WHERE id = ?', (2,))
updated_student = cursor.fetchone()

conn.close()

if updated_student:
    id, name, age, grade = updated_student
    print("Updated Record:")
    print(f"ID: {id}, Name: {name}, Age: {age}, Grade: {grade:.2f}")
else:
    print("No student found with the given ID.")
