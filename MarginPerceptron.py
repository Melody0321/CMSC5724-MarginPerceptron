import numpy as np


def read_file(file_name):
    with open(file_name, 'r') as f:
        first = next(f).strip('\n').split(',')
        lines = f.readlines()
    f.close()
    for i in range(0, len(lines)):
        lines[i] = lines[i].strip('\n')

    return first, lines


if __name__ == "__main__":
    files = ['2d-r16-n10000', '4d-r24-n10000', '8d-r12-n10000']
    for file in files:
        first_line, data = read_file(file)
        print(first_line)
        d = int(first_line[0])  # dimensionality
        n = int(first_line[1])  # points_number
        r = int(first_line[2])  # radius
        r_guess = r
        print(data)
