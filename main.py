from math import factorial, log

# a) Обчислення елементів послідовності
def sequence_element(x, k):
    return x**(2 * k) / factorial(2 * k)

# b) Обчислення добутку
def product_sequence(n):
    product = 1
    for i in range(1, n + 1):
        product *= (1 + 1 / i**2)
    return product

# c) Обчислення визначника без numpy
def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for col in range(n):
        sub_matrix = [[matrix[i][j] for j in range(n) if j != col] for i in range(1, n)]
        det += ((-1)**col) * matrix[0][col] * determinant(sub_matrix)
    return det

def create_matrix(n, a, b):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        matrix[i][i] = a + b
        if i < n - 1:
            matrix[i][i + 1] = a * b
        if i > 0:
            matrix[i][i - 1] = 1
    return matrix

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
    with open("output.txt", "w") as outfile:
        # Вже задані дані
        x_a = 2
        k_a = 5
        n_b = 5
        n_c = 4
        a_c = 2
        b_c = 3
        n_d = 10
        x_e = 0.5
        epsilon_e = 1e-6

        # a) Обчислення елементів послідовності
        outfile.write("a) Обчислення елементів послідовності:\n")
        result_a = sequence_element(x_a, k_a)
        outfile.write(f"Елемент послідовності для x = {x_a}, k = {k_a}: {result_a}\n\n")

        # b) Обчислення добутку
        outfile.write("b) Обчислення добутку:\n")
        result_b = product_sequence(n_b)
        outfile.write(f"Добуток для n = {n_b}: {result_b}\n\n")

        # c) Обчислення визначника
        outfile.write("c) Обчислення визначника:\n")
        matrix = create_matrix(n_c, a_c, b_c)
        result_c = determinant(matrix)
        outfile.write(f"Визначник порядку {n_c} для a = {a_c}, b = {b_c}: {result_c}\n\n")

        # d) Обчислення суми
        outfile.write("d) Обчислення суми:\n")
        result_d = sequence_sum(n_d)
        outfile.write(f"Сума для n = {n_d}: {result_d}\n\n")

        # e) Обчислення ряду Тейлора для ln((1 + x) / (1 - x))
        outfile.write("e) Обчислення ряду Тейлора для ln((1 + x) / (1 - x)):\n")
        taylor_result = taylor_ln(x_e, epsilon_e)
        math_result = log((1 + x_e) / (1 - x_e))
        outfile.write(f"Значення ряду Тейлора: {taylor_result}\n")
        outfile.write(f"Значення функції з math: {math_result}\n\n")

if __name__ == "__main__":
    main()