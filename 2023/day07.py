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
            case 1:
                rank = 0
            case 2:
                rank = 1 if max(occurances.values()) == 4 else 2
            case 3:
                rank = 3 if max(occurances.values()) == 3 else 4
            case 4:
                rank = 5
            case 5:
                rank = 6
        return rank
    
    def gold_logic(occurances):
        match (len(occurances)):
            case 1:
                rank = 0
            case 2:
                if 'J' in occurances:
                    rank = 0
                else:
                    rank = 1 if max(occurances.values()) == 4 else 2
            case 3:
                if max(occurances.values()) == 3:
                    rank = 1 if 'J' in occurances else 3
                else:
                    if 'J' in occurances:
                        rank = 1 if occurances['J'] == 2 else 2
                    else:
                        rank = 4
            case 4:
                rank = 3 if 'J' in occurances else 5
            case 5:
                rank = 5 if 'J' in occurances else 6
        return rank

    hand_ranks = []
    for i in range(0,7):
        hand_ranks.append([])

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