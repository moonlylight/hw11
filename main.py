from math import factorial, log
import numpy as np

# a) Обчислення елементів послідовності
def sequence_element(x, k):
    return x**(2 * k) / factorial(2 * k)

# b) Обчислення добутку
def product_sequence(n):
    product = 1
    for i in range(1, n + 1):
        product *= (1 + 1 / i**2)
    return product

# c) Обчислення визначника
def determinant(n, a, b):
    matrix = np.zeros((n, n))
    for i in range(n):
        matrix[i][i] = a + b
        if i < n - 1:
            matrix[i][i + 1] = a * b
        if i > 0:
            matrix[i][i - 1] = 1
    return round(np.linalg.det(matrix))

# d) Обчислення суми
def sequence_sum(n):
    a = [1, 1, 1]
    for k in range(3, n):
        a.append(a[k - 1] + a[k - 3])
    return sum(a[k] / 2**(k + 1) for k in range(n))

# e) Обчислення ряду Тейлора для ln((1 + x) / (1 - x))
def taylor_ln(x, epsilon):
    if abs(x) >= 1:
        raise ValueError("x має бути в межах (-1, 1)")
    result, term, k = 0, x, 1
    while abs(term) > epsilon:
        result += term
        term = (x**(2 * k + 1)) / (2 * k + 1)
        k += 1
    return 2 * result

def main():
    # a) Обчислення елементів послідовності
    print("a) Обчислення елементів послідовності:")
    x = float(input("Введіть значення x: "))
    k = int(input("Введіть значення k: "))
    print(f"Елемент послідовності для x = {x}, k = {k}: {sequence_element(x, k)}\n")

    # b) Обчислення добутку
    print("b) Обчислення добутку:")
    n = int(input("Введіть значення n: "))
    print(f"Добуток для n = {n}: {product_sequence(n)}\n")

    # c) Обчислення визначника
    print("c) Обчислення визначника:")
    n = int(input("Введіть порядок визначника n: "))
    a = float(input("Введіть значення a: "))
    b = float(input("Введіть значення b: "))
    print(f"Визначник порядку {n} для a = {a}, b = {b}: {determinant(n, a, b)}\n")

    # d) Обчислення суми
    print("d) Обчислення суми:")
    n = int(input("Введіть значення n: "))
    print(f"Сума для n = {n}: {sequence_sum(n)}\n")

    # e) Обчислення ряду Тейлора для ln((1 + x) / (1 - x))
    print("e) Обчислення ряду Тейлора для ln((1 + x) / (1 - x)):")
    x = float(input("Введіть значення x (|x| < 1): "))
    epsilon = float(input("Введіть точність epsilon: "))
    taylor_result = taylor_ln(x, epsilon)
    math_result = log((1 + x) / (1 - x))
    print(f"Значення ряду Тейлора: {taylor_result}")
    print(f"Значення функції з math: {math_result}\n")

if __name__ == "__main__":
    main()