from flask import Flask, request, redirect, url_for

app = Flask(__name__)

try:
    with open('task.txt', 'r', encoding='utf-8') as file:
        tasks = [line.strip() for line in file.readlines()]
except FileNotFoundError:
    tasks = []

@app.route('/', methods=['GET', 'POST'])
def home():
    # Если пользователь нажал кнопку и отправил данные (POST)
    if request.method == 'POST':
        new_task = request.form.get('task_name')
        if new_task:  # Если поле не пустое
            tasks.append(new_task)
            with open('tasks.txt', 'a', encoding='utf-8') as file:
                file.write(f'{new_task}\n')
            print(f"Добавлена новая задача: {new_task}") # Выведем в терминал

    # Генерируем HTML, чтобы показать задачи
    task_list_html = ""
    for index, task in enumerate(tasks):
        # Проверяем, выполнена ли задача
        if task.startswith("[+] "):
            style = "text-decoration: line-through; color: #888;"
        else:
            style = ""

        task_list_html += f"""
        <li style="display: flex; justify-content: space-between; align-items: center;">
            <span style="{style}">{task}</span>
            <div style="display: flex; gap: 10px;">
                <form action="/delete/{index}" method="POST" style="margin: 0;">
                    <button type="submit" style="background-color: #e74c3c; margin: 0;">✖</button>
                </form>
                <form action="/complete/{index}" method="POST" style="margin: 0;">
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

@app.route('/delete/<int:task_index>', methods=['POST'])
def delete_task(task_index):
    # Проверяем, существует ли такая задача
    if 0 <= task_index < len(tasks):
        # Удаляем задачу из списка в памяти
        deleted_task = tasks.pop(task_index)
        print(f"Удалена задача: {deleted_task}")
        
        # Перезаписываем файл без этой задачи
        with open('tasks.txt', 'w', encoding='utf-8') as file:
            for task in tasks:
                file.write(f"{task}\n")
                
    # Возвращаемся на главную страницу
    return redirect(url_for('home'))

@app.route('/complete/<int:task_index>', methods=['POST'])
def complete_task(task_index):
    if 0 <= task_index < len(tasks):
        # Если задача еще не выполнена, добавляем маркер
        if not tasks[task_index].startswith("[+] "):
            tasks[task_index] = "[+] " + tasks[task_index]
        
        # Перезаписываем файл
        with open('tasks.txt', 'w', encoding='utf-8') as file:
            for task in tasks:
                file.write(f"{task}\n")
                
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
