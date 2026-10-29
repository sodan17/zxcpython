with open('journal.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    count = len(lines)
print(f'Всего записей в журнале: {count}')