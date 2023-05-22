# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть 
# распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, 
# например, у операции умножения.

def printOperTable(operation, numRows, numColumns):
    arr = [[operation(i, j) for i in range(1, numRows + 1)] for j in range(1, numColumns + 1)]
    for i in arr:
        print(*[f'{x:>4}' for x in i])
line = int(input('Введите количество строк: '))
colums = int(input('Введите количество столбцов: '))
printOperTable(lambda x, y: x * y, line, colums)
