number = int(input('Choose any number:'))
if number > 0:
    print('Positive number')
elif number < 0:
    print('Negative number')
elif number == 0:
    print('Equal to zero')


age = int(input('How old are you?'))
if age < 0:
    print('Incorrect age')
elif age <= 12:
    print('You are a child')
elif age <= 17:
    print('You are a teenager')
elif age <= 64:
    print('You are an abult')
elif age >= 65:
    print('You are a pensioner')


password = input('Enter your password:')
if password == 'python123':
    print('Access is allowed')
else: 
    print('Access is prohibited') 
