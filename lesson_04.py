for i in range(1, 11):
    print(i)



total = 0
i = 1

while i <= 100:
    total += i
    i += 1

print(total)



number = int(input('Choose a number:'))
for i in range(1, 11):
    print(f'{number} * {i} = {number * i}')



while True:
    guess = int(input('Guess the number:'))
    if guess == 7:
        print('Got it')
        break
    else:
        print('Mimo, try again')