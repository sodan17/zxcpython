import sqlite3

text = input('Введите задачу которую вы хотите добавить: ')

conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()

cursor.execute('INSERT INTO tasks (title, is_done) VALUES (?, ?)', (text, 0))

conn.commit()
conn.close()
print('Задача добавлена в базу')