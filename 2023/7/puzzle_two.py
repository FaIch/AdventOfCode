def solve_puzzle(filename):
    categorized_hands = {'one_pair': [], 'two_pairs': [], 'three_oak': [],
                         'full_house': [], 'four_oak': [], 'five_oak': [],
                         'high_card': []}

    with open(filename, 'r') as f:
        for line in f:
            hand, bid = line.strip().split()
            bid = int(bid)

            category = replace_jokers_and_evaluate(hand)
            categorized_hands[category].append((hand, bid))

    for category in categorized_hands:
        categorized_hands[category] = sort_hands(categorized_hands[category])

    complete_array = (categorized_hands['high_card'] + categorized_hands['one_pair'] +
                      categorized_hands['two_pairs'] + categorized_hands['three_oak'] +
                      categorized_hands['full_house'] + categorized_hands['four_oak'] +
                      categorized_hands['five_oak'])

    total_sum = sum(bid * (rank + 1) for rank, (hand, bid) in enumerate(complete_array))
    return total_sum


hand_rank_order = ['high_card', 'one_pair', 'two_pairs', 'three_oak', 'straight', 'flush', 'full_house', 'four_oak', 'straight_flush', 'five_oak']


def replace_jokers_and_evaluate(hand):

    joker_replacements = 'AKQT98765432'
    best_hand_type = 'high_card'

    if hand.count('J') == 0:
        return categorize_hand(hand)

    for replacement in joker_replacements:
        new_hand = hand.replace('J', replacement, 1)
        if hand.count('J') > 1:
            inner_best = replace_jokers_and_evaluate(new_hand)
            if hand_rank_order.index(inner_best) > hand_rank_order.index(best_hand_type):
                best_hand_type = inner_best
        else:
            current_type = categorize_hand(new_hand)
            if hand_rank_order.index(current_type) > hand_rank_order.index(best_hand_type):
                best_hand_type = current_type

    return best_hand_type


def categorize_hand(hand):
    card_count = {card: hand.count(card) for card in set(hand)}

    counts = list(card_count.values())
    unique_counts = set(counts)

    if 5 in unique_counts:
        return 'five_oak'

    if 4 in unique_counts:
        return 'four_oak'

    if 3 in unique_counts and 2 in unique_counts:
        return 'full_house'

    if 3 in unique_counts:
        return 'three_oak'

    if counts.count(2) == 2:
        return 'two_pairs'

    if 2 in unique_counts:
        return 'one_pair'

    return 'high_card'


def card_strength(card):
    card_order = 'AKQT98765432J'
    return card_order.index(card)


def sort_hands(hands):
    def hand_sort_key(hand):
        return [card_strength(card) for card in hand]

    return sorted(hands, key=lambda hand: hand_sort_key(hand[0]), reverse=True)


print(solve_puzzle('input.txt'))
