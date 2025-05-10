import sqlite3
from MySQLdb import connect
conn = sqlite3,connect("school.db")
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS student (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        grade TEXT
    )
''')
cursor.execute("INSERT INTO students VALUES(?,?,?,?)",(1,"Alice",14,"A"))
cursor.execute("INSERT INTO students VALUES(?,?,?,?)",(2,"Bob",15,"B"))
cursor.execute("INSERT INTO students VALUES(?,?,?,?)",(3,"Charlie",14,"A"))
cursor.execute("SELECT *FROM students")
for row in cursor.fetchail():
 print(row)
cursor.execute("UPDATE students SET grade = ? WHERE name = ?",("A+","Bob"))
conn.commit()
cursor.execute("DELETE FROM students WHERE id = ?",(3,))
conn.commit()
cursor.close()
conn.close()