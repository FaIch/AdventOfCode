def solve_puzzle(filename):
    total_sum = 0
    with open(filename, 'r') as f:
        temp_array = []
        for line in f:
            temp_array.append(line.strip())
            if len(temp_array) == 3:
                total_sum += get_value(temp_array[0], temp_array[1], temp_array[2])
                temp_array.clear()

    return total_sum


def get_value(s1, s2, s3):
    char = list(set(s1) & set(s2) & set(s3))

    if char[0].isupper():
        return ord(char[0]) - 38
    return ord(char[0]) - 96


print(solve_puzzle('input.txt'))
