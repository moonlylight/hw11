from math import factorial, log

# a) Генератор для обчислення елементів послідовності
def sequence_element_gen(x):
    k = 0
    while True:
        yield x**(2 * k) / factorial(2 * k)
        k += 1

def compute_sequence_element(x, k):
    gen = sequence_element_gen(x)
    result = None
    for i in range(k + 1):
        result = next(gen)
    return result

# b) Генератор для обчислення добутку послідовності
def product_sequence_gen():
    i = 1
    product = 1
    while True:
        product *= (1 + 1 / i**2)
        yield product
        i += 1

def compute_product_sequence(n):
    gen = product_sequence_gen()
    result = None
    for i in range(n):
        result = next(gen)
    return result

# c) Генератор для рекурентного визначника
def determinant_gen(n, a, b):
    def determinant(matrix):
        size = len(matrix)
        if size == 1:
            return matrix[0][0]
        if size == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        det = 0
        for col in range(size):
            sub_matrix = [[matrix[i][j] for j in range(size) if j != col] for i in range(1, size)]
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

    matrix = create_matrix(n, a, b)
    yield determinant(matrix)

def compute_determinant(n, a, b):
    gen = determinant_gen(n, a, b)
    return next(gen)

# d) Генератор для обчислення рекурентної суми
def sequence_sum_gen():
    a = [1, 1, 1]
    for k in range(3):
        yield a[k]
    k = 3
    while True:
        next_term = a[k - 1] + a[k - 3]
        a.append(next_term)
        yield next_term
        k += 1

def compute_sequence_sum(n):
    gen = sequence_sum_gen()
    result = 0
    for k in range(n):
        result += next(gen) / 2**(k + 1)
    return result

# e) Генератор для ряду Тейлора
def taylor_ln_gen(x):
    if abs(x) >= 1:
        raise ValueError("x має бути в межах (-1, 1)")
    term = x
    k = 1
    while True:
        yield term
        term = (x**(2 * k + 1)) / (2 * k + 1)
        k += 1

def compute_taylor_ln(x, epsilon):
    gen = taylor_ln_gen(x)
    result = 0
    while True:
        term = next(gen)
        if abs(term) < epsilon:
            break
        result += term
    return 2 * result

def main():
    with open("output.txt", "w") as outfile:
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
        result_a = compute_sequence_element(x_a, k_a)
        outfile.write(f"Елемент послідовності для x = {x_a}, k = {k_a}: {result_a}\n\n")

        # b) Обчислення добутку
        outfile.write("b) Обчислення добутку:\n")
        result_b = compute_product_sequence(n_b)
        outfile.write(f"Добуток для n = {n_b}: {result_b}\n\n")

        # c) Обчислення визначника
        outfile.write("c) Обчислення визначника:\n")
        result_c = compute_determinant(n_c, a_c, b_c)
        outfile.write(f"Визначник порядку {n_c} для a = {a_c}, b = {b_c}: {result_c}\n\n")

        # d) Обчислення суми
        outfile.write("d) Обчислення суми:\n")
        result_d = compute_sequence_sum(n_d)
        outfile.write(f"Сума для n = {n_d}: {result_d}\n\n")

        # e) Обчислення ряду Тейлора
        outfile.write("e) Обчислення ряду Тейлора для ln((1 + x) / (1 - x)):\n")
        result_e = compute_taylor_ln(x_e, epsilon_e)
        math_result = log((1 + x_e) / (1 - x_e))
        outfile.write(f"Значення ряду Тейлора: {result_e}\n")
        outfile.write(f"Значення функції з math: {math_result}\n\n")

if __name__ == "__main__":
    main()