def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return 'Error: Division by zero'
    return a / b

if __name__ == '__main__':
    print(f'5 + 3 = {add(5, 3)}')
    print(f'5 - 3 = {subtract(5, 3)}')
    print(f'5 * 3 = {multiply(5, 3)}')
    print(f'6 / 3 = {divide(6, 3)}')