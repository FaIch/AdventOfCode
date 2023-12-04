def create_array(filename):
    complete_array = []
    with open(filename, 'r') as f:
        for line in f:
            unpolished = line.strip().split(' ')[2:]
            complete_array.append([i for i in unpolished if i != ''])
    return complete_array


def find_total(array):
    total_sum = 0

    for i in range(len(array)):
        winning_numbers = []
        my_numbers = []
        exponent = -1

        for j in range(len(array[i])):
            split_index = array[i].index('|')
            if j < split_index:
                winning_numbers.append(array[i][j])
            elif j > split_index:
                my_numbers.append(array[i][j])

        for num in my_numbers:
            if num in winning_numbers:
                exponent += 1

        if exponent > -1:
            total_sum += 2**exponent

    return total_sum


def main():
    array = create_array("input.txt")
    print(find_total(array))


if __name__ == "__main__":
    main()
