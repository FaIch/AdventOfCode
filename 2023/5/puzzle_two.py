import copy
from tqdm import tqdm

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
    seeds_info = array[0][7:].split(' ')
    seed_ranges= []

    for i in range(0, len(seeds_info), 2):
        start = int(seeds_info[i])
        length = int(seeds_info[i + 1])
        seed_ranges.append((start, start + length))

    complete_array = [seed_ranges]
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
    min_location = float('inf')

    total_iterations = sum(end - start for start, end in array[0])
    progress = tqdm(total=total_iterations, desc="Processing", unit="seed")

    for start, end in array[0]:
        for seed in range(start, end):
            current_value = seed
            for i in range(1, len(array)):
                for value_map in array[i]:
                    source = int(value_map.source)
                    destination = int(value_map.destination)
                    length = int(value_map.range_length)

                    if source <= current_value <= source + length:
                        current_value = destination + (current_value - source)
                        break
            min_location = min(min_location, current_value)
            progress.update(1)

    progress.close()
    return min_location



if __name__ == '__main__':
    result = parse_array(create_array('input.txt'))
    print(find_location_number(result))
