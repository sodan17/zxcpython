import sqlite3
from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    # Если пользователь нажал кнопку и отправил данные (POST)
    if request.method == 'POST':
        new_task = request.form.get('task_name')
        if new_task: # Если поле не пустое
            # Добавляем в базу (SQL-команда INSERT)
            cursor.execute('INSERT INTO tasks (title) VALUES (?)', (new_task,))
            conn.commit()

     # Получаем все задачи из базы (SQL-команда SELECT)
    cursor.execute('SELECT * FROM tasks')
    db_tasks = cursor.fetchall()
    conn.close()

    # Генерируем HTML, чтобы показать задачи
    task_list_html = ""

    for db_task in db_tasks:
        task_id = db_task[0]
        task_title = db_task[1]
        task_is_done = db_task[2]

        if task_is_done == 1:
            style = 'text-decoration: line-through; color: #888;'
        else:
            style = ""

        task_list_html += f"""
        <li style="display: flex; justify-content: space-between; align-items: center;">
            <span style="{style}">{task_title}</span>
            <div style="display: flex; gap: 10px;">
                <form action="/delete/{task_id}" method="POST" style="margin: 0;">
                    <button type="submit" style="background-color: #e74c3c; margin: 0;">✖</button>
                </form>
                <form action="/complete/{task_id}" method="POST" style="margin: 0;">
                    <button type="submit" style="background-color: #2ecc71; margin: 0;">✔</button>
                </form>
            </div>
        </li>
        """
    

    html_page = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Мой Менеджер Задач</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                color: #333;
                max-width: 600px;
                margin: 40px auto; /* Центрируем страницу */
                padding: 20px;
            }}
            h1 {{ color: #2c3e50; }}
            input[type="text"] {{
                padding: 10px;
                width: 70%;
                border: 1px solid #ccc;
                border-radius: 5px;
            }}
            button {{
                padding: 10px 15px;
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }}
            button:hover {{ background-color: #2980b9; }}
            ul {{ list-style-type: none; padding: 0; }}
            li {{
                background: white;
                margin: 10px 0;
                padding: 10px;
                border-radius: 5px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        </style>
    </head>
    <body>
        <h1>Добро пожаловать в Менеджер Задач!</h1>
        
        <!-- Вот наша форма! -->
        <form method="POST">
            <input type="text" name="task_name" placeholder="Введите задачу...">
            <button type="submit">Добавить задачу</button>
        </form>

        <h2>Мои задачи:</h2>
        <ul>
            {task_list_html}
        </ul>
    </body>
    </html>
    """
    return html_page

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):

    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))

    conn.commit()
    conn.close()

    # Возвращаемся на главную страницу
    return redirect(url_for('home'))

@app.route('/complete/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    # 1. Подключаемся к базе
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()

    # 2. Говорим базе: "Обнови строку, установи is_done = 1, где id равен task_id"
    cursor.execute("UPDATE tasks SET is_done = 1 WHERE id = ?", (task_id,))

    # 3. Сохраняем и закрываем
    conn.commit()
    conn.close()

    # 4. Возвращаемся на главную
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
