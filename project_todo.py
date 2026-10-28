tasks = []
while True:
    print('\n--- МЕНЕДЖЕР ЗАДАЧ ---')
    print('1. Добавить задачу')
    print('2. Показать все задачи')
    print('3. Выход')

    choice = input('Ваш выбор: ')

    if choice == '1':
        new_task = input('Что нужно сделать? ')
        tasks.append(new_task)
    elif choice == '2':
        for index, task in enumerate(tasks, start=1):
            print(f'{index}. {task}')
    elif choice == '3':
        print('До встречи!')
        break
    else:
        print('Неверный ввод, пробуйте снова.')