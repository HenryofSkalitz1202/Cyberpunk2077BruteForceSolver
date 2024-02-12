def read_file_to_string(file_path):
    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()
        return file_contents
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None

def main_reader_txt(file_path):
    file_content = read_file_to_string(file_path)

    buffer_size = int(file_content[0])
    matrix_width = int(file_content[2])
    matrix_length = int(file_content[4])

    matrix_idx = 6
    matrix = []
    for i in range(matrix_length):
        a = []
        for j in range(matrix_width):
            a.append(file_content[matrix_idx] + file_content[matrix_idx + 1])
            matrix_idx += 3
        matrix.append(a)

    number_of_sequences = int(file_content[matrix_idx])
    sequences = []
    matrix_idx += 2

    for i in range(number_of_sequences):
        string = ''
        while file_content[matrix_idx] != '\n':
            string += file_content[matrix_idx]
            matrix_idx += 1

        matrix_idx += 1

        score = ''
        while (file_content[matrix_idx] != '\n') and (matrix_idx < len(file_content) - 1):
            score += file_content[matrix_idx]
            matrix_idx += 1

        if matrix_idx == len(file_content) - 1:
            score += file_content[matrix_idx]

        if i != number_of_sequences - 1:
            matrix_idx += 1

        sequences.append((string.split(), score))

    return matrix, buffer_size, sequences
