from utilities.get_data import get_data
from collections import Counter
def main(mode='silver', data_type=''):
    data = get_data(__file__, data_type)
    letters = dict(zip('AKQJT98765432', range(14, 1, -1))) # Credit https://github.com/teippa/
    
    if mode == 'gold':
        letters.update({'J' : 1})

    def deduce_level(occurances):
        # Add jokers to highest amount. Idea credit: https://github.com/knuutti/
        jokers = occurances.pop('J') if mode == 'gold' and 'J' in occurances else 0
        match (len(occurances)):
            case 0 | 1: # Five of kind OR All Jokers
                level = 0
            case 2:     # Four of kind OR full house
                level = 1 if max(occurances.values()) + jokers == 4 else 2
            case 3:     # Three of kind OR two pair
                level = 3 if max(occurances.values()) + jokers == 3 else 4
            case 4:     # One Pair
                level = 5
            case 5:     # High card
                level = 6
        return level
    
    hand_levels = [[] for _ in range(0,7)]
    for line in data:
        hand, bid = line.split()
        occurances = Counter(hand)
        level = deduce_level(occurances)
        hand_levels[level].append((list([letters[x] for x in hand]), bid))

    hand_levels = [sorted(hand_level, key=lambda x:x[0],reverse=True) for hand_level in hand_levels]

    total = 0
    rank = 0
    for hand_level in hand_levels:
        for hand, bid in hand_level:
            total += int(bid) * (len(data) - rank)
            rank += 1

    print(f'{mode} : {total}')

if __name__ == "__main__":
    # from time import perf_counter_ns
    main('gold')
    # s = perf_counter_ns()
    # main('gold', data_type='big')
    # e = perf_counter_ns()
    # print(f'per loop: {round((e-s)/1_000_000_000,2)} s')