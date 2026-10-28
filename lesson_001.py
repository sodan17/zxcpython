import random

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