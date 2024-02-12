import time, random

def is_valid_move(matrix, visited, row, col):
    rows = len(matrix)
    cols = len(matrix[0])
    return 0 <= row < rows and 0 <= col < cols and not visited[row][col]


def find_paths(matrix, visited, row, col, length, path, coor, all_paths, all_coor, direction):
    if length == 0:
        all_paths.append(path[:])
        all_coor.append(coor[:])
        return

    visited[row][col] = True

    if direction == 'horizontal':
        horizontal_dir = []

        for i in range(1, len(matrix[0])):
            horizontal_dir.append((0, i))
            horizontal_dir.append((0, i * -1))

        # Horizontal movements
        for dr, dc in horizontal_dir:
            new_row, new_col = row + dr, col + dc
            if is_valid_move(matrix, visited, new_row, new_col):
                path.append(matrix[new_row][new_col])
                coor.append((new_col + 1, new_row + 1))
                find_paths(matrix, visited, new_row, new_col, length - 1, path, coor, all_paths, all_coor, 'vertical')
                path.pop()
                coor.pop()
    else:
        vertical_dir = []

        for i in range(1, len(matrix[0])):
            vertical_dir.append((i, 0))
            vertical_dir.append((i * -1, 0))

        # Vertical movements
        for dr, dc in vertical_dir:
            new_row, new_col = row + dr, col + dc
            if is_valid_move(matrix, visited, new_row, new_col):
                path.append(matrix[new_row][new_col])
                coor.append((new_col + 1, new_row + 1))
                find_paths(matrix, visited, new_row, new_col, length - 1, path, coor, all_paths, all_coor, 'horizontal')
                path.pop()
                coor.pop()

    visited[row][col] = False

def find_all_paths(matrix, length):
    rows = len(matrix)
    cols = len(matrix[0])
    all_paths = []
    all_coor = []

    for j in range(cols):  # Iterate over cells in the first row only
        visited = [[False] * cols for _ in range(rows)]
        path = [matrix[0][j]]
        coor = [(j + 1, 1)]
        find_paths(matrix, visited, 0, j, length - 1, path, coor, all_paths, all_coor, 'vertical')

    return (all_paths, all_coor)

def isSublist(lst, sub):
    if not sub:
        return True
    if not lst:
        return False

    for i in range(len(lst)):
        if lst[i:i + len(sub)] == sub:
            return True

    return False

def find_max_index(lst):
    if not lst:
        return None  # Return None if the list is empty
    max_value = max(lst)
    max_index = lst.index(max_value)
    return max_index

# Example usage:
def main_solver_txt(matrix, buffer_size, sequences):
    start = time.time()
    all_paths = find_all_paths(matrix, buffer_size)[0]
    all_coor = find_all_paths(matrix, buffer_size)[1]

    score_path = []
    for path in all_paths:
        temp_score = 0
        for sequence in sequences:
            if isSublist(path, sequence[0]):
                temp_score += int(sequence[1])
        score_path.append(temp_score)

    #Print the optimal solution
    str = f"{max(score_path)}\n"

    str += f"{' '.join(all_paths[find_max_index(score_path)])}\n"

    for coor in all_coor[find_max_index(score_path)]:
        str += f"{coor}\n"

    end = time.time()
    res = end - start
    final_res = res * 1000

    str += f"\n{final_res} ms"

    print(f"\n{str}")
    return str

def random_matrix(rows, cols, elements):
    matrix = []
    for _ in range(rows):
        row = [random.choice(elements) for _ in range(cols)]
        matrix.append(row)

    return matrix

def random_sequence(token, seq_max_size, seq):
    a = [random.choice(token) for _ in range(random.randint(2, seq_max_size))]

    #Loop to ensure that every sequence is unique
    loop_stat = False
    while not loop_stat:
        if a in seq:
            a = [random.choice(token) for _ in range(random.randint(2, seq_max_size))]
        else:
            loop_stat = True

    return a

def save_string_to_file(string, filename):
    with open(filename, 'w') as file:
        file.write(string)

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

    start = time.time()

    seq = []
    for _ in range(numof_sequence):
        a = random_sequence(token, seq_max_size, seq)
        seq.append(a)

    seq_value = [random.randint(10, 50) for _ in range(len(seq))]

    all_paths = find_all_paths(matrix, buffer_size)[0]
    all_coor = find_all_paths(matrix, buffer_size)[1]

    score_path = []
    for path in all_paths:
        temp_score = 0
        for sequence in seq:
            if isSublist(path, sequence):
                temp_score += int(seq_value[seq.index(sequence)])
        score_path.append(temp_score)

    # Print the matrix and sequence
    print("")
    str = "Matrix:\n"

    for row in matrix:
        str += f"{row}\n"

    str += f"\nSequence:\n"

    for i in range(len(seq)):
        str += f"{seq[i]}\n"
        str += f"{seq_value[i]}\n"

    str += f"\n{max(score_path)}\n{' '.join(all_paths[find_max_index(score_path)])}\n"

    for coor in all_coor[find_max_index(score_path)]:
        str += f"{coor}\n"

    end = time.time()
    res = end - start
    final_res = res * 1000

    str += f"\n{final_res} ms"

    print(str)
    return str
