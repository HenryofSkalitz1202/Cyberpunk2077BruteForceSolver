import random

def random_matrix(rows, cols, elements):
    matrix = []
    for _ in range(rows):
        row = [random.choice(elements) for _ in range(cols)]
        matrix.append(row)

    return matrix

def main_solver_cli():
    numof_unique_tokens = int(input("Number of unique tokens: "))

    token = []
    for i in range(numof_unique_tokens):
        token.append(input(f"Token {i + 1}: "))
    buffer_size = int(input("Buffer size: "))
    matrix_row = int(input("Number of matrix rows: "))
    matrix_column = int(input("Number of matrix columns: "))
    matrix = random_matrix(matrix_row, matrix_column, token)

    numof_sequence = int(input("Number of sequences: "))
    seq_max_size = int(input("Maximum size of sequence: "))

    seq = []
    for _ in range(numof_sequence):
        seq.append([random.choice(token) for _ in range(random.randint(2, seq_max_size))])

    seq_value = [random.randint(10, 50) for _ in range(len(seq))]

    print(seq)
    print(seq_value)


