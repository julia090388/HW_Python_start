def recSum(a, b):
    if b == 0:
        return a
    return 1 + recSum(a, b - 1)
number1 = int(input('Введите число: '))
number2 = int(input('Введите число: '))
print(f'{number1} + {number2} = {recSum(number1, number2)}')