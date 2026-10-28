zzz = input()
with open('notes.txt', 'w', encoding="utf-8") as file:
    file.write(zzz)

with open('notes.txt', 'r', encoding='utf-8') as file:
    text = file.read()
print(text)

name = input('Введите ваше имя: ')
date = input('Введите сегодняшнюю дату: ')
with open('journal.txt', 'a', encoding='utf-8') as file:
    file.write(f'{name} - {date}\n')
print('Запись добавлена')

with open('journal.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    count = len(lines)
print(f'Всего записей в журнале: {count}')