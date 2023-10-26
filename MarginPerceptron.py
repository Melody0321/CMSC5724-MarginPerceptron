import numpy as np
import math

def read_file(file_name):
    with open(file_name, 'r') as f:
        first = next(f).strip('\n').split(',')
        lines = f.readlines()
    f.close()
    for i in range(0, len(lines)):
        lines[i] = lines[i].strip('\n')

    return first, lines


def dot_product(v1, v2):
    result = 0
    for i in range(len(v1)):
        result += v1[i] * v2[i]
    return result


def norm(w):
    w_norm = 0
    for i in range(len(w)):
        w_norm += w[i] ** 2
    w_norm = math.sqrt(w_norm)
    return w_norm


def calculate_margin(weight, n, R):
    # margin is the smallest distance from the points of S to the plane
    margin = R
    for points in range(n):
        distance = abs(dot_product(weight, data[points]))/norm(weight)
        if distance < margin:
            margin = distance
    return margin

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
