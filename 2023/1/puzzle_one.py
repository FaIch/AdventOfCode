total_sum = 0
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, '1', '2', '3', '4', '5', '6', '7', '8', '9']

with open('input.txt', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        first_num = 0
        last_num = 0
        for char in line:
            if char in numbers:
                if first_num == 0:
                    first_num = char
                last_num = char
        number = first_num + last_num
        total_sum += int(number)
print(total_sum)
