def power(line):
    game_data = line.split(': ')[1]
    games = game_data.split(';')
    min_red, min_green, min_blue = float('-inf'), float('-inf'), float('-inf')

    for game in games:
        components = game.strip().split(',')

        for component in components:
            value, color = component.strip().split(' ')
            value = int(value)

            if color == 'red':
                min_red = max(min_red, value)
            elif color == 'green':
                min_green = max(min_green, value)
            elif color == 'blue':
                min_blue = max(min_blue, value)
    print(min_red, min_green, min_blue)

    return min_red * min_green * min_blue


def read_file(filename):
    total_sum = 0
    with open(filename, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            total_sum += power(line)
    print(total_sum)


read_file('input.txt')
