from enum import IntEnum


class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2


def solve_puzzle(filename):
    total_score = 0
    with open(filename, 'r') as f:
        for line in f:
            total_score += play_game(line[0], line[2])
    return total_score


def determine_winner(your_action, opponent_action):
    if your_action == opponent_action:
        return 3
    elif your_action == Action.Rock:
        if opponent_action == Action.Scissors:
            return 6
        return 0
    elif your_action == Action.Paper:
        if opponent_action == Action.Rock:
            return 6
        return 0
    elif opponent_action == Action.Paper:
        return 6
    return 0


def play_game(opponent_choice, your_choice):
    score = 0

    move_action_dict = {
        'A': 0,
        'B': 1,
        'C': 2,
        'X': 0,
        'Y': 1,
        'Z': 2
    }

    move_value_dict = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }
    score += move_value_dict.get(your_choice)

    your_action = Action(move_action_dict.get(your_choice))
    opponent_action = Action(move_action_dict.get(opponent_choice))
    score += determine_winner(your_action, opponent_action)

    return score


print(solve_puzzle('input.txt'))
