class Task:
    def __init__(self, title):
        self.title = title
        self.is_done = False

    def mark_done(self):
        self.is_done = True

# --- ЗАГРУЗКА ЗАДАЧ ИЗ ФАЙЛА ---
try:

    with open('tasks.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        tasks =[]
        for line in lines:
            new_task = Task(line.strip())
            tasks.append(new_task)
except FileNotFoundError:
    tasks = []


# --- ОСНОВНАЯ ПРОГРАММА ---
while True:
    print('\n--- МЕНЕДЖЕР ЗАДАЧ ---')
    print('1. Добавить задачу')
    print('2. Показать все задачи')
    print('3. Выход')
    print('4. Отметить задачу выполненой')

    choice = input('Ваш выбор: ')

    if choice == '1':
        task_text = input('Что нужно сделать? ')
        new_task = Task(task_text)
        tasks.append(new_task)

        with open('tasks.txt', 'a', encoding='utf-8') as file:
            file.write(f'{new_task.title}\n')

        print('Задача добавлена!')

    elif choice == '2':
        if len(tasks) == 0:
            print('Список задач пуст')
        else:
            for index, task in enumerate(tasks, start=1):
                
                 if task.is_done:
                     status = '[+]' # Выполнено
                 else:
                     status = '[-]' # Не выполнено
                
                 print(f'{index}. {status} {task.title}')

    elif choice == '3':
        print('До встречи!')
        break

    elif choice == '4':
        try:
            num = int(input('Введите номре задачи: '))
            tasks[num - 1].mark_done()
            print('Задача отмечена!')
        except IndexError:
            print('Ошибка: такой задачи нет!')
        except ValueError:
            print('Ошибка: вводить можно только числа!')
         

    else:
        print('Неверный ввод, пробуйте снова.')