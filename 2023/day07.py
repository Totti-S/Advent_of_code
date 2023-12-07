from utilities.get_data import get_data
from collections import Counter
def main(mode='silver', data_type=''):
    data = get_data(__file__, data_type)

    letters = { "A" : 14, "K" : 13, "Q" : 12, "J" : 11, "T" : 10, "9" : 9, 
                "8" : 8, "7" : 7, "6" : 6, "5" : 5, "4" : 4, "3" : 3, "2": 2}
    
    if mode == 'gold':
        letters.update({'J' : 1})
    
    def compare_rank(rank_data):
        new_list = []
        for hand_and_bid in rank_data:
            hand, _ = hand_and_bid
            for i, new_h in enumerate(new_list):
                h, _ = new_h
                for card, list_card in zip(hand, h):
                    card = letters[card]
                    list_card = letters[list_card]
                    if card != list_card:
                        break
                if card >= list_card:
                    break
                else:
                    continue
            else:
                new_list.append(hand_and_bid)
                continue
            new_list.insert(i, hand_and_bid)
        return new_list
    
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
        hand_levels[level].append((list(hand), bid))
    
    hand_levels = [compare_rank(hand_level) for hand_level in hand_levels] # Sort inside the rank

    total = 0
    rank = 0
    for hand_level in hand_levels:
        for hand, bid in hand_level:
            total += int(bid) * (len(data) - rank)
            rank += 1

    print(f'{mode} : {total}')
if __name__ == "__main__":
    main('gold')