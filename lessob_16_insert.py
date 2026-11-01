import sqlite3

text = input('Введите задачу которую вы хотите добавить: ')

conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()

cursor.execute('INSERT INTO tasks (title, is_done) VALUES (?, ?)', (text, 0))

conn.commit()
conn.close()
print('Задача добавлена в базу')

conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM tasks')
tasks = cursor.fetchall()

for task in tasks:
    print(tasks)

conn.close()