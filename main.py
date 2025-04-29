from math import factorial, log
import numpy as np

def sequence_element(x, k):
    return x**(2 * k) / factorial(2 * k)

def product_sequence(n):
    product = 1
    for i in range(1, n + 1):
        product *= (1 + 1 / i**2)
    return product

def determinant(n, a, b):
    matrix = np.zeros((n, n))
    for i in range(n):
        matrix[i][i] = a + b
        if i < n - 1:
            matrix[i][i + 1] = a * b
        if i > 0:
            matrix[i][i - 1] = 1
    return round(np.linalg.det(matrix))

def sequence_sum(n):
    a = [1, 1, 1]
    for k in range(3, n):
        a.append(a[k - 1] + a[k - 3])
    return sum(a[k] / 2**(k + 1) for k in range(n))

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
    with open("output.txt", "w") as outfile:
        # a) Обчислення елементів послідовності
        outfile.write("a) Обчислення елементів послідовності:\n")
        x = float(input("Введіть значення x: "))
        k = int(input("Введіть значення k: "))
        result_a = sequence_element(x, k)
        outfile.write(f"Елемент послідовності для x = {x}, k = {k}: {result_a}\n\n")

        # b) Обчислення добутку
        outfile.write("b) Обчислення добутку:\n")
        n = int(input("Введіть значення n: "))
        result_b = product_sequence(n)
        outfile.write(f"Добуток для n = {n}: {result_b}\n\n")

        # c) Обчислення визначника
        outfile.write("c) Обчислення визначника:\n")
        n = int(input("Введіть порядок визначника n: "))
        a = float(input("Введіть значення a: "))
        b = float(input("Введіть значення b: "))
        result_c = determinant(n, a, b)
        outfile.write(f"Визначник порядку {n} для a = {a}, b = {b}: {result_c}\n\n")

        # d) Обчислення суми
        outfile.write("d) Обчислення суми:\n")
        n = int(input("Введіть значення n: "))
        result_d = sequence_sum(n)
        outfile.write(f"Сума для n = {n}: {result_d}\n\n")

        # e) Обчислення ряду Тейлора для ln((1 + x) / (1 - x))
        outfile.write("e) Обчислення ряду Тейлора для ln((1 + x) / (1 - x)):\n")
        x = float(input("Введіть значення x (|x| < 1): "))
        epsilon = float(input("Введіть точність epsilon: "))
        taylor_result = taylor_ln(x, epsilon)
        math_result = log((1 + x) / (1 - x))
        outfile.write(f"Значення ряду Тейлора: {taylor_result}\n")
        outfile.write(f"Значення функції з math: {math_result}\n\n")

if __name__ == "__main__":
    main()