def create_array(filename):
    complete_array = []
    with open(filename, 'r') as f:
        for line in f:
            n = line.index(':') + 1
            unf = line.strip()[n:]
            number = ''

            for char in unf:
                if char != ' ':
                    number += char

            complete_array.append(number)

    return solve_puzzle(complete_array)


def solve_puzzle(array):
    number_of_solutions = 0
    time = int(array[0])
    for i in range(time):
        if i * (time - i) > int(array[1]):
            number_of_solutions += 1

    return number_of_solutions


print(create_array('input.txt'))
