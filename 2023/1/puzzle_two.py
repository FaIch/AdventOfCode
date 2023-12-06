total_sum = 0

numdict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


def find_numbers_in_line(line, numdict):
    numbers = []
    for word, value in numdict.items():
        index = line.find(word)
        while index != -1:
            numbers.append((index, str(value)))
            index = line.find(word, index + 1)
    for i, char in enumerate(line):
        if char.isdigit():
            numbers.append((i, char))
    return numbers


with open('input.txt', 'r') as f:
    for line in f:
        line = line.strip()
        number_occurrences = find_numbers_in_line(line, numdict)

        if number_occurrences:
            number_occurrences.sort()
            first_num = number_occurrences[0][1]
            last_num = number_occurrences[-1][1]
            number = first_num + last_num
            total_sum += int(number)

print(total_sum)
