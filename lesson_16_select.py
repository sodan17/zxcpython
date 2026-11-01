import sqlite3

conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM tasks')
tasks = cursor.fetchall()

for id, title, is_done in tasks:
    if is_done == 1:
        status = '(Выполнено)'
    else:
        status = '(Не выполнено)'

    print(f'{id}. {title} {status}')

conn.close()