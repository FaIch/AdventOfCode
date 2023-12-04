numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def create_array(filename):
    complete_array = []
    with open(filename, 'r') as f:
        for line in f:
            complete_array.append(list(line.strip()))
    return complete_array


def find_number(array, i):
    number = array[i]

    left = i - 1
    while left >= 0 and array[left] in numbers:
        number = array[left] + number
        left -= 1

    right = i + 1
    while right < len(array) and array[right] in numbers:
        number += array[right]
        right += 1

    push = right - i - 1

    return int(number), push


def find_sum(array):
    symbols = set('!@#$%^&*()-+?_=,<>/')
    total_sum = 0

    for i in range(len(array)):
        j = 0
        while j < len(array[i]):
            if array[i][j] in numbers:
                adjacent_symbol = False
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        if di == 0 and dj == 0:
                            continue
                        ni, nj = i + di, j + dj
                        if 0 <= ni < len(array) and 0 <= nj < len(array[ni]) and array[ni][nj] in symbols:
                            adjacent_symbol = True
                            break
                    if adjacent_symbol:
                        break

                if adjacent_symbol:
                    number, push = find_number(array[i], j)
                    total_sum += number
                    j += push

            j += 1

    print(total_sum)


def main():
    array = create_array('input.txt')
    find_sum(array)


if __name__ == "__main__":
    main()
