import sqlite3

conn = sqlite3.connect('school.db')

cursor = conn.cursor()

cursor.execute('SELECT * FROM students')

students = cursor.fetchall()

conn.close()

print("ID | Name     | Age | Grade")
print("----------------------------")
for student in students:
    id, name, age, grade = student
    print(f"{id:2} | {name:8} | {age:3} | {grade:.2f}")
