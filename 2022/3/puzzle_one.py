def solve_puzzle(filename):
    total_sum = 0
    with open(filename, 'r') as f:
        for line in f:
            total_sum += get_line_sum(line)
    return total_sum

def get_line_sum(line):
    sum_of_line = 0

    index = len(line)//2

    backpack_one, backpack_two = line[:index], line[index:]
    common_letters = list(set(backpack_one) & set(backpack_two))

    for char in common_letters:
        if char.isupper():
            sum_of_line += ord(char) - 38
        else:
            sum_of_line += ord(char) - 96
    return sum_of_line


print(solve_puzzle('input.txt'))
