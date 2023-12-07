from utilities.get_data import get_data
from collections import Counter
def main(mode='silver', data_type=''):
    data = get_data(__file__, data_type)

    hand_ranks = []
    for i in range(0,7):
        hand_ranks.append([])

    letters = {
        "A" : 14,
        "K" : 13,
        "Q" : 12,
        "J" : 11,
        "T" : 10
    }
    if mode == 'gold':
        letters.update({'J' : 1})
    
    def compare_rank(rank_data):
        new_list = []
        for hand in rank_data:
            if not new_list:
                new_list.append(hand)
            else:
                tmp_hand, _ = hand
                for i, new_h in enumerate(new_list):
                    h, _ = new_h
                    for x, a in zip(tmp_hand, h):
                        x = int(x) if x.isdigit() else letters[x]
                        a = int(a) if a.isdigit() else letters[a]
                        if x != a:
                            break
                    if x > a:
                        break
                    elif x == a:
                        break
                    else:
                        continue
                else:
                    new_list.append(hand)
                    continue
                new_list.insert(i, hand)
        return new_list

    if mode =='silver':
        for line in data:
            hand, bid = line.split()

            occurances = Counter(hand)
            if len(occurances) == 1:
                rank = 0
            elif len(occurances) == 2:
                if max(occurances.values()) == 4:
                    rank = 1
                else:
                    rank = 2
            elif len(occurances) == 3:
                if max(occurances.values()) == 3:
                    rank = 3
                else:
                    rank = 4
            elif len(occurances) == 4:
                rank = 5
            else:
                rank = 6
            hand_ranks[rank].append((list(hand), bid))
    else:   # Gold solution
        for line in data:
            hand, bid = line.split()

            occurances = Counter(hand)
            if len(occurances) == 1:
                rank = 0
            elif len(occurances) == 2:
                if 'J' in occurances:
                    rank = 0
                elif max(occurances.values()) == 4:
                    rank = 1
                else:
                    rank = 2
            elif len(occurances) == 3:
                if max(occurances.values()) == 3:
                    rank = 1 if 'J' in occurances else 3
                else:
                    if 'J' in occurances:
                        rank = 1 if occurances['J'] == 2 else 2
                    else:
                        rank = 4
            elif len(occurances) == 4:
                rank = 3 if 'J' in occurances else 5
            else:
                rank = 5 if 'J' in occurances else 6
            hand_ranks[rank].append((list(hand), bid))

    hand_ranks = [compare_rank(hand_rank) for hand_rank in hand_ranks]

    total = 0
    i = 0
    for hand_rank in hand_ranks:
        if not hand_rank: continue
        for hand, bid in hand_rank:
            total += int(bid) * (len(data) - i)
            i+=1

    print(total)
if __name__ == "__main__":
    main('gold')
    # main('gold', data_type='test')
