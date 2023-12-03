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

    return int(number)


def find_sum(array):
    total_sum = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == '*':
                adjacent = []
                adjacent_index = []
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        if di == 0 and dj == 0:
                            continue
                        ni, nj = i + di, j + dj
                        if 0 <= ni < len(array) and 0 <= nj < len(array[ni]):
                            adjacent.append(array[ni][nj])
                            adjacent_index.append([ni, nj])
                indexes = []
                print(adjacent)
                print(adjacent_index)
                k = 0
                while k < len(adjacent):
                    current_i, current_j = adjacent_index[k]
                    if adjacent[k] in numbers:
                        if [current_i, current_j-1] in indexes:
                            target_index = indexes.index([current_i, current_j-1])
                            indexes[target_index] = adjacent_index[k]
                        elif [current_i, current_j+1] in indexes:
                            index = indexes.index([current_i, current_j+1])
                            indexes[index] = adjacent_index[k]
                        else:
                            indexes.append(adjacent_index[k])

                    k += 1
                if len(indexes) == 2:
                    first_number = find_number(array[indexes[0][0]], indexes[0][1])
                    second_number = find_number(array[indexes[1][0]], indexes[1][1])
                    total_sum += first_number*second_number

            j += 1
        i += 1
    print(total_sum)


def main():
    array = create_array('input.txt')
    find_sum(array)


if __name__ == "__main__":
    main()
