import numpy as np


def create_array(filename):
    complete_array = []
    with open(filename, 'r') as f:
        for line in f:
            n = line.index(':') + 1
            unf = line.strip()[n:].split(' ')
            complete_array.append([i for i in unf if i != ''])
    return solve_puzzle(complete_array)


def solve_puzzle(array):
    number_of_solutions = []
    for i in range(len(array[0])):
        number_of_solutions.append(0)
        
    for i in range(len(array[0])):
        for j in range(int(array[0][i])):
            if j * (int(array[0][i])-j) > int(array[1][i]):
                number_of_solutions[i] += 1
    return np.prod(number_of_solutions)


print(create_array('input.txt'))
