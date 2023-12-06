import numpy as np

def create_array(filename):
    complete_array = []
    with open(filename, 'r') as f:
        for line in f:
            unpolished = line.strip().split(' ')[2:]
            complete_array.append([i for i in unpolished if i != ''])
    return complete_array


def find_total(array):
    total_cards = 0
    array_length = len(array)
    amount_of_cards = np.full(array_length, 1)

    for i in range(array_length):
        winning_numbers = []
        my_numbers = []
        correct_numbers = 0

        for j in range(len(array[i])):
            split_index = array[i].index('|')
            if j < split_index:
                winning_numbers.append(array[i][j])
            elif j > split_index:
                my_numbers.append(array[i][j])

        for num in my_numbers:
            if num in winning_numbers:
                correct_numbers += 1

        for k in range(1, correct_numbers+1):
            if i + k <= len(amount_of_cards):
                amount_of_cards[i + k] = amount_of_cards[i + k] + amount_of_cards[i]

    for i in range(len(amount_of_cards)):
        total_cards += amount_of_cards[i]

    return total_cards


def main():
    array = create_array("input.txt")
    print(find_total(array))


if __name__ == "__main__":
    main()
