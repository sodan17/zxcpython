import random
# --- №1
try:
    a = int(input('Введите первое число:'))
    b = int(input('Введите второе число: '))
    operation = input('Введите операцию (+, -, *, /): ')

    if operation == '+':
        print(f'Результат: {a + b}')
    elif operation == '-':
        print(f'Результат: {a - b}')
    elif operation == '*':
        print(f'Результат: {a * b}')
    elif operation == '/':
        print(f'Решение: {a / b}')
    else:
        print('Неизвестная операция')

except ValueError:
    print('Ошибка: Вы ввели не число!.')
except ZeroDivisionError:
    print('Ошибка: на ноль делить нельзя!')

# --- №2 and №3

def safe_input(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print('Это не число! Пробуй еще')

secret_number = random.randint(1, 100)

while True:
    guess = safe_input('Guess the number from 1 to 100:')

    if guess == secret_number:
        print('Got it')
        break
    else:
        print('Mimo, try again')