import copy


def create_array(filename):
    complete_array = []
    with open(filename, 'r') as f:
        temp_array = []
        for line in f:
            if line == '\n':
                res = [eval(i) for i in copy.deepcopy(temp_array)]
                complete_array.append(res)
                temp_array.clear()
            else:
                temp_array.append(line.strip())
    return solve_puzzle(complete_array)


def solve_puzzle(array):
    calories = []
    for i in array:
        calories.append(sum(i))

    calories.sort(reverse=True)
    sum_top_three = 0

    for i in range(3):
        sum_top_three += calories[i]

    return sum_top_three


print(create_array('input.txt'))
