a = int(input("Введите число: "))
b = int(input("В какую степень возвести число: "))
def raise_degree(a, b):
    if b == 1:
        return a
    if b != 1:
        return a * raise_degree(a, b - 1)
print(raise_degree(a, b))