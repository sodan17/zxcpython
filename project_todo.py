# --- ЗАГРУЗКА ЗАДАЧ ИЗ ФАЙЛА ---
try:

    with open('tasks.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

        tasks =[]
        for line in lines:
            tasks.append(line.strip())
except FileNotFoundError:
    tasks = []


# --- ОСНОВНАЯ ПРОГРАММА ---
while True:
    print('\n--- МЕНЕДЖЕР ЗАДАЧ ---')
    print('1. Добавить задачу')
    print('2. Показать все задачи')
    print('3. Выход')

    choice = input('Ваш выбор: ')

    if choice == '1':
        new_task = input('Что нужно сделать? ')
        tasks.append(new_task)

        with open('tasks.txt', 'a', encoding='utf-8') as file:
            file.write(f'{new_task}\n')

        print('Задача добавлена!')

    elif choice == '2':
        if len(tasks) == 0:
            print('Список задач пуст')
        else:
            for index, task in enumerate(tasks, start=1):
                 print(f'{index}. {task}')

    elif choice == '3':
        print('До встречи!')
        break

    else:
        print('Неверный ввод, пробуйте снова.')