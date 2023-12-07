def solve_puzzle(filename):
    one_pair = []
    two_pairs = []
    three_oak = []
    full_house = []
    four_oak = []
    five_oak = []
    high_card = []

    with open(filename, 'r') as f:
        for line in f:
            hand, bid = line.strip().split()
            bid = int(bid)
            card_count = {}

            for card in hand:
                card_count[card] = card_count.get(card, 0) + 1

            counts = list(card_count.values())
            if 5 in counts:
                five_oak.append((hand, bid))
            elif 4 in counts:
                four_oak.append((hand, bid))
            elif 3 in counts and 2 in counts:
                full_house.append((hand, bid))
            elif 3 in counts:
                three_oak.append((hand, bid))
            elif counts.count(2) == 2:
                two_pairs.append((hand, bid))
            elif 2 in counts:
                one_pair.append((hand, bid))
            else:
                high_card.append((hand, bid))

    sorted_one_pair = sort_hands(one_pair)
    sorted_two_pairs = sort_hands(two_pairs)
    sorted_three_oak = sort_hands(three_oak)
    sorted_full_house = sort_hands(full_house)
    sorted_four_oak = sort_hands(four_oak)
    sorted_five_oak = sort_hands(five_oak)
    sorted_high_card = sort_hands(high_card)

    complete_array = (sorted_high_card + sorted_one_pair + sorted_two_pairs +
                      sorted_three_oak + sorted_full_house + sorted_four_oak + sorted_five_oak)


    total_sum = sum(bid * (rank + 1) for rank, (hand, bid) in enumerate(complete_array))
    return total_sum


def card_strength(card):
    card_order = 'AKQJT98765432'
    return card_order.index(card)


def sort_hands(hands):
    def hand_sort_key(hand):
        return [card_strength(card) for card in hand]

    return sorted(hands, key=lambda hand: hand_sort_key(hand[0]), reverse=True)


print(solve_puzzle('input.txt'))
