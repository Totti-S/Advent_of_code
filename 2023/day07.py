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
    
    def silver_logic(occurances):
        match (len(occurances)):
            case 1:     # Five of kind
                rank = 0
            case 2:     # Four of kind OR full house
                rank = 1 if max(occurances.values()) == 4 else 2
            case 3:     # Three of kind OR two pair
                rank = 3 if max(occurances.values()) == 3 else 4
            case 4:     # One Pair
                rank = 5
            case 5:     # High card
                rank = 6
        return rank
    
    def gold_logic(occurances):
        pre_joker_rank = silver_logic(occurances)
        if 'J' not in occurances:   # If no jokers present rank is what it needs to be
            return pre_joker_rank

        # We convert the 'before joker'- rank. This easily preditable 
        # what the rank should be, if we know what hand we have before
        rank = -1
        match (pre_joker_rank):
            case 0 | 1 | 2: # Five OR four of kind OR full house
                rank = 0
            case 3:         # Three of kind
                rank = 1
            case 4:         # Two pair
                rank = 1 if occurances['J'] == 2 else 2
            case 5:         # One pair
                rank = 3
            case 6:         # High card
                rank = 5
        return rank

    hand_ranks = [[] for _ in range(0,7)]
    logic_func = gold_logic if mode == 'gold' else silver_logic

    for line in data:
        hand, bid = line.split()
        occurances = Counter(hand)
        rank = logic_func(occurances)
        hand_ranks[rank].append((list(hand), bid))
    hand_ranks = [compare_rank(hand_rank) for hand_rank in hand_ranks]

    total = 0
    i = 0
    for hand_rank in hand_ranks:
        for hand, bid in hand_rank:
            total += int(bid) * (len(data) - i)
            i += 1

    print(f'{mode} : {total}')
if __name__ == "__main__":
    main('gold')