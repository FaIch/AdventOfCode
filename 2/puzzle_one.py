def valid_game(line):
    game_data = line.split(': ')[1]

    games = game_data.split(';')

    for game in games:
        red, green, blue = 0, 0, 0

        components = game.strip().split(',')

        # Extract color values
        for component in components:
            value, color = component.strip().split(' ')
            value = int(value)

            if color == 'red':
                red = value
            elif color == 'green':
                green = value
            elif color == 'blue':
                blue = value

        if red > 12 or green > 13 or blue > 14:
            return False

    return True


def read_file(filename):
    total_sum = 0
    with open(filename, 'r') as f:
        game_id = 1
        while True:
            line = f.readline()
            if not line:
                break
            if valid_game(line):
                total_sum += game_id
            game_id += 1
    print(total_sum)


read_file('input.txt')
