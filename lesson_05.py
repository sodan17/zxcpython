games = ['cs', 'dota', 'resident', 'garis', 'cod']
for game in games:
    print(game)

tasks = []

while True:
    task = input('Business (или "stop"):')
    if task == "stop":
        break
    tasks.append(task)

print(f'All things to do: {len(tasks)}')
for task in tasks:
    print(task)

numbers = [4, 8, 15, 16, 23, 42]

amout = sum(numbers)
print(amout)
print(max(numbers))
print(min(numbers))
count = len(numbers)
average = amout / count
print(average)

numbers = []

for i in range(5):
    num = int(input("Введи число: "))
    numbers.append(num)

print("Обратный порядок:")
print(numbers[::-1])