import random 
tell = input('Бросьте кубик: ')
if tell == 'Бросил':
    print(f'Выпало: {random.randint(1, 6)}')

import random
secret_number = random.randint(1, 100)
while True:
    guess = int(input('Guess the number from 1 to 100:'))
    if guess == secret_number:
        print('Got it')
        break
    else:
        print('Mimo, try again')

import random
movies = ['Аватар', 'Мстители', 'Титаник', 'Переводчик', 'Интерстейлар']
print(random.choice(movies))

import datetime 
name = input('Введите ваше имя: ')
with open('journal.txt', 'a', encoding='utf-8') as file:
    file.write(f'{name} - {datetime.datetime.now().strftime('%d.%m.%Y')}\n')
print('Запись добавлена!')