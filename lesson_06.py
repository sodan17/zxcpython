def great(name):
    print(f'Привет, {name}!')

great('Egor')
great('Maxim')
great('Blad')


def area(width, height):
    return width * height
result = area(5, 10)
print(result)

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
print(is_even(4))
print(is_even(7))
print(is_even(0))

def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if b == 0:
        return('На ноль делить нельзя')
    else:
        return a / b
        
print(div(5, 5))