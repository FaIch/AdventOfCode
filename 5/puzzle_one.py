import copy


class ValueMap:
    def __init__(self, destination, source, range_length):
        self.destination = destination
        self.source = source
        self.range_length = range_length


def create_array(filename):
    complete_array = []
    with open(filename, 'r') as f:
        for line in f:
            if line == '\n':
                continue
            complete_array.append(line.strip())

    return complete_array


def parse_array(array):
    seeds = array[0][7:].split(' ')
    complete_array = [seeds]
    temp_array = []
    for i in range(1, len(array)):
        if array[i][0].isnumeric():
            destination, source, range_length = array[i].split(' ')
            temp_array.append(ValueMap(destination, source, range_length))

            if i == len(array) - 1:
                temp_copy = copy.deepcopy(temp_array)
                complete_array.append(temp_copy)

        elif len(temp_array) > 0:
            temp_copy = copy.deepcopy(temp_array)
            complete_array.append(temp_copy)
            temp_array.clear()

    return complete_array


def find_location_number(array):
    for i in range(1, len(array)):
        for j in range(len(array[0])):
            current_value = int(array[0][j])
            for k in range(len(array[i])):
                source = int(array[i][k].source)
                destination = int(array[i][k].destination)
                length = int(array[i][k].range_length)

                if source <= current_value <= (source + length):
                    array[0][j] = destination + (current_value - source)
                    break

    return min(array[0])

if __name__ == '__main__':
    result = parse_array(create_array('input.txt'))
    print(find_location_number(result))
