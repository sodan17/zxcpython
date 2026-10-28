my_profile = {
'name': 'Egor',
'age': 16,
'city': 'Rostov',
'hobby': 'program'
}
print(my_profile['name'])

my_profile = {
'name': 'Egor',
'age': 16,
'city': 'Rostov',
'hobby': 'program'
}
my_profile['dream'] = 'стать программистом'
my_profile['age'] += 1
for key, value in my_profile.items():
    print(f'{key}: {value}')

contacts = {} 
while True:
    name = input('Введите имя (или "стоп" для выхода): ')
    if name == 'стоп':
        break
    phone = input('Введите номер телефона: ')
    contacts[name] = phone
for name, phone in contacts.items():
    print(f'{name}: {phone}')

    def calculator(a, b, operation):
        if operation == '+':
            return a + b
        elif operation == '-':
            return a - b
        elif operation == '*':
            return a * b
        elif operation == '/':
            if b == 0:
                return 'Делить на ноль нельзя!'
            else:
                return a / b
        else:
            return 'Неизвестная операция'
print(calculator(5, 2, '+'))
print(calculator(6, 9, '-'))
print(calculator(3, 4, '*'))
print(calculator(8, 2, '/'))
print(calculator(8, 0, '/'))
print(calculator(8, 2, '^'))