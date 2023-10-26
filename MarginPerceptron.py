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


def add(v1, v2):
    result = v1
    for i in range(len(v1)):
        result[i] += v2[i]

    return result


def subtract(v1, v2):
    result = v1
    for i in range(len(v1)):
        result[i] -= v2[i]

    return result

def norm(w):
    w_norm = 0
    for i in range(len(w)):
        w_norm += w[i] ** 2
    w_norm = math.sqrt(w_norm)
    return w_norm


def iteration(w_original):
    flag=1
    w = w_original
    for i in range(n):
        point_data = data[i].split(',')[0:d]
        point_data = list(map(float, point_data))
        label = int(data[i].split(',')[-1])
        multiply_result = dot_product(w, point_data)
        if norm(w) != 0:
            distance = multiply_result * label / norm(w)
        else:
            distance = 0

        print(distance)
        if distance < r_guess / 2 or multiply_result * label < 0:
            if label == 1:
                add(w, point_data)
            else:
                subtract(w, point_data)
            return w
        else:
            flag=0

    return w_original,flag

def Training(data, w, t, d, r):
    r_guess=r;
    for n in range(t):
        w,flag=iteration(w)
        if flag==1:
            return True
        else:
            return False
    return False
    

def calculate_margin(weight, n, R):
    # margin is the smallest distance from the points of S to the plane
    margin = R
    for points in range(n):
        point_data = data[points].split(',')[0:d]
        point_data = list(map(float, point_data))
        distance = abs(dot_product(weight, point_data))/norm(weight)
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
        w = [0] * d
        t=math.ceil(12 * (r ** 2) / (r_guess ** 2))
        while Training(data, w, t, d, r):
            r_guess=r_guess/2
        print(data)
