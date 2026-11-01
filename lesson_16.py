import sqlite3

# 1. Подключаемся к базе (если файла нет, он создастся)
conn = sqlite3.connect('tasks.db')

# 2. Создаем курсор (руку, которая будет работать с базой)
cursor = conn.cursor()

# 3. Выполняем SQL-команду: создаем таблицу tasks
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        is_done INTEGER DEFAULT 0
    )
''')

# 4. Сохраняем изменения (подтверждаем)
conn.commit()

# 5. Закрываем соединение
conn.close()

print('База данных и таблица успешно созданы!')
