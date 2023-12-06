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


def play_to_lose(opponent_action):
    if opponent_action == Action.Rock:
        return 3
    elif opponent_action == Action.Paper:
        return 1
    return 2


def play_to_win(opponent_action):
    if opponent_action == Action.Rock:
        return 2
    elif opponent_action == Action.Paper:
        return 3
    return 1


def play_game(opponent_choice, your_choice):
    score = 0

    move_action_dict = {
        'A': 0,
        'B': 1,
        'C': 2,
    }

    move_value_dict = {
        Action.Rock: 1,
        Action.Paper: 2,
        Action.Scissors: 3
    }

    outcome_dict = {
        'X': 0,
        'Y': 3,
        'Z': 6
    }
    outcome_value = outcome_dict.get(your_choice)
    score += outcome_value

    opponent_action = Action(move_action_dict.get(opponent_choice))

    if outcome_value == 0:
        score += play_to_lose(opponent_action)
    elif outcome_value == 6:
        score += play_to_win(opponent_action)
    else:
        score += move_value_dict.get(opponent_action)

    return score


print(solve_puzzle('input.txt'))
